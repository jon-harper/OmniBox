---
title: Bottom Panels
summary: List of all bottom panels.
authors: Jon Harper
date: 2023-12-13
---

{% import 'format.md' as format with context %}
{% set prefix = '../' -%}
{% set comp_type='Bottom Panel' -%}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists all bottom panels for OmniBox.

{% for comp in items -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor %}