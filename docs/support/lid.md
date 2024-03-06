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

Lids may be Short or Long; a case needs either a single Long lid or two Short lids.

<figure markdown>
[![front panel illustration](../img/components/lid.webp){width="480px"}](../img/components/lid.webp)
<figcaption markdown>
Lids can provide ventilation, mount a display, or even hold a spool roller.
</figcaption>
</figure>

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix, img_width="300px") }}
{% endfor %}