"""Retrieve public primary documents; never download campaign media binaries."""
from pathlib import Path
import datetime, hashlib, json, urllib.request
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
DOCS=[
 {'id':'asa-boohoo-2022','url':'https://www.asa.org.uk/rulings/boohoo-com-uk-ltd-a21-1136109-boohoo-com-uk-ltd.html','title':'ASA Ruling on Boohoo.com UK Ltd','organization':'Advertising Standards Authority','year':2022,'start':'ASA Ruling on Boohoo.com UK Ltd','end':'More on'},
 {'id':'asa-gucci-2016','url':'https://www.asa.org.uk/rulings/guccio-gucci-spa-a15-321743.html','title':'ASA Ruling on Guccio Gucci SpA','organization':'Advertising Standards Authority','year':2016,'start':'ASA Ruling on Guccio Gucci SpA','end':'More on'},
 {'id':'asa-calvin-klein-2024','url':'https://www.asa.org.uk/rulings/calvin-klein-inc-g23-1194611-calvin-klein-inc-1.html','title':'ASA Ruling on Calvin Klein Inc (revised 6 March 2024)','organization':'Advertising Standards Authority','year':2024,'start':'ASA Ruling on Calvin Klein Inc','end':'CAP Code (Edition 12)'},
 {'id':'acm-hm-2022','url':'https://www.acm.nl/en/publications/going-forward-decathlon-and-handm-will-provide-better-information-about-sustainability-consumers','title':'Going forward, Decathlon and H&M will provide better information about sustainability to consumers','organization':'Netherlands Authority for Consumers and Markets','year':2022,'start':'Going forward, Decathlon','end':'See also:'},
 {'id':'udhr-1948','url':'https://www.un.org/en/about-us/universal-declaration-of-human-rights','title':'Universal Declaration of Human Rights','organization':'United Nations','year':1948,'start':'Preamble','end':None},
 {'id':'pantano-2021','url':'https://research-information.bris.ac.uk/files/250098384/burst_paper_accepted_.pdf','title':'When a luxury brand bursts: Modelling the social media viral effects of negative stereotypes adoption leading to brand hate','authors':[{'kind':'person','given':'Eleonora','family':'Pantano'}],'year':2021,'doi':'10.1016/j.jbusres.2020.09.049','format':'pdf'},
 {'id':'srivastava-2022','url':'https://liu.diva-portal.org/smash/get/diva2%3A1657350/FULLTEXT01.pdf','title':'Girls’ portrayals in fast fashion advertisements','authors':[{'kind':'person','given':'Sonali','family':'Srivastava'},{'kind':'person','given':'Terhi-Anna','family':'Wilska'},{'kind':'person','given':'Johanna','family':'Sjöberg'}],'year':2022,'doi':'10.1080/10253866.2022.2067149','format':'pdf'},
]
if __name__=='__main__':
 snapshots=ROOT/'source-snapshots'; snapshots.mkdir(exist_ok=True)
 for doc in DOCS:
  try:
   request=urllib.request.Request(doc['url'],headers={'User-Agent':'Mozilla/5.0 (academic source verification)'})
   with urllib.request.urlopen(request,timeout=90) as response:
    raw=response.read(); doc['final_url']=response.url; doc['content_type']=response.headers.get('Content-Type')
   doc['sha256']=hashlib.sha256(raw).hexdigest()
   if doc.get('format')=='pdf':
    assert raw.startswith(b'%PDF'), 'Response is not PDF'
    dest=snapshots/(doc['id']+'.pdf'); dest.write_bytes(raw)
   else:
    soup=BeautifulSoup(raw,'html.parser')
    for tag in soup(['script','style','nav','footer','header']): tag.decompose()
    main=soup.find('main') or soup
    text=main.get_text('\n',strip=True)
    start=text.find(doc['start']); assert start>=0, 'Article start missing'
    text=text[start:]
    if doc['end'] and doc['end'] in text: text=text[:text.index(doc['end'])]
    dest=snapshots/(doc['id']+'.md')
    dest.write_text('# '+doc['title']+'\n\nSource: '+doc['url']+'\n\n'+text+'\n')
   doc['snapshot']=str(dest); doc['status']='retrieved'
  except Exception as exc: doc['status']='unavailable';doc['error']=str(exc)
  doc['retrieved_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
  print(doc['id'],doc['status'],flush=True)
 (ROOT/'primary-sources.json').write_text(json.dumps(DOCS,ensure_ascii=False,indent=2))
