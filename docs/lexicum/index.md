---
layout: lexicum
title: Fashion Lexicum
description: Controlled vocabulary for fashion design, business, and communication — Creación Digital.
lang: en
permalink: /lexicum/
---

{%- assign lex = site.data.lexicum -%}
{%- assign prov = lex.provenance -%}

<div class="lexicum-page" data-lexicum markdown="0">
<section class="lexicum-hero" aria-labelledby="lexicum-title">
<div class="lexicum-hero__inner">
<p class="lexicum-eyebrow">Controlled vocabulary</p>
<h1 id="lexicum-title">Fashion Lexicum</h1>
<p class="lexicum-hero__lede">{{ lex.field.description }}</p>
<ul class="lexicum-stats" aria-label="Lexicum statistics">
<li><strong>{{ lex.stats.concepts }}</strong> concepts</li>
<li><strong>{{ lex.stats.subfields }}</strong> schemes</li>
<li>Design · Business · Communication</li>
</ul>
{%- if prov %}
<div class="lexicum-credit">
<p class="lexicum-credit__by">
By <a href="{{ prov.author.orcid }}">{{ prov.author.name }}</a>
{%- if prov.author.role %} — {{ prov.author.role }}{% endif %}
· ORCID <a href="{{ prov.author.orcid }}">0000-0001-6862-9081</a>
</p>
<p class="lexicum-credit__stack">
Built with <strong>{{ prov.vocabulary_engine.name }} {{ prov.vocabulary_engine.version }}</strong>
(YAML → SKOS ConceptSchemes);
published via <strong>{{ prov.publication_stack.static_site }}</strong>
+ {{ prov.publication_stack.templates }};
ontology layer <a href="{{ prov.ontology.skos.url }}">SKOS (2009-08-18)</a>
with optional <a href="{{ prov.ontology.cidoc_crm.url }}">CIDOC-CRM {{ prov.ontology.cidoc_crm.version }}</a> class maps.
</p>
<p class="lexicum-credit__method">{{ prov.method }}</p>
</div>
{%- endif %}
</div>
</section>

<div class="lexicum-toolbar" role="search">
<div class="lexicum-toolbar__inner">
<label class="sr-only" for="lexicum-search">Search concepts</label>
<input id="lexicum-search" class="lexicum-search" type="search" placeholder="Search labels, definitions, aliases…" data-lexicum-search autocomplete="off" />
<div class="lexicum-filters" role="group" aria-label="Filter by scheme">
<button type="button" class="lexicum-filter" data-lexicum-filter="all" aria-pressed="true">All</button>
{%- for scheme in lex.subfields %}
<button type="button" class="lexicum-filter" data-lexicum-filter="{{ scheme.slug }}" aria-pressed="false">{{ scheme.title | replace: 'Fashion ', '' }}</button>
{%- endfor %}
</div>
</div>
</div>

<div class="lexicum-body">
{%- for scheme in lex.subfields %}
{%- assign scheme_anchor = scheme.slug | replace: '_', '-' %}
<section class="lexicum-scheme" id="{{ scheme_anchor }}" aria-labelledby="scheme-{{ scheme.slug }}">
<header class="lexicum-scheme__head">
<h2 id="scheme-{{ scheme.slug }}">{{ scheme.title }}</h2>
<p class="lexicum-scheme__meta">{{ scheme.concept_count }} concepts · <code>{{ scheme.slug }}</code></p>
{%- if scheme.description and scheme.description != '' %}
<p class="lexicum-scheme__desc">{{ scheme.description }}</p>
{%- endif %}
</header>
<div class="lexicum-concepts">
{%- for concept in scheme.concepts %}
{%- assign concept_anchor = scheme_anchor | append: '--' | append: concept.slug %}
{%- capture search_blob -%}{{ concept.pref_label }} {{ concept.definition }} {% for a in concept.alt_labels %}{{ a }} {% endfor %} {{ concept.crm_mapping }} {{ concept.scope_note }}{%- endcapture %}
<article class="lexicum-concept" id="{{ concept_anchor }}" data-lexicum-concept data-scheme="{{ scheme.slug }}" data-search="{{ search_blob | strip | escape }}">
<h3 class="lexicum-concept__label">{{ concept.pref_label }}</h3>
<p class="lexicum-concept__def">{{ concept.definition }}</p>
{%- if concept.alt_labels.size > 0 %}
<ul class="lexicum-concept__alts" aria-label="Alternative labels">
{%- for alt in concept.alt_labels %}
<li><span class="lexicum-chip">{{ alt }}</span></li>
{%- endfor %}
</ul>
{%- endif %}
{%- assign rel_groups = 'broader,narrower,related' | split: ',' %}
{%- for group_name in rel_groups %}
{%- if group_name == 'broader' %}{%- assign refs = concept.broader -%}{%- endif %}
{%- if group_name == 'narrower' %}{%- assign refs = concept.narrower -%}{%- endif %}
{%- if group_name == 'related' %}{%- assign refs = concept.related -%}{%- endif %}
{%- if refs.size > 0 %}
<ul class="lexicum-concept__rels" aria-label="{{ group_name }} relations">
{%- for ref in refs %}
{%- assign ref_sub = scheme.slug -%}
{%- assign ref_slug = ref -%}
{%- if ref contains '.' -%}
{%- assign ref_parts = ref | split: '.' -%}
{%- assign ref_sub = ref_parts[0] -%}
{%- assign ref_slug = ref_parts[1] -%}
{%- endif -%}
{%- assign ref_label = ref_slug -%}
{%- for s2 in lex.subfields -%}
{%- if s2.slug == ref_sub -%}
{%- for c2 in s2.concepts -%}
{%- if c2.slug == ref_slug -%}
{%- assign ref_label = c2.pref_label -%}
{%- endif -%}
{%- endfor -%}
{%- endif -%}
{%- endfor -%}
{%- assign ref_anchor = ref_sub | replace: '_', '-' | append: '--' | append: ref_slug -%}
<li><span class="lexicum-chip lexicum-chip--rel"><span class="lexicum-chip__kind">{{ group_name }}</span> <a href="#{{ ref_anchor }}">{{ ref_label }}</a></span></li>
{%- endfor %}
</ul>
{%- endif %}
{%- endfor %}
{%- if concept.crm_mapping or concept.scope_note %}
<p class="lexicum-concept__semantic">
{%- if concept.crm_mapping %}<span class="lexicum-semantic__crm"><span class="lexicum-semantic__key">CIDOC-CRM</span> {{ concept.crm_mapping }}</span>{%- endif %}
{%- if concept.crm_mapping and concept.scope_note %} · {% endif %}
{%- if concept.scope_note %}<span class="lexicum-semantic__scope">{{ concept.scope_note }}</span>{%- endif %}
</p>
{%- endif %}
</article>
{%- endfor %}
</div>
</section>
{%- endfor %}

<p class="lexicum-empty" data-lexicum-empty role="status">No concepts match this search. Clear the query or choose another scheme.</p>
<p class="lexicum-footnote">
Schema <code>lexfield-public/v1</code> — fashion is the prototype tenant of the multi-field vocabulary engine.
Snapshot {{ lex.cloned_at | default: '' }}.
</p>
</div>
</div>
