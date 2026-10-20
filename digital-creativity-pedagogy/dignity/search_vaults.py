"""Read-only scoped and cross-project neural discovery; persist every scope."""
from pathlib import Path
import concurrent.futures
import json
import subprocess
ROOT=Path(__file__).resolve().parent
CROSS='/Users/ruvebal/src/.cursor/skills/grounding-graph/scripts/cross_project_neural_search.py'
ATH='/Users/ruvebal/src/athanor/.venv/bin/athanor'
QUERIES=[
 ('recognition','dignity recognition difference humiliation instrumentalization ethics'),
 ('critical-thinking','critical thinking dialogue problem posing education Freire hooks'),
 ('objectification','objectification agency autonomy denial subjectivity women advertising Nussbaum'),
 ('decolonial','colonial gaze racial stereotypes fashion advertising cultural appropriation'),
 ('labour','fashion garment workers dignity living wages consumer responsibility'),
 ('media','influencer advertising autonomy manipulation overconsumption fashion body image'),
]
SCOPED=[
 ('profield-digital-creativity','fashion image retouching ethics body agency authorship'),
 ('profield-nuevos-medios-moda-2026-27','gender stereotypes objectification advertising social media fashion'),
 ('profield-creativity-techniques','critical thinking dignity education ethics dialogue'),
 ('profield-stem-code-ai-epistemology-critique','critical pedagogy power agency ethics'),
 ('scholar-ai-criticism','human agency dignity recognition bias critique'),
]
def run(item):
 slug,query,argv=item
 result=subprocess.run(argv,capture_output=True,text=True,timeout=180)
 (ROOT/'vault-search'/f'{slug}.json').write_text(result.stdout)
 if result.stderr: (ROOT/'vault-search'/f'{slug}.stderr.txt').write_text(result.stderr)
 return {'id':slug,'query':query,'returncode':result.returncode,'command':argv,
         'role':'discovery only; resolve pages and citation before use'}
if __name__=='__main__':
 (ROOT/'vault-search').mkdir(exist_ok=True)
 tasks=[('cross-'+name,q,['python3',CROSS,q,'--top','15','--json']) for name,q in QUERIES]
 tasks += [(slug,q,[ATH,'search',q,'--project-slug',slug,'--library','scholar','--top-k','6']) for slug,q in SCOPED]
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  receipts=list(pool.map(run,tasks))
 (ROOT/'vault-search'/'receipts.json').write_text(json.dumps(receipts,indent=2))
 print(json.dumps([{'id':r['id'],'returncode':r['returncode']} for r in receipts]))
