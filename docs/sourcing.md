---
title: Sourcing
summary: List of parts and known sources
authors: Jon Harper
date: 2023-11-30
---

{% for part_type in part_types() -%}

{% if part_type != 'Printed' %}

### {{ part_type }}

{% for part_id, part in filter_parts(part_type).items() -%}

#### {{ part_header(part_id, part.name) }}

{{ source_table(part) }}

{% endfor %}

{% endif -%}

{% endfor %}
