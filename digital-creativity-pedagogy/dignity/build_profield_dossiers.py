"""Archive source-grounded maps, explicit same-agent audits and tool checks."""
from pathlib import Path
import json,subprocess,re
ROOT=Path(__file__).resolve().parent
ENGINE=Path('/Users/ruvebal/src/profield')
CLI=str(ENGINE/'.venv/bin/profield')
CLAIMS={
'ideas':[
 ('Normative framework','I01','ESTABLISHED','The Universal Declaration grounds equal dignity and rights independently of distinctions named in Article 2. This is a normative framework, not a campaign-effect estimate.','United Nations. 1948. Universal Declaration of Human Rights, arts. 1–2. https://www.un.org/en/about-us/universal-declaration-of-human-rights','confirmed'),
 ('Normative framework','I02','ESTABLISHED','Spain’s General Advertising Law Article 3(a) explicitly addresses advertising that attacks dignity; its consolidated text was checked on 2026-10-20, last update shown 2023-03-01. Application to a case requires jurisdictional and factual analysis.','España. 1988. Ley 34/1988, General de Publicidad, art. 3(a). https://www.boe.es/buscar/act.php?id=BOE-A-1988-26156#a3','confirmed'),
 ('Visual agency','I03','EMERGING','A visual discourse analysis of 15 Nordic fast-fashion advertisements identifies complex portrayals that need not dislodge stereotypes. This bounded sample is not an industry-wide prevalence measure.','Srivastava, Sonali, Terhi-Anna Wilska, and Johanna Sjöberg. 2022. Girls’ portrayals in fast fashion advertisements. Consumption Markets & Culture 25(6):501–524. https://doi.org/10.1080/10253866.2022.2067149','confirmed'),
 ('Visual agency','I04','ESTABLISHED','Browne’s historical discussion of commodity spectacle connects visual consumption to racialisation. Its transfer to a contemporary advertisement is a situated interpretive question.','Browne, Simone. 2015. Dark Matters: On the Surveillance of Blackness. Duke University Press. https://doi.org/10.1215/9780822375302','confirmed'),
 ('Political economy and media','I05','EMERGING','Abidin’s study describes under-compensated and underacknowledged gendered visibility labour in follower-anchored Instagram fashion advertorials. It does not measure current platform prevalence.','Abidin, Crystal. 2016. Visibility labour: Engaging with Influencers’ fashion brands and #OOTD advertorial campaigns on Instagram. Media International Australia 161(1):86–100. https://doi.org/10.1177/1329878X16665177','confirmed'),
 ('Political economy and media','I06','ESTABLISHED','UNEP’s Playbook recommends reducing messages of overconsumption and supporting citizens’ demands for wider change. This is practitioner guidance, not measured campaign impact.','United Nations Environment Programme. 2023. The Sustainable Fashion Communication Playbook. https://www.unep.org/resources/publication/sustainable-fashion-communication-playbook','confirmed'),
 ('Political economy and media','I07','EMERGING','Pantano models online diffusion around a particular luxury campaign using negative stereotypes. The issue year is 2021, with online-first publication in 2020; the event does not provide a universal causal law.','Pantano, Eleonora. 2021. When a luxury brand bursts: Modelling the social media viral effects of negative stereotypes adoption leading to brand hate. Journal of Business Research 123:117–125. https://doi.org/10.1016/j.jbusres.2020.09.049','confirmed'),
 ('Teaching inquiry','I08','ESTABLISHED','The supplied 2026 practice bank case GD16 connects textile production location, fair working conditions, materials and communication. This is a documented practice, not an effectiveness study.','Global Dignity España and Fundación AYO. 2026. Dignidad e innovación educativa: Banco de buenas prácticas, GD16, PDF p.17. Local supplied source; no public edition URL verified.','confirmed'),
 ('Teaching inquiry','I09','ESTABLISHED','Freire’s problem-posing relation treats teacher and learners as investigators of a shared object. Our fashion tasks are a pedagogical adaptation, not an intervention validated by that text.','Freire, Paulo. 2000. Pedagogy of the Oppressed. 30th anniversary edition. Continuum. ISBN 9781501305313. Supplied vault edition verified on title and copyright pages.','confirmed'),
 ('Unresolved claims','I10','UNVERIFIED','Removing identity labels from a campaign guarantees equal recognition and eliminates discrimination. No verified source establishes this guarantee.','No verifiable source found; presented as a rejected proposition, not a finding.','disputed'),
 ('Unresolved claims','I11','UNVERIFIED','These proposed classroom activities improve wellbeing or reduce discriminatory behaviour. No classroom evaluation was performed.','No verifiable outcome study for these activities.','unverifiable'),
 ('Unresolved claims','I12','UNVERIFIED','All five supplied PDFs have complete evaluator-safe author-year metadata. Four do not have a verified publication year.','bibliography audit and source-page inspection, 2026-10-20.','disputed'),
],
'images':[
 ('Documented execution decisions','V01','ESTABLISHED','The ASA upheld an objection to Boohoo’s particular T-shirt product images on objectification and sexualisation grounds on 16 February 2022. The execution was seen in November 2021.','Advertising Standards Authority. 2022. ASA Ruling on Boohoo.com UK Ltd. https://www.asa.org.uk/rulings/boohoo-com-uk-ltd-a21-1136109-boohoo-com-uk-ltd.html','confirmed'),
 ('Documented execution decisions','V02','ESTABLISHED','The 6 April 2016 Gucci ruling distinguished two images and found one irresponsible in its presentation of thinness. It does not diagnose the model’s health.','Advertising Standards Authority. 2016. ASA Ruling on Guccio Gucci SpA. https://www.asa.org.uk/rulings/guccio-gucci-spa-a15-321743.html','confirmed'),
 ('Documented execution decisions','V03','ESTABLISHED','The revised 6 March 2024 Calvin Klein ruling reversed the objectification finding about FKA twigs while maintaining the objection to untargeted placement.','Advertising Standards Authority. 2024. ASA Ruling on Calvin Klein Inc, revised. https://www.asa.org.uk/rulings/calvin-klein-inc-g23-1194611-calvin-klein-inc-1.html','confirmed'),
 ('Claims, narrative and circulation','V04','ESTABLISHED','ACM secured commitments from H&M and Decathlon in 2022 to adjust or stop insufficiently clear sustainability claims. Commitments must not be described as fines or criminal convictions.','Netherlands Authority for Consumers and Markets. 2022. Going forward, Decathlon and H&M will provide better information about sustainability to consumers. https://www.acm.nl/en/publications/going-forward-decathlon-and-handm-will-provide-better-information-about-sustainability-consumers','confirmed'),
 ('Claims, narrative and circulation','V05','EMERGING','Pantano’s study examines the Dolce & Gabbana chopsticks controversy through negative stereotype adoption and online diffusion. It supports a situated narrative and circulation analysis, not an adjudicated universal racial-discrimination finding.','Pantano, Eleonora. 2021. When a luxury brand bursts. Journal of Business Research 123:117–125. https://doi.org/10.1016/j.jbusres.2020.09.049','confirmed'),
 ('Media evidence and access','V06','ESTABLISHED','The verified GUCCI channel has an official short edit of the Cruise 2016 campaign, dated 16 September 2015. It is related media, not authenticated evidence of the exact adjudicated end-frame.','GUCCI. 2015. The Cruise 2016 Campaign — A Short Edit. https://www.youtube.com/watch?v=EvcdVVHta1U','confirmed'),
 ('Media evidence and access','V07','UNVERIFIED','A surviving campaign video necessarily preserves the exact version seen by a regulator. No version identity was established.','No verified end-frame/version correspondence; do not fabricate timecodes.','disputed'),
 ('Media evidence and access','V08','UNVERIFIED','Metadata availability or public access clears campaign image rights for republication or remix. No rights clearance was obtained.','Source access is not a licence. Provider candidates remain unaccepted.','disputed'),
 ('Research method','V09','EMERGING','A small visual discourse study offers a method for reading composition, action and portrayal together, without making visible variety a proxy for equality.','Srivastava, Sonali, Terhi-Anna Wilska, and Johanna Sjöberg. 2022. Girls’ portrayals in fast fashion advertisements. https://doi.org/10.1080/10253866.2022.2067149','confirmed'),
 ('Research method','V10','UNVERIFIED','The broad media-provider search produced a ready-to-publish collection of relevant campaign images. Its noisy archival candidates were not accepted.','Media discovery manifests and provider audit logs, 2026-10-20.','disputed'),
]}

