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

Lower Bay Trays may be Short or Long. A Long tray covers the mount points of two Short trays and must be mounted from side-to-side in the case.

Every tray (short or long) attaches to the Core case body with four (4) M3 x 6mm screws. Additional materials are listed with each part.

<figure markdown>
  [![img][img_lower_bay]{ width="480" }][img_lower_bay]
  <figcaption>Up to three (3) Long trays will fit in a case, or six (6) Short trays.
    <br/>A Short tray is pictured.</figcaption>
</figure>

[img_lower_bay]: ../img/components/lower_bay.webp

{% for comp in items -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor %}