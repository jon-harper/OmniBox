---
title: Displays
summary: List of all CPU and MCU displays.
authors: Jon Harper
date: 2023-12-13
prefix: ../
comp_type: Display
---

{% import 'format.md' as format with context %}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists all displays compatible with OmniBox.

<figure markdown>
[![display panel illustration](../img/components/display.webp){width="480px"}](../img/components/display.webp)
<figcaption markdown>
Display panels are the primary method of interacting with your OmniBox.
</figcaption>
</figure>

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}