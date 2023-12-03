---
title: Debug Tests
summary: Debugging stuff
authors: Jon Harper
date: 2023-06-15
---

## Printed Files

| Name | Version | Contributor |
|------|---------|-------------|
{% for part_id, part in parts().items() -%}
    {% if part.part_type == 'Printed' -%}
        {% if part.version -%}
            {% set vers = part.version -%}
        {% else -%}
            {% set vers = "n/a" -%}
        {% endif -%}
        {% if part.author -%}
            {% set contrib = part.author.name -%}
        {% else -%}
            {% set contrib = '' -%}
        {% endif -%}
        {{ '| {} | {} | {} |'.format(part_link(part_id), vers, author_link(part.author)) }}
    {% endif -%}
{% endfor %}

{% for assy_type in assembly_types() -%}

{% if assy_type != "subassemblies" -%}

## {{ assy_type }}

{% for assy in filter_assemblies(assy_type).values() -%}
{% if assy.name -%}

### {{ assy.name }}

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

{% endif -%}

{% endfor %}

## Contributors

{% for author_id, author in part_authors().items() -%}
- [{{ author.name }}]({{ author.url}})
{% endfor -%}
