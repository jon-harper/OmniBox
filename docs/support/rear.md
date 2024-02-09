---
title: Rear Panels
summary: List of all rear panels.
authors: Jon Harper
date: 2023-12-13
prefix: ../
comp_type: Rear Panel
---

{% import 'format.md' as format with context %}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

This page lists all side panels for OmniBox.

<figure markdown>
[![rear panel illustration](../img/components/rear.webp){width="480px"}](../img/components/rear.webp)
<figcaption markdown>
Rear panels serve many purposes.
</figcaption>
</figure>

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}