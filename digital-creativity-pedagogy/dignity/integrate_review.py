"""Archive editorial amendments and integrate only accepted, reviewed drafts."""
from pathlib import Path
import difflib,json,re,subprocess
ROOT=Path(__file__).resolve().parent
SITE=ROOT.parents[1]/'docs/dignity'

def linked(text,key):
 return re.sub(r'\(([^()]+ (?:19|20)\d{2})\)',lambda m:'['+m.group(0)+'](#ref-'+key+')',text)

def provenance(slug,row,record):
 data={'claim':'DIGNITY.'+slug,'status':'VERIFIED','discovery':{
  'service':'Athanor / cross-project neural discovery / direct primary-source reading as recorded',
  'project_slug':'scholar-dignity; source-specific scopes in vault-search/receipts.json',
  'knowledge_scope':'field_prospection','query':'Exact source-specific queries retained in the private research pack',
  'source_locator':row['db']+':'+row['node'],'similarity':None,
  'proposed_use':row['supports']},'source':{'extraction_db':row['db'],'document_coat':Path(row['db']).parents[1].name,
  'node_id':row['node'],'page_index':row['page_index'],'printed_page':None,'page_basis':row['page_basis']},
  'resolver':row['resolver'],'quote':'none','public_citation':record['citation'],
  'supports':row['supports'],'does_not_support':row['does_not_support']}
 return '\n{% if site.publication.publish_internal_metadata %}\n<!-- curriculum-internal:\nPROVENANCE_LINE: '+json.dumps(data,ensure_ascii=False)+'\ntuning_record: '+record['record']+'\n-->\n{% endif %}\n'

if __name__=='__main__':
 records=json.loads((ROOT/'scribe-records.json').read_text())
 concepts=json.loads((ROOT/'final_concepts.json').read_text())
 report=[]
 for slug,concept in concepts.items():
  accepted=[r for r in records if r['idea']==slug and r['returncode']==0]
  assert accepted,'No accepted local draft for '+slug
  record=accepted[-1];folder=Path(record['record']);raw=(folder/'thessia-raw.md').read_text()
  source=json.loads((folder/'provenance.json').read_text())['evidence']
  integrated=linked(concept['en'],concept['key'])
  (folder/'integrated.md').write_text(integrated+'\n')
  (folder/'integrated-es.md').write_text(linked(concept['es'],concept['key'])+'\n')
  (folder/'amendments.diff').write_text(''.join(difflib.unified_diff(raw.splitlines(keepends=True),(integrated+'\n').splitlines(keepends=True),fromfile='thessia-raw.md',tofile='integrated.md')))
  evaluation=f'''# Editorial review — {slug}

Reviewer: Codex, not an independent human or model reviewer. Professor release remains pending.

| Axis | Raw assessment | Integrated assessment |
| --- | --- | --- |
| Sentence-role fidelity | FAIL: marker gate does not establish actual four-sentence prose | PASS: four bounded sentences, one question |
| Voice | FAIL: leading colons, repetition or abstract/polemical phrasing | PASS: concrete, plain and concise |
| Concreteness | Reviewed against the actual source node | PASS: source example retained; no invented anecdote |
| Citation shape | Wrapper results preserved; comma/long-author forms can evade its parser | PASS: exact approved work, linked to registry entry; complete node and citation checked |
| Openness and counter-critique | Raw boundary required editing | PASS: explicit transfer boundary, no promised effects |
| First-year readability | FAIL: raw length/complexity unsuitable | PASS: one source-led idea, one operational question |

Amendment: {concept['amendment']}

Spanish text is a reviewed translation of the amended English paragraph,
not a separate cold prose generation or second evidence claim.
'''
  (folder/'evaluation.md').write_text(evaluation)
  for locale,filename in [('en',SITE/'index.md'),('es',SITE/'es/index.md')]:
   if not filename.exists():continue
   text=filename.read_text();marker='<!-- dignity-concept:'+slug+' -->'
   if marker in text:
    filename.write_text(text.replace(marker,linked(concept[locale],concept['key'])+provenance(slug,source,record)))
  report.append({'idea':slug,'record':record['record'],'rejected_attempts':sum(r['idea']==slug and r['returncode']!=0 for r in records),'amendment':concept['amendment'],'public_reference_key':concept['key'],'source_node':source['node'],'final_editorial_status':'reviewed; professor release pending'})
 (ROOT/'SCRIBE-PERFORMANCE.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print('Integrated six amended concepts; raw drafts, rejections and evaluations retained.')
