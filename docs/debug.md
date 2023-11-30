---
title: Debug Tests
summary: Debugging stuff
authors: Jon Harper
date: 2023-06-15
---

## Printed Files

| Name | Link | Version |
|------|------|---------|
{% for part_id, part in parts().items() -%}
{% if part.file_url -%}

{% if part.version -%}
| {{ part.name }} | [File]({{ part.file_url }}) | Version: {{part.version}} |
{% else -%}
| {{ part.name }} | [File]({{ part.file_url }}) | n/a |
{% endif -%}

{% endif -%}
{% endfor %}

## Assemblies

{% for assy in assemblies().values() -%}
{% if assy.name -%}

### {{ assy.name }}

{% if assy.assy_type -%}
Type: {{ assy.assy_type }}
{% endif %}

{% if assy.attributes -%}
Attributes: {{ assy.attributes }}
{% endif %}

| Type | Part | Qty | UOM |
|------|------|-----|-----|
{% for part_id, qty in assy.parts.items() -%}
{{ bom_table_row(part_id, qty) }}
{% endfor %}

{% endif -%}

{% endfor %}

## Contributors

{% for author_id, author in part_authors().items() -%}
- [{{ author.name }}]({{ author.url}})
{% endfor -%}
