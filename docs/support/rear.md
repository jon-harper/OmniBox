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

The rear panel is highly customizable with the [Rear Panel Template](../upgrade/templates.md#rear-panel).

<figure markdown>
[![rear panel illustration](../img/components/rear.webp){width="480px"}](../img/components/rear.webp)
<figcaption markdown>
In addition to acting as a wiring passthru for your printer, rear panels are a major ventilation source.
</figcaption>
</figure>

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}