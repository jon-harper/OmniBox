---
title: Lower Bay
summary: List of all lower bay trays.
authors: Jon Harper
date: 2023-12-13
prefix: ../
comp_type: Lower Bay
---

{% import 'format.md' as format with context %}

{% set items = product.sortEntries(product.filterComponents(comp_type).values()) -%}

Lower Bay Trays may be Short or Long. A Long tray covers the mount points of two Short trays and must be mounted
from side-to-side in the case. There are two dedicated lower bay trays locations and four more that can occupy
an unused CPU tray bay.

<figure markdown>
  [![img][img_lower_bay]{ width="480" }][img_lower_bay]
  <figcaption>Up to three (3) Long trays will fit in a case, or six (6) Short trays.</figcaption>
</figure>

[img_lower_bay]: ../img/components/lower_bay.webp

{% for comp in items -%}
{{ format.comp_entry(comp, prefix=prefix) }}
{% endfor %}