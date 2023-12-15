---
title: Displays
summary: List of all CPU and MCU displays.
authors: Jon Harper
date: 2023-12-13
---

{% import 'format.md' as format with context %}
{% set prefix = '../' -%}
{% set comp_type='Display' -%}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists all displays compatible with OmniBox.

{% for comp in items -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor %}