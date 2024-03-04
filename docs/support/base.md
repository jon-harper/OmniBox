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

<figure markdown>
[![OmniBox base](../img/components/base.webp){width="480px"}](../img/components/base.webp)
<figcaption markdown>
The Base is the foundation of an OmniBox case.
</figcaption>
</figure>

## Base Options

### Base Depth

Before printing a specific base, ensure it is deep enough for your power supply (you can check this on the
[:octicons-checklist-24: PSU Trays](psu.md) page).

### Power Switch

The OmniBox Base can be printed to accept a 29mm x 10.5mm snap-in SPST rocker switch, a 12.5mm toggle switch, 
or none at all (if you are mounting a switch elsewhere, e.g., the front or real panel).

Larger power supplies are not compatible with toggle switches. The [:octicons-checklist-24: PSU Trays](psu.md)
page has specifics.

### IEC C14 Power Socket

<div class="grid" markdown>
<div markdown>
Power is provided through a standard fused IEC C14 power socket. The Basic base is available for users with different
power inlet needs (e.g. a power inlet with integrated switch).
</div>
<div markdown>
![an IEC C14 power socket](../img/parts/fused_iec_c14.webp){width="300px"}
</div>
</div>
## Bases

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}