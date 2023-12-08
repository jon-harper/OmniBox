---
title: Debug Tests
summary: Debugging stuff
authors: Jon Harper
date: 2023-06-15
---

### Test Product

{{ fmt.badge(':material-tag:', 'Version', 'http://', 'mcu_v2') }}

{{ fmt.badge(':octicons-person-fill-24:', 'Contributor', 'http://', 'MrMeh', 'http://')}} 

{{ fmt.badge(':material-cog-outline:', 'Uses heat set inserts', 'http://') }}

{% set assy_type = 'MCU' -%}

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

