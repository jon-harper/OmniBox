---
title: Bottom Panels
summary: List of all bottom panels.
authors: Jon Harper
date: 2023-12-13
prefix: ../../
comp_type: Bottom Panel
---

{% import 'format.md' as format with context %}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists all bottom panels for OmniBox.
<figure markdown>
[![Bottom panel illustration](../img/components/bottom.webp){width="360px"}](../img/components/bottom.webp)
<figcaption markdown>
Bottom panels cover up the power supply and give your case feet.
</figcaption>
</figure>

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}