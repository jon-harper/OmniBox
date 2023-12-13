---
title: Sourcing
summary: List of parts and known sources
authors: Jon Harper
date: 2023-11-30
---

{% import 'format.md' as format with context %}

{% for part_type in product.part_types -%}

{% if part_type != 'Printed' %}

### {{ part_type }}

{% for part_id, part in product.sortParts(product.filterParts(part_type).items()) -%}

#### {{ part.name }}

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
{{ format.source_table(part) }}
</div>
{% if part.img_url -%}
<div markdown class="jh-grid-img">
[![{{part.name}}]({{part.img_url}}){ width="240px" }]({{part.img_url}})
</div>
{% endif -%}
</div>
{% endfor %}

{% endif -%}

{% endfor %}

