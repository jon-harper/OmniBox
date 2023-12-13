---
title: Core
summary: List of all core case components.
authors: Jon Harper
date: 2023-12-13
---

{% import 'format.md' as format with context %}
{% set prefix = '../' -%}

This page lists all Core component configurations for OmniBox.

## Main Body

{% set comp_type='Main Body' -%}

{% set items = product.sortComponents(product.filterComponents(comp_type).values()) -%}

{% for comp in items -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor %}

## Base

{% set comp_type='Base' -%}

{% set items = product.sortComponents(product.filterComponents(comp_type).values()) -%}

{% for comp in items -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor %}