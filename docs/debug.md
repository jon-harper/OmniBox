---
title: Debug Tests
summary: Debugging stuff
authors: Jon Harper
date: 2023-06-15
---

### Test Product

{{ fmt.badge(':material-tag:', 'http://', 'Version', 'mcu_v2') }} {{ fmt.badge(':octicons-person-fill-24:', 'http://', 'Contributor', 'MrMeh') }} {{ fmt.badge(':material-cog-outline:', 'http://', 'Uses Heat Set Inserts') }}

## Printed Files

| Name | Version | Contributor |
|------|---------|-------------|
{% for part_id, part in product.parts.items() -%}
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
        {{ '| {} | {} | {} |'.format(fmt.part_link(part_id), vers, fmt.author_link(part.author)) }}
    {% endif -%}
{% endfor %}

{% for assy_type in assembly_types() -%}

{% if assy_type != "subassemblies" -%}

## {{ assy_type }}

{% for section_name, entries in section_assemblies(filter_assemblies(assy_type)).items() -%}

### {{ section_name }}

{% if entries.keys() | count == 1 -%}
{% set _, assy = entries.popitem() -%}

{{ fmt.bom_table(assy) }}

{% else -%}
{% for assy_id, assy in entries.items() -%}
=== "{{ assy.attributes['variant'] }}"

{{ fmt.bom_table(assy, indent='    ') }}
{% endfor -%}

{% endif -%}

{% endfor %} 

{% endif -%}

{% endfor %} 

