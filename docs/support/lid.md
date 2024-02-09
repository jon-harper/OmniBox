---
title: Lids
summary: List of all lid panels.
authors: Jon Harper
date: 2023-12-13
prefix: ../
comp_type: Lid
---

{% import 'format.md' as format with context %}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists all lids available for OmniBox.

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix, img_width="300px") }}
{% endfor %}