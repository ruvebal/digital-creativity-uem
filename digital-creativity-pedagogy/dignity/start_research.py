"""Launch two auditable Profield research strands; public keywords only."""
from pathlib import Path
import concurrent.futures
import datetime
import json
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
PROFIELD = Path('/Users/ruvebal/src/profield')
BIN = str(PROFIELD / '.venv/bin/profield')

FIELDS = {
    'ideas': ['human dignity fashion advertising objectification recognition agency',
              'critical visual literacy fashion education ethics representation',
              'gender stereotypes advertising consumer dignity racial discrimination',
              'dignity labour fashion supply chains responsible communication'],
    'images': ['fashion advertising dignity objectification regulatory rulings',
               'fashion image racial stereotypes sexualisation body image retouching',
               'critical fashion campaign visual analysis agency framing gaze',
               'fashion film advertising stereotypes counter advertising redesign'],
}

def command(args, out):
    with out.open('w') as stream:
        result = subprocess.run(args, cwd=PROFIELD, stdout=stream,
                                stderr=subprocess.STDOUT, timeout=600)
    return result.returncode

def worker(strand):
    run = ROOT / 'profield' / strand
    run.mkdir(parents=True, exist_ok=True)
    field = run / 'field.yaml'
    field.write_text('id: dignity-fashion-' + strand + '\n'
        + 'title: Dignity and fashion ' + strand + '\nkeywords:\n'
        + ''.join('  - ' + q + '\n' for q in FIELDS[strand])
        + 'areas: [dignity, fashion-communication, critical-literacy]\n'
        + 'confidentiality: public-keywords-only\n'
        + 'themes: [agency, representation, gender, race, labour, pedagogy]\n')
    receipts = []
    rc = command([BIN, 'prompt', 'pass1', str(field), '-o',
                  str(run / 'pass1.prompt.md')], run / 'prompt.log')
    receipts.append({'operation': 'profield prompt pass1', 'returncode': rc})
    if strand == 'ideas':
        for i, query in enumerate(FIELDS[strand], 1):
            url = 'https://api.crossref.org/works?' + urllib.parse.urlencode({
                'query': query, 'rows': 10, 'select': 'DOI,title,author,published,URL,type,link'})
            try:
                request = urllib.request.Request(url, headers={'User-Agent':
                    'DignityCurriculumResearch/1.0 (public bibliography discovery)'})
                with urllib.request.urlopen(request, timeout=50) as response:
                    data = json.load(response)
                (run / f'registry-{i:02}.json').write_text(json.dumps(data,
                    ensure_ascii=False, indent=2))
                receipts.append({'query': query, 'url': url, 'status': 'retrieved',
                    'count': len(data['message']['items']), 'evidence_status': 'discovery only'})
            except Exception as exc:
                receipts.append({'query': query, 'url': url, 'error': str(exc)})
    else:
        for i, query in enumerate([
                'fashion advertising women objectification',
                'fashion diversity representation portrait',
                'garment workers fashion advertising'], 1):
            args = [BIN, 'media-prospect', '--course', 'CD I', '--unit', 'I.1',
                '--field', 'fashion image', '--subfield',
                'image practices, circulation, editorial/commercial boundary',
                '--media-type', 'image', '--providers', 'wikimedia,internet_archive',
                '--search-text', query, '--max-results', '8', '--no-llm',
                '--runs-root', str(run), '--run-id', f'dignity-{i:02}']
            rc = command(args, run / f'media-{i:02}.log')
            receipts.append({'query': query, 'returncode': rc,
                             'evidence_status': 'unaccepted discovery; rights not cleared'})
    (run / 'subprocess-receipt.json').write_text(json.dumps({
        'strand': strand, 'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'receipts': receipts, 'independent_review': False}, ensure_ascii=False, indent=2))
    return strand

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for strand in pool.map(worker, ['ideas', 'images']):
            print(strand + ': research discovery subprocess complete', flush=True)
