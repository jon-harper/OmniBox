---
title: Main Body
summary: List of all Main Bodies for OmniBox.
authors: Jon Harper
date: 2023-12-13
prefix: ../
---

{% import 'format.md' as format with context %}

This page lists all Main Body configurations for OmniBox.

<figure markdown>
[![OmniBox main body](../img/components/main_body.webp){ width="480px" }](../img/components/main_body.webp)
<figcaption markdown>
Most trays and panels attach to the Main Body.
</figcaption>
</figure>

{% set comp_type='Main Body' -%}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}
