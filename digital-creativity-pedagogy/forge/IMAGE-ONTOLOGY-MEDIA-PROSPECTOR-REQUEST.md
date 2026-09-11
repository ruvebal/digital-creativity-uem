# Media Prospector request — I.0 image ontology

Target repository: `/Users/ruvebal/src/profield`

Prepare a reviewed media collection for the I.0 image-ontology masterclass.
Search these fields and subfields:

```text
field: image ontology and photographic truth
subfield: Joan Fontcuberta, post-photography, analog photography, digital capture,
digitised photographs, non-AI machine-generated images, procedural generative art,
data visualisation, AI/model-generated images, hybrid images
```

Search only approved providers and preserve canonical source pages, creator,
date, asset ID, preview URL, rights evidence, credit line, accessibility data,
and retrieval date. Use Wikimedia Commons, Internet Archive, and Library of
Congress first. Search museum or institutional collections only when their
rights statement is explicit.

Suggested command for an image pack:

```bash
.venv/bin/profield media-prospect \
  --course "CD I" \
  --unit I.0 \
  --field "image ontology and photographic truth" \
  --subfield "Joan Fontcuberta, post-photography, analog photography, digital capture, digitised photographs, non-AI machine-generated images, procedural generative art, data visualisation, AI/model-generated images, hybrid images" \
  --media-type image \
  --providers wikimedia,internet_archive,loc \
  --max-results 40 \
  --no-llm
```

Classify every accepted candidate with:

```text
production_ontology: analog_human_made | analog_photographic | digital_capture |
  digitised_analog | digital_native | non_ai_machine_generated | generative_art |
  data_generated_or_visualised | ai_or_model_generated | hybrid
image_function: trace_or_testimony | representation_or_reproduction |
  diagram_or_explanation | measurement_or_data_argument | fiction_or_simulation |
  expression_or_composition | advertising_or_persuasion | evidence_or_document |
  hybrid_claim
```

Do not infer that an image is AI-generated from appearance. Require creator or
source documentation. Do not infer Fontcuberta authorship, date, or licence;
verify it from the canonical collection record.

Review, rank, reject, assign the collection `image-ontology-i0`, then export an
MP5-ready handoff keyed by media slots such as:

```text
I.0.ontology.analog-photographic
I.0.ontology.digitised-analog
I.0.ontology.non-ai-machine-generated
I.0.ontology.generative-art
I.0.ontology.data-visualisation
I.0.ontology.ai-model-generated
I.0.ontology.hybrid
I.0.fontcuberta.post-photography
```

Ranking and collection membership are not rights clearance. Keep rejected and
unresolved records in the review report, not the public teaching pack. Do not
edit `digital-creativity-uem`; return the collection snapshot, rights report,
and accepted YAML handoff only after explicit human acceptance.
