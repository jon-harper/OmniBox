---
title: Debug Tests
summary: Debugging stuff
authors: Jon Harper
date: 2023-06-15
---

## Full BOM

{% for part in part_data.values() -%}
### {{ part.name }}

- ID: {{part.part_id}}

{% if part.image_url -%}
{{ product_img(part.image_url, width=480) }}
{% endif -%}
{% endfor -%}

## Bundlr BOM Generator

<!-- <form id="bundlr-form" method="POST">
    <select name="lid">
        <option disabled="">Lid</option>
        <option value="short">Short</option><option value="long">Long</option>
    </select>
    <select name="mcu_tray">
        <option disabled="">MCU Tray</option>
        <option value="mcu_btt_octopus">BTT Octopus</option>
        <option value="mcu_skr_pico">SKR Pico</option>
    </select>
    <select name="side_panel_1">
        <option disabled="">Side Panel 1</option>
        <option value="side_panel_blank">Blank</option>
        <option value="side_panel_fan5012">50x12mm Fan</option>
    </select>
    </br></br>
    <input id="bundle-button" class="md-button" type="button" value="Generate ZIP Bundle">
    <input id="bom-button" class="md-button" type="button" value="Generate BOM">
</form> -->