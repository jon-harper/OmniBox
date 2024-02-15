---
title: Main Body
summary: List of all Main Bodies for OmniBox.
authors: Jon Harper
date: 2023-12-13
prefix: ../
---

{% import 'format.md' as format with context %}

This page lists all Core component configurations for OmniBox.

## Main Body

{% set comp_type='Main Body' -%}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}
