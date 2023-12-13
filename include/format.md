{% macro comp_img(comp, width="240px", prefix = '') -%}
{% if comp.img_url -%}
    {% set url = prefix + comp.img_url -%}
[![{{comp.name}}]({{url}}){ width="{{width}}" }]({{url}})
{% endif -%}
{% endmacro -%}

{% macro comp_note(comp) -%}
{% if comp.note -%}
{{ comp.note }}
{% else -%}
*(None)*
{% endif -%}
{% endmacro -%}

{% macro comp_entry(comp, prefix='', img_width="240px") -%}
### {{ comp.name }}

<div markdown class="grid">
<div markdown>
:octicons-paperclip-24: **General Notes**

{{ comp_note(comp) }}
</div>
<div markdown>
{{ comp_img(comp, width=img_width, prefix=prefix) }}
</div>
</div>

:octicons-versions-24: **Details**

{% if comp.variants | count > 1 -%}
{% set indent='    ' -%}
{% for v in comp.variants -%}
=== "{{ v.name }}"
    {{ fmt.render_badges(comp, v)}}

{{ bom_table(v, indent=indent, prefix=prefix)}}
{% endfor -%}
{% else -%}
{% set v = comp.variants[0] -%}
{{ fmt.render_badges(comp, v)}}

{{ bom_table(v, prefix=prefix) }}
{% endif -%}
---------
{% endmacro -%}

{% macro source_table(part) -%}
| Source | Ships To | Ships From | Note |
|--------|----------|------------|------|
{% if part.sources | count == 0 -%}
| | | |
{% else -%}
{% for source in part.sources -%}
| [{{source.supplier.name}}]({{source.url}} "") | {{ source.supplier.ships }} | {{ source.supplier.region }} | {{ source.note }} |
{% endfor -%}
{% endif -%}
{% endmacro -%}

{% macro bom_table(variant, indent='', prefix='') -%}
{{indent}}| Type | Part | Qty |
{{indent}}|------|------|-----|
{% if variant.parts -%}
{% for part_id, qty in variant.parts.items()-%}
{% set part = product.partFromId(part_id) -%}
{% set link = fmt.part_link(part_id, part, prefix=prefix) -%}
{{indent}}|{{part.part_type}}|{{link}}|{{qty}}|
{% endfor -%}
{% endif %}
{% endmacro -%}
