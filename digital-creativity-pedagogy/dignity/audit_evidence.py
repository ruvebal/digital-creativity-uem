"""Verified bibliographic corrections and full-node evidence audit.

No date is inferred from PDF creation metadata, filenames or event dates.
All corrections preserve their prior values and documentary justification.
"""
from pathlib import Path
import json, sqlite3, subprocess
ROOT=Path(__file__).resolve().parent
LIB=Path('/Users/ruvebal/ahmes-library/scholar/documents')
AHMES='/Users/ruvebal/src/ahmes/.venv/bin/ahmes'
CORPUS=Path('/Users/ruvebal/projects/ruvebal/scholar/dignity/.ahmes/batch-manifest.json')

def coat(db, values, reason, receipts):
 with sqlite3.connect(db) as conn:
  before={r[0]:{'value':r[1],'confidence':r[2],'method':r[3]} for r in conn.execute('select key,value,confidence,method from metadata')}
  for key,value in values.items():
   if not isinstance(value,str): value=json.dumps(value,ensure_ascii=False)
   conn.execute('insert or replace into metadata(key,value,confidence,method) values(?,?,1.0,?)',(key,value,'human'))
  conn.commit()
 receipts.append({'db':str(db),'before':before,'verified_values':values,'basis':reason,'reviewer':'Codex source verification, 2026-10-20'})

def nodes(db, term, limit=3):
 with sqlite3.connect(db) as conn:
  return conn.execute('select n.node_id,s.page_index,n.markdown_content from fission_node n left join anchor_spatial s using(node_id) where lower(n.markdown_content) like lower(?) and length(n.markdown_content)>50 order by length(n.markdown_content) desc limit ?',('%'+term+'%',limit)).fetchall()

def evidence(key,db,term,boundary,rows):
 found=nodes(db,term)
 for node,page,content in found:
  result=subprocess.run([AHMES,'query','--cite',str(db)+':'+node,'--style','chicago-author-date'],capture_output=True,text=True)
  basis='PDF order; page_index+1, not inferred printed pagination'
  if key.startswith(('asa-','acm-','udhr-','pantano-','spain-')):
   basis='Primary web/XML snapshot; synthetic Markdown page 0 is not a printed page and is not cited publicly as page 1'
  rows.append({'key':key,'db':str(db),'node':node,'page_index':page,'page_basis':basis,'content':content,'resolver':result.stdout+result.stderr,'returncode':result.returncode,'supports':term,'does_not_support':boundary})

