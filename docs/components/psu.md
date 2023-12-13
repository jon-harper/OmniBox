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

This page lists all SBCs/SoC CPUs compatible with OmniBox.


{% for comp in items -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor %}