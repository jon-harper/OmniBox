---
title: Debug Tests
summary: Debugging stuff
authors: Jon Harper
date: 2023-06-15
---

{% for part in part_data.values() -%}
### {{part.part_id}} : {{ part.name }}

{% if part.source -%}
- [:material-cart: {{ part.source.supplier }}]({{ part.source.url }})
{% endif -%}
{% if part.image_url -%}
{{ product_img(part.image_url, width=480) }}
{% endif -%}
{% endfor -%}
