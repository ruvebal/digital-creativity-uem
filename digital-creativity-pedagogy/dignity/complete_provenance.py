"""Attach exact discovery traces, source checks and explicit dated-source gaps."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent
SITE=ROOT.parents[1]/'docs/dignity'
DISCOVERY={
 'worth':('scholar-dignity','Open https://www.un.org/en/about-us/universal-declaration-of-human-rights',None),
 'agency':('profield-digital-creativity; profield-nuevos-medios-moda-2026-27','human dignity critical thinking ethics recognition objectification fashion advertising',0.7173228641884438),
 'difference':('scholar-ai-criticism','colonial gaze racial stereotypes fashion advertising cultural appropriation',0.6374314044097729),
 'labour':('scholar-dignity','dignidad industria textil condiciones laborales comunicar valores',0.7915298781938527),
 'consumption':('profield-nuevos-medios-moda-2026-27','fashion garment workers dignity living wages consumer responsibility',0.6956417080902246),
 'dialogue':('scholar-alchemy','critical thinking dialogue problem posing education Freire hooks',0.7015954063930968),
}
CLAIMS=[
 ('visibility','abidin-visibility','abidin-2016','(Abidin 2016)','Gendered visibility labour in the particular Instagram study; present prevalence and individual motives are not inferred.'),
 ('spanish-law','spain-advertising-1988','espana-1988','(España 1988, art. 3(a))','Article 3(a), consolidated information page last updated 2023-03-01, consulted 2026-10-20; not a case-specific legal opinion.'),
 ('boohoo','asa-boohoo-2022','asa-boohoo-2022','(Advertising Standards Authority 2022)','Specific UK ASA execution finding; full primary ruling read through web tools, local snapshot is a short exact excerpt.'),
 ('gucci','asa-gucci-2016','asa-gucci-2016','(Advertising Standards Authority 2016)','Specific UK ASA presentation finding; no diagnosis; related official video is not authenticated as the adjudicated version.'),
 ('hm','acm-hm-2022','acm-2022','(Netherlands Authority for Consumers and Markets 2022)','Dutch 2022 commitments, not criminal conviction, fine or comprehensive judgement about products/workers.'),
 ('dg','pantano-2021','pantano-2021','(Pantano 2021)','Primary study of a particular negative-stereotype campaign controversy, not a regulatory finding or representative population survey.'),
 ('calvin-klein','asa-calvin-klein-2024','asa-calvin-klein-2024','(Advertising Standards Authority 2024)','Full revised ruling read online: objectification reversed, untargeted placement objection retained. Local exact excerpt documents agency; full ruling is linked and version dated.'),
 ('gd-adaptation','gd-textile','global-dignity-2026','(Global Dignity España and Fundación AYO 2026)','Adaptation of reported practice GD16; no educational efficacy, labour impact or institutional endorsement inferred.'),
]
def block(data):
 return '\n{% if site.publication.publish_internal_metadata %}\n<!-- curriculum-internal:\nPROVENANCE_LINE: '+json.dumps(data,ensure_ascii=False)+'\n-->\n{% endif %}\n'

if __name__=='__main__':
 evidence=json.loads((ROOT/'evidence-nodes.json').read_text())
 sources={d['id']:d for d in json.loads((ROOT/'primary-sources.json').read_text())}
 for page in [SITE/'index.md',SITE/'es/index.md']:
  text=page.read_text()
  def exact(match):
   data=json.loads(match.group(1));slug=data['claim'].replace('DIGNITY.','')
   if slug in DISCOVERY:
    project,query,similarity=DISCOVERY[slug]
    data['discovery'].update(project_slug=project,query=query,similarity=similarity)
    data['discovery']['proposed_use']='Discovery located the work; the exact cited node was then read independently. The similarity is a discovery score, not evidence of support.'
   return 'PROVENANCE_LINE: '+json.dumps(data,ensure_ascii=False)
  text=re.sub(r'^PROVENANCE_LINE: (\{.*\})$',exact,text,flags=re.M)
  for slug,key,ref,citation,boundary in CLAIMS:
   if '"claim": "DIGNITY.case.'+slug+'"' in text:continue
   row=next(r for r in evidence if r['key']==key and 'evaluator_safe=yes' in r['resolver'])
   url=sources.get(key,{}).get('url')
   if key=='abidin-visibility':query='gender stereotypes objectification advertising social media fashion';project='profield-nuevos-medios-moda-2026-27'
   elif key=='gd-textile':query=DISCOVERY['labour'][1];project='scholar-dignity'
   else:query='Open '+str(url);project='scholar-dignity'
   data={'claim':'DIGNITY.case.'+slug,'status':'VERIFIED','discovery':{'service':'Athanor / primary-source reading','project_slug':project,'knowledge_scope':'field_prospection','query':query,'source_locator':row['db']+':'+row['node'],'similarity':None,'proposed_use':boundary},'source':{'document_coat':Path(row['db']).parents[1].name,'extraction_db':row['db'],'node_id':row['node'],'page_index':row['page_index'],'printed_page':None,'page_basis':row['page_basis']},'resolver':row['resolver'],'quote':'none','public_citation':citation,'supports':boundary,'does_not_support':row['does_not_support']}
   marker='['+citation+'](#ref-'+ref+')'
   assert marker in text,(page,marker)
   # For GD the first occurrence is in the B1 paragraph; target the final adaptation citation.
   index=text.rfind(marker) if slug=='gd-adaptation' else text.find(marker)
   end=index+len(marker);text=text[:end]+block(data)+text[end:]
  if 'dignity-cascade-manifest:' not in text:
   gaps=[];seen=set()
   for row in evidence:
    if row['key'].startswith('corpus-') and 'evaluator_safe=yes' not in row['resolver'] and row['key'] not in seen:
     seen.add(row['key']);gaps.append({'status':'[BIBLIO-GAP]','db':row['db'],'node':row['node'],'page_index':row['page_index'],'resolver':row['resolver'],'reason':'No verified publication year; source read and indexed, no date invented','public_citation':'OMITTED'})
   meta='\n{% if site.publication.publish_internal_metadata %}\n<!-- curriculum-internal:\ndignity-cascade-manifest:\nforge_date: 2026-10-20\nvault_refs_n: 13\nharness: lesson-scribe v0.1 · prompt-v2.1\nreview: Codex editorial review; professor release pending\nundated_source_gaps: '+json.dumps(gaps,ensure_ascii=False)+'\n-->\n{% endif %}\n'
   end=text.find('\n---',4)+4;text=text[:end]+meta+text[end:]
  assert 'dignity-concept:' not in text
  page.write_text(text)
 print('Attached exact discovery traces, case provenance and four undated-source gaps to both guide locales.')
