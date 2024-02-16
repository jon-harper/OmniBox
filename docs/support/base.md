---
title: Base
summary: List of all OmniBox Bases.
authors: Jon Harper
date: 2023-12-13
prefix: ../
---

{% import 'format.md' as format with context %}
{% set comp_type='Base' -%}
{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists the configurations available for OmniBox's Base and discusses the options available.

## Base Options

### Base Depth

Before printing a specific base, ensure it is deep enough for your power supply (you can check this on the [PSU](psu.md) page).

### Power Switch

The OmniBox Base can be printed to accept either a 29mm x 10.5mm snap-in SPST rocker switch or a 12mm toggle switch.

Larger power supplies will not fit with a toggle switch. Check the [:octicons-checklist-24: PSU Trays](support/psu.md)
page for more.

### IEC C14 Power Socket

Power is provided through a standard fused IEC C14 power socket. The Basic base is available for users with different
power inlet needs (e.g. a power inlet with integrated switch).

## Bases

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}