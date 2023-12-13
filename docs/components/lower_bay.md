---
title: Lower Bay
summary: List of all lower bay trays.
authors: Jon Harper
date: 2023-12-13
---

{% import 'format.md' as format with context %}
{% set prefix = '../' -%}
{% set comp_type='Lower Bay' -%}

{% set items = product.sortComponents(product.filterComponents(comp_type).values()) -%}

This page lists all components available for the lower bay.

{% for comp in items -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor %}