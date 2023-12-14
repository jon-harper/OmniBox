---
title: PSUs
summary: List of all power supply components.
authors: Jon Harper
date: 2023-12-13
---

{% import 'format.md' as format with context %}
{% set prefix = '../' -%}
{% set comp_type='PSU' -%}

{% set items = product.sortComponents(product.filterComponents(comp_type).values()) -%}

This page lists power supplies (PSUs) currently supported by OmniBox.

<figure markdown>
  [![front left render](../img/components/psu.webp){ width="480" }](../img/components/psu.webp)
  <figcaption>Power supplies are mounted underneath the case body.</figcaption>
</figure>

!!! note "Note: Mean Well Clones"
    There are several brands of clones, usually using the same model number as Mean Well. The most common of these is the Landy LRS-350-24. These clones are generally compatible with the Mean Well trays.

{% for comp in items -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor %}