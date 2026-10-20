"""Refresh only this cascade's isolated project metadata, preserving nodes.

The CLI intentionally treats completed injections as no-ops, including after
verified bibliography corrections. Use its existing document upsert adapter
to synchronise the document coat; record the full prior metadata for rollback.
"""
from pathlib import Path
import asyncio,json,os,sqlite3
from uuid import UUID
import psycopg
from psycopg import sql
from psycopg.rows import dict_row
from athanor_api.infrastructure.postgres.corpus import PostgresCorpusRepository
from athanor_api.application.use_cases import InjectionService
ROOT=Path(__file__).resolve().parent

async def main():
 repo=PostgresCorpusRepository(os.environ['DATABASE_URL'])
 project=await repo.get_project_by_slug('scholar-dignity','scholar')
 assert project and project.slug=='scholar-dignity'
 assert project.schema_name=='project_'+project.project_id.hex
 manifests=[Path('/Users/ruvebal/projects/ruvebal/scholar/dignity/.ahmes/batch-manifest.json'),ROOT/'source-snapshots/.ahmes/batch-manifest.json']
 receipts=[]
 for path in manifests:
  for entry in json.loads(path.read_text()).values():
   if entry.get('status')!='PROCESSED_OK':continue
   db=entry['outputs']['extraction_db']
   with sqlite3.connect(db) as conn:
    conn.row_factory=sqlite3.Row
    source=dict(conn.execute('select * from source').fetchone())
    metadata,title=InjectionService._read_metadata(conn,source['file_name'])
   document_id=UUID(source['document_id'])
   with psycopg.connect(os.environ['DATABASE_URL'],row_factory=dict_row) as connection:
    before=connection.execute(sql.SQL('select * from {}.document where document_id=%s').format(sql.Identifier(project.schema_name)),(document_id,)).fetchone()
   assert before,'Document not previously ingested: '+str(document_id)
   document=dict(before);document['title']=title;document['metadata']=metadata
   await repo.upsert_document(project.schema_name,document)
   receipts.append({'document_id':str(document_id),'db':db,'before':dict(before),'after_title':title,'after_metadata':metadata})
 (ROOT/'index-metadata-refresh.json').write_text(json.dumps({'project_slug':'scholar-dignity','reason':'Synchronise verified bibliography corrections after idempotent CLI skipped metadata-only changes','documents':receipts},default=str,ensure_ascii=False,indent=2))
 print('Refreshed bibliography metadata for',len(receipts),'documents; no nodes or embeddings changed.')

if __name__=='__main__':asyncio.run(main())
