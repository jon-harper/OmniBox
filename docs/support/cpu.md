---
title: CPUs
summary: List of all SoC/SBC CPU components
authors: Jon Harper
date: 2023-12-13
prefix: ../
comp_type: CPU
---

{% import 'format.md' as format with context %}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists system-on-a-chip (SoC) CPUs currently compatible with OmniBox. These are commonly known as single board computers (SBC).

<figure markdown>
  [![front left render](../img/components/cpu.webp){ width="480" }](../img/components/cpu.webp)
  <figcaption>CPU trays can be mounted on the left or right side of the case.</figcaption>
</figure>

If you do not use an SBC, the side of the CPU bay can be used as a [:octicons-checklist-24: Side Panel](side.md).


{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}