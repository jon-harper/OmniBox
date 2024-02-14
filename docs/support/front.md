---
title: Front Panels
summary: List of all front panels.
authors: Jon Harper
date: 2023-12-13
prefix: ../
comp_type: Front Panel
---

{% import 'format.md' as format with context %}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists all front panels for OmniBox.

<figure markdown>
[![front panel illustration](../img/components/front_panel.webp){width="480px"}](../img/components/front_panel.webp)
<figcaption markdown>
Front panels provide ventilation and can mount SD card extensions, USB connectors, or even LED lights.
</figcaption>
</figure>

Panels normally have one of three vent styles:
<figure markdown>
[![front panel illustration](../img/components/fp_styles.webp){width="480px"}](../img/components/fp_styles.webp)
</figure>

1. Hexagons (Left)
2. Slots (Center)
3. Angled Slats (Right)

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}