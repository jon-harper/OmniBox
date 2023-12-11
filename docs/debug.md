---
title: Debug Tests
summary: Debugging stuff
authors: Jon Harper
date: 2023-06-15
---

# All Components

{% for comp_type in product.assembly_types -%}

## {{ comp_type }}

{% for comp_id, comp in product.filterComponents(comp_type).items() -%}
{{ fmt.component_entry(comp) }}

---------

{% endfor -%}

{% endfor %}
