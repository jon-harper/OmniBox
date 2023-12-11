---
title: Sourcing
summary: List of parts and known sources
authors: Jon Harper
date: 2023-11-30
---

{% for part_type in product.part_types -%}

{% if part_type != 'Printed' %}

### {{ part_type }}

{% for part_id, part in product.filterParts(part_type).items() -%}

{{ fmt.sourcing_part_entry(part_id, part) }}

{% endfor %}

{% endif -%}

{% endfor %}