if __name__=='__main__':
 for strand,claims in CLAIMS.items():
  strand_root=ROOT/'profield'/strand;field=strand_root/'field.yaml'
  run=strand_root/('dignity-fashion-'+strand)/'20261020'
  run.mkdir(parents=True,exist_ok=True)
  head='# Research provenance\n\nCodex map, same-agent adversarial audit and tool/source verification. No independent external model or human peer review is claimed. Public keywords only. Tags describe documentary confidence within this bounded dossier; case studies are not field-wide consensus.\n\n'
  text=head;area=None
  for section,key,tag,claim,citation,verdict in claims:
   if area!=section: text+='## '+section+'\n\n';area=section
   url=re.search(r'https?://\S+',citation)
   formatted=f'[{citation[:url.start()].strip()}]({url.group(0)})' if url else citation
   text+=f'- [{tag}] {key}: {claim} Source: {formatted}\n\n'
  (run/'pass1.raw.md').write_text(text)
  audit=head+'## Adversarial audit\n\n'
  tools=head+'## Tool and full-source verification\n\n'
  for section,key,tag,claim,citation,verdict in claims:
   audit+=f'- {verdict}: {key}: {claim} Boundary retained. Source audit: {citation}\n\n'
   tools+=f'- {verdict}: {key}: {claim} Checked against primary source / local full-node evidence / acquisition receipt as applicable. {citation}\n\n'
  (run/'pass2.raw.md').write_text(audit);(run/'pass3.notes.md').write_text(tools)
  commands=[]
  for passno,filename,surface in [('pass1','pass1.raw.md','codex-source-grounded-map'),('pass2','pass2.raw.md','codex-same-agent-adversarial-audit'),('pass3','pass3.notes.md','codex-primary-tool-verification')]:
   if passno!='pass1':
    args=[CLI,'prompt',passno,str(field),'-o',str(run/(passno+'.prompt.md'))]
    if passno=='pass2':args+=['--prior',str(run/'pass1.raw.md')]
    if passno=='pass3':args+=['--run',str(run)]
    commands.append(args)
   commands.append([CLI,'ingest',passno,str(field),'--from',str(run/filename),'--surface',surface,'--run',str(run)])
  commands += [[CLI,'digest',str(field),'--run',str(run)], [CLI,'lexicum',str(field),'--run',str(run)]]
  with (run/'engine.log').open('w') as log:
   for args in commands:
    result=subprocess.run(args,cwd=ENGINE,stdout=log,stderr=subprocess.STDOUT)
    if result.returncode: raise RuntimeError('Profield command failed: '+str(args))
  (run/'RESEARCH-STATUS.md').write_text(f'''# {strand.title()} investigation

Completed: public-keyword prompt; subprocess discovery; source-grounded map;
same-agent adversarial audit; primary-source/tool verification; native Profield
ingestion, digest and lexicum. Claim entries: {len(claims)}.

No independent second model/reviewer, systematic-review completeness or media
rights clearance is claimed. Some raw scholarly retrieval candidates are not
retained. See ../../../../RESEARCH-SYNTHESIS.md and ../../../../evidence-nodes.json for
the evidence boundaries. The engine's parser/digest counts are technical
outputs; inspect unmatched verdicts before treating its status as a review.
''')
  print(strand,'native Profield dossier complete',flush=True)
