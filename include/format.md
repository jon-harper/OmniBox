{% import 'badges.md'as badges -%}

{% macro part_header(part_id, name) -%}
<a name="{{part_id}}"></a> {{ name }}
{% endmacro -%}

{% macro add_image(obj, prefix, img_width="240px") -%}
{% if obj.img_url -%}
{% set dest = prefix + obj.img_url -%}
[![{{obj.name}}]({{dest}}){ width="{{img_width}}" }]({{dest}})
{% endif -%}
{% endmacro -%}

{% macro add_figure(obj, prefix, img_width="240px") -%}
{% if obj.img_url -%}
{% set dest = prefix + obj.img_url -%}
<figure markdown>
[![{{obj.name}}]({{dest}}){ width="{{img_width}}" }]({{dest}})
</figure>
{% endif -%}
{% endmacro -%}

{%- macro add_note(comp) -%}
{% if comp.note -%}
{{ comp.note }}
{% else -%}
*(None)*
{% endif -%}
{% endmacro -%}

{%- macro add_hsi_info(item, img_width="200px", prefix='')-%}
{%- if 'hsi_img' in item.attributes.keys() %}
??? hsi "Heat Set Insert Locations"
    <div markdown class="grid">
{% for url in item.attributes['hsi_img'] %}
    [![Heat set insert details]({{prefix + url}}){ width="{{img_width}}"}]({{prefix + url}})
{% endfor %}
    </div>
{% endif -%}
{%- endmacro -%}

{% macro comp_entry(comp, img_width="240px", prefix='') -%}
### {{ comp.name }}

{% if comp.attributes and comp.attributes['fit_test'] -%}

{{issue_tag(comp.attributes['fit_test'])}}
{% endif -%}

{% if comp.variants | count > 1 %}
{%- set indent='    ' -%}
{% for v in comp.variants -%}
=== "{{ v.name }}"
{{indent}}<div markdown class="grid"><div markdown>
{{indent}}{{ badges.render(comp, v, prefix=prefix) }}
{{indent}}
{{indent}}:octicons-paperclip-24: **General Notes**
{{indent}}
{{ make_indented(add_note(comp), indent) }}
{% if v.note -%}
{{indent}}:material-text-box-multiple-outline: **Variant Notes**
{{indent}}
{{ make_indented(add_note(v), indent) }}
{%- endif %}
{{indent}}</div><div markdown>
{{make_indented (add_figure(comp, prefix, img_width), indent) }}
{{indent}}</div></div>
{{indent}}:octicons-pencil-24: **Materials**
{{indent}}
{{ make_indented(bom_table(v, prefix=prefix), indent) }}
{{ make_indented(add_hsi_info(v, "200px", prefix), indent)}}
{%- endfor -%}
{%- else -%} {# comp.variants | count > 1 #}
{%- set v = comp.variants[0] -%}
<div markdown class="grid"><div markdown>
{{ badges.render(comp, v, prefix=prefix) }}

:octicons-paperclip-24: **General Notes**

{{ add_note(comp) }}

{% if v.note -%}
:material-text-box-multiple-outline: **Variant Notes**

{{add_note(v)}}
{%- endif %}
</div>
<div markdown>
{{ add_figure(comp, prefix, img_width) }}
</div>
</div>

:octicons-pencil-24: **Materials**

{{ bom_table(v, prefix=prefix) }}
{{ add_hsi_info(v, "200px", prefix) }}
{% endif -%} {# comp.variants | count > 1 #}

---------
{% endmacro -%}

{% macro source_table(part) -%}
| Source | Ships To | Ships From | Note |
|--------|----------|------------|------|
{% if part.sources | count == 0 -%}
| | | |
{% else -%}
{% for source in part.sources -%}
| [{{source.supplier.name}}]({{source.url}} "{{source.supplier.name}}: {{part.name}}") | {{ source.supplier.ships }} | {{ source.supplier.region }} | {{ source.note }} |
{% endfor -%}
{% endif -%}
{% endmacro -%}

{% macro bom_table(variant, prefix='') -%}
| Type | Part | Qty |
|------|------|-----|
{% if variant.parts -%}
{% for part_id, qty in variant.parts.items()-%}
{% set part = product.partFromId(part_id) -%}
{% set link = part_link(part_id, part, prefix=prefix) -%}
{% if part.part_type == 'Printed' -%}
|:material-printer-3d-nozzle: {{part.part_type}}|{{link}}|{{qty}} {{part.units}}|
{% else -%}
|{{part.part_type}}|{{link}}|{{qty}} {{part.units}}|
{% endif -%}
{% endfor -%}
{% endif %}
{% endmacro -%}

{# I hate the way this macro is written, but a more concise version has newlines. #}
{# Spoiler alert: still hate it. #}
{% macro part_link(part_id, part = None, prefix = '', url_text=None) -%}
{% if not part -%}
{% set part = product.partFromId(part_id=part_id) -%}
{% endif -%}
{% if not url_text -%}
{% set url_text = part.name -%}
{% endif -%}
{% if not part.file_url and not part.sources -%}
{{url_text}}{% else -%}
{% if part.part_type == 'Printed' and part.file_url -%}
{% if part.file_url.startswith(product.local_url_prefix) -%}
{% set icon = ":material-git:" -%}
{% set url = part.file_url -%}
{% set tooltip = "OmniBox GitHub file download"-%}
{% else -%}
{% set icon = ':octicons-link-external-24:' -%}
{% set url = part.file_url -%}
{% set tooltip = 'External site file download'-%}
{% endif -%}
{% elif part.sources -%}
{% set icon = ':material-cart:' -%}
{% set url = prefix + 'sourcing/#' + part_id -%}
{% set tooltip =  'Sourcing information' -%}
{% endif -%}
[{{icon}} {{url_text}}]({{url}} "{{tooltip}}"){% endif -%}
{% endmacro -%}