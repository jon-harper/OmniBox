---
title: Side Panels
summary: List of all side panels.
authors: Jon Harper
date: 2023-12-13
prefix: ../../
comp_type: Side Panel
---

{% import 'format.md' as format with context %}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists all side panels for OmniBox.

<figure markdown>
[![side panel illustration](../img/components/side.webp){width="480px"}](../img/components/side.webp)
<figcaption markdown>
Side panels can mount CPU trays, fans, or connectors.
</figcaption>
</figure>

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}