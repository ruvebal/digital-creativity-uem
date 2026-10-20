"""One grounded paragraph per lesson-scribe call, with all gates retained."""
from pathlib import Path
import datetime,json,subprocess,uuid,re
ROOT=Path(__file__).resolve().parent
MEMORY=Path('/Users/ruvebal/src/deviac/fine-tuning/thessia-tuning-memory')
PYTHON='/Users/ruvebal/src/ahmes/.venv/bin/python'
WRAPPER='/Users/ruvebal/src/deviac/fine-tuning/scripts/thessia_generate.py'
IDEAS=[
 ('worth','Equal worth, different lives','udhr-articles-1948',None,'(United Nations 1948)',
  'Distinguish inherent worth from status, beauty, productivity or buying power. Article 1 establishes equal dignity and rights; article 2 names differences without withdrawing equal entitlement. Course application: in an image critique, assess the editorial decision, never rank a person. Use the actual declaration as your example. Do not claim this declaration automatically settles a legal advertising case.'),
 ('agency','An image distributes agency','srivastava-2022','3d9ac8ed-446c-5ca1-bb19-880639ae0f25','(Srivastava et al. 2022)',
  'A visual discourse study examined 15 Nordic fast-fashion advertisements and found complex portrayals that need not dislodge stereotypes. Ask who acts, who looks and who is reduced to a role. Use that study as your concrete example; do not name its sampled brands or reproduce images of minors. Formal cues support an interpretation; they do not diagnose a model or measure audience effects.'),
 ('difference','Shared dignity does not erase history','browne-commodity','57e89038-7393-552d-981f-432dce0ebe7c','(Browne 2015)',
  'Browne analyses commodity spectacle and histories of racialisation. Apply this as a question about the histories carried by a visual trope, not as proof that every present fashion image repeats one colonial mechanism. Equality of worth does not make people interchangeable or make audiences culturally identical. Your concrete example is Browne’s historical analysis of commodity spectacle, without adding details absent from the source.'),
 ('labour','The person outside the frame','gd-textile',None,'(Global Dignity España and Fundación AYO 2026)',
  'The supplied 2026 practice bank case GD16 asks teams acting as a textile company to decide production location, fair labour conditions, materials and communication. Its named author is Belén María Moreno Cabezalí. Use this actual documented practice as your example, without naming its institution. It connects communication to production decisions. A respectful poster cannot by itself establish fair labour conditions, and the case is a teacher report, not an effectiveness study.'),
 ('consumption','A viewer can also be a citizen','unep-consumption','898f3365-fd0d-5720-942c-4ac95c014cd7','(United Nations Environment Programme 2023)',
  'The Sustainable Fashion Communication Playbook recommends countering greenwashing, reducing messages of overconsumption and supporting citizens’ demands for wider change. Name the Playbook as your concrete example. Course question: can an image or call to action make room for repair, reuse, reflection or collective action without measuring success only by purchases? This is normative practitioner guidance, not evidence of measured classroom or campaign outcomes. Do not portray consumers as irrational or morally deficient.'),
 ('dialogue','A critique must be answerable','freire-dialogue','a381d3a9-43e9-511e-a0f7-37431665bd6b','(Freire 2000)',
  'Freire describes problem-posing education in which teacher and students investigate a shared object rather than receive deposited answers. Use this described pedagogical relation as the real example. In the proposed campaign critique the shared object is a documented editorial decision; students must be able to challenge the teacher’s reading. Do not claim these activities have measured benefits. Do not demand personal testimony or moral agreement; those are explicit course design choices.'),
]
if __name__=='__main__':
 evidence=json.loads((ROOT/'evidence-nodes.json').read_text())
 records=json.loads((ROOT/'scribe-records.json').read_text()) if (ROOT/'scribe-records.json').exists() else []
 for slug,title,key,node,citation,thesis in IDEAS:
  if any(r['idea']==slug and r['returncode']==0 for r in records): continue
  candidates=[r for r in evidence if r['key']==key and (node is None or r['node']==node)]
  row=candidates[0];assert 'evaluator_safe=yes' in row['resolver'],key
  record=MEMORY/('2026-10-20-'+str(uuid.uuid4())+'-dc-dignity-'+slug)
  record.mkdir(parents=True)
  excerpt=row['content']
  if key=='udhr-articles-1948':
   start=excerpt.find('All human beings are born'); excerpt=excerpt[max(0,start-30):start+900]
  excerpt=excerpt[:1800]
  brief=f'''# Dignity — {title}

## THESIS
{thesis}

## GROUNDED PATH
1. {citation}. Ahmes: {row['db']}:{row['node']}
Verified relevant excerpt (complete source node retained in provenance.json):
{excerpt}
Resolver:
{row['resolver']}
Boundary: {row['does_not_support']}

## ATHANOR FINDINGS
Scope: scholar-dignity; profield-digital-creativity; profield-nuevos-medios-moda-2026-27; cross-project DevIAC discovery.
The exact queries, project scopes and matches are in the dignity/vault-search research pack.
Cross-project matches reached scholar-alchemy (Freire), scholar-ai-criticism (Browne), and media labour research (Abidin).
These are discovery pointers, never evidence. Undated supplied documents remain bibliography gaps.

## PUBLIC CITATION PERMITTED
{citation}
No direct quotations permitted in this paragraph. No other author or year may be added.
'''
  prompt=f'''You are the author of a student guide on dignity and fashion communication, under Rubén Vega Balbás’s editorial control. Write in clear English for first-year university students.
Write exactly ONE paragraph with four sentences, marked [S1], [S2], [S3], [S4]. Maximum 115 words. Return only the paragraph.
S1: a concrete observation stating the main idea. S2: explain it through the actual source example in the brief, and include exactly {citation}. S3: an open question students can investigate. S4: a boundary or counterargument that leaves the claim open to challenge.
Use plain words. No direct quotations, quoted slogans, invented examples, new sources, broad causal claims or institutional names. Do not name your writing techniques or research tools. Do not mention antilism. Distinguish source findings from the course application. Do not promise learning effects.

{brief}

FINAL OUTPUT RULE: Output exactly four sentences in this literal order: [S1] statement. [S2] source example with {citation}. [S3] one question? [S4] boundary statement. No quotation marks. No author abbreviations. No additional question. No headings. All four markers are required.'''
  (record/'BRIEF.md').write_text(brief);(record/'prompt.md').write_text(prompt)
  (record/'verbatims.json').write_text(json.dumps([{'citation':citation,'db_path':row['db'],'node_id':row['node'],'verbatims':[row['content']]}],ensure_ascii=False))
  (record/'provenance.json').write_text(json.dumps({'course':'DC image + NM media','guide':'/dignity/','idea':slug,'evidence':row,'harness':'lesson-scribe v0.1 / prompt-v2.1','independent_human_review':False},ensure_ascii=False,indent=2))
  attempt=sum(r['idea']==slug for r in records)
  prompt+='\nBegin with the literal marker [S1]. Include [S2], [S3], [S4] exactly once each. This is a required output schema, not prose decoration.\n'
  (record/'prompt.md').write_text(prompt)
  args=[PYTHON,WRAPPER,'--prompt',prompt,'--out',str(record/'thessia-raw.md'),'--brief',str(record/'BRIEF.md'),'--model','thessia-scholar-v3','--num-predict','512','--temperature','0.1','--seed',str(42+attempt),'--verbatim-registry',str(record/'verbatims.json'),'--expected-sentences','4']
  with (record/'generation.log').open('w') as log:
   rc=subprocess.run(args,stdout=log,stderr=subprocess.STDOUT,timeout=1000).returncode
  if rc==0 and citation not in re.sub(r',(?= \d{4})','',(record/'thessia-raw.md').read_text()):
   (record/'editorial-citation-rejection.txt').write_text('Required citation form missing or changed; generation is not approved for integration.')
   rc=2
  records.append({'idea':slug,'title':title,'record':str(record),'returncode':rc,'citation':citation})
  (ROOT/'scribe-records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
  print(slug,rc,flush=True)
  # Unload only this script's completed generation before the next guarded call.
  subprocess.run(['ollama','stop','thessia-scholar-v3'],capture_output=True)
