---
title: MCUs
summary: List of all MCU components
authors: Jon Harper
date: 2023-12-13
prefix: ../../
comp_type: MCU
---

{% import 'format.md' as format with context %}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists microcontroller boards that are currently compatible with OmniBox.

<figure markdown>
  [![front left render][img_mcu]{ width="480" }][img_mcu]
  <figcaption>MCUs are mounted near the lid for accessibility.</figcaption>
</figure>

[img_mcu]: ../img/components/mcu.webp

!!! tip
    Looking for a board that isn't listed? [:material-git: Open an issue!][git_issues]


{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}