if __name__=='__main__':
 receipts=[]; rows=[]
 manifest=json.loads(CORPUS.read_text())
 for source,entry in manifest.items():
  db=Path(entry['outputs']['extraction_db']);name=Path(source).name
  values={}
  if name.startswith('Fichas'):
   values={'title':'Dignidad e innovación educativa: Banco de buenas prácticas','organization':'Global Dignity España and Fundación AYO','year':'2026'}
   reason='PDF cover: 21 fichas · Actualización junio 2026; repeated footer: Global Dignity España · Fundación AYO. PDF page 17 visually inspected (case GD16).'
  elif name.startswith('Dignity'):
   values={'title':'Dignidad: Lo esencial','organization':'Global Dignity'}
   reason='PDF cover and final Global Dignity branding; publication year absent. Creation timestamp is not a publication date.'
  elif name.startswith('Guía'):
   values={'title':'Guía del facilitador: Workshop Dignity','organization':'Global Dignity'}
   reason='PDF cover and welcome identify the workshop and organization; publication year absent. PDF template author is not promoted to intellectual author.'
  elif name.startswith('GD '):
   values={'title':'Global Dignity: Red de Embajadores y Embajadoras de la Dignidad','organization':'Global Dignity'}
   reason='PDF page 1 title; publication year absent. Historical dates in the body do not date the edition.'
  else:
   values={'title':'Formación Embajadores y Embajadoras de la Dignidad: Cuéntanos tu experiencia'}
   reason='Single-page heading; no verified publication year or intellectual author. June 2027 event date is not publication date.'
  coat(db,values,reason,receipts)
  evidence('corpus-'+db.parent.parent.name,db,'dignidad','Documentary or normative teaching resource, not a measured learning-effect study.',rows)
  if name.startswith('Fichas'):
   evidence('gd-textile',db,'En equipos de 4-6','Documented practice GD16, PDF page 17. Teacher report, not an independent efficacy evaluation; adapted activity does not inherit institutional endorsement.',rows)

 # Correct a demonstrably misattributed existing vault record, using its own title/copyright pages.
 freire=LIB/'freire_2000_untitled_f6c6d412/extract/extraction.db'
 coat(freire,{'title':'Pedagogy of the Oppressed','authors':[{'kind':'person','given':'Paulo','family':'Freire'}],'year':'2000'},
      'PDF index 4: PAULO FREIRE, PEDAGOGY of the OPPRESSED, 30TH ANNIVERSARY EDITION. PDF index 5: First published in 2000 by the Continuum International Publishing Group Inc; later reprint dates retained as edition history. Bloomsbury was wrongly treated as author.',receipts)
 evidence('freire-dialogue',freire,'Liberating education','Critical-pedagogy framework; not a controlled evaluation of these fashion activities.',rows)
 abidin=LIB/'abidin_2016_visibility_labour_engaging_with_influencers_fashion_brands_and_ootd_advertorial_campaigns_on_instagram_f13f6ee0/extract/extraction.db'
 evidence('abidin-visibility',abidin,'under-compensated','Study of particular Instagram practices; does not establish present platform prevalence or every follower’s motives.',rows)
 browne=LIB/'browne_simone_dark_matters_on_the_surveillance_of_blackness_2015_duke_university_press_92b84660/extract/extraction.db'
 evidence('browne-commodity',browne,'McClintock','Historical critical lens; not evidence that a particular contemporary advertisement reproduces the same mechanism.',rows)
 unep=LIB/'sustainable_fashion_communication_playbook_08e2ea03/extract/extraction.db'
 evidence('unep-consumption',unep,'perpetuating overconsumption','Practitioner/normative guidance; not proof that changing a campaign reduces purchases or improves labour conditions.',rows)

 primary=json.loads((ROOT/'primary-sources.json').read_text())
 supplementary=json.loads((ROOT/'source-snapshots/.ahmes/batch-manifest.json').read_text())
 terms={'asa-boohoo-2022':'objectified','asa-gucci-2016':'unhealthily thin',
        'asa-calvin-klein-2024':'confident','acm-hm-2022':'commitments',
        'udhr-1948':'equal in dignity','pantano-2021':'chopsticks',
        'srivastava-2022':'stereotypes','spain-advertising-1988':'dignidad',
        'udhr-articles-1948':'All human beings are born'}
 for source,entry in supplementary.items():
  key=Path(source).stem;record=next(d for d in primary if d['id']==key)
  db=Path(entry['outputs']['extraction_db'])
  values={k:record[k] for k in ['title','organization','authors','year','doi'] if k in record}
  values['source_url']=record['url']
  coat(db,values,'Verified against primary source heading/date, DOI registry and publisher/repository record; primary-sources.json records acquisition limitations. ASA text snapshot is an explicitly identified short web-tool excerpt.',receipts)
  evidence(key,db,terms[key],
      'Specific source and jurisdiction/date only. No universal harm, causation, diagnosis, copyright clearance or new legal obligation inferred.',rows)
 # Append-only correction receipts preserve earlier states on reruns.
 corrections=ROOT/'bibliographic-corrections.json'
 existing=json.loads(corrections.read_text()) if corrections.exists() else []
 corrections.write_text(json.dumps(existing+receipts,ensure_ascii=False,indent=2))
 (ROOT/'evidence-nodes.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
 print(json.dumps({'corrections':len(receipts),'evidence_nodes':len(rows),'safe_resolutions':sum('evaluator_safe=yes' in r['resolver'] for r in rows),'gaps':sum('evaluator_safe=yes' not in r['resolver'] for r in rows)},indent=2))
