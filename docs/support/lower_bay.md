---
title: Lower Bay Components
summary: A complete list of parts supported by OmniBox
authors: Jon Harper
date: 2022-07-22
---

:material-alpha-t-box: :material-alpha-l-box-outline: Lower Bay Trays mount below the MCU board and are used for a wide range of parts. Parts compatible with the lower bay are listed here. The [`Trays/Lower Bay`][git_lower_bay] git folder is organized with subfolders for each supported part. All variations based around that part are in the same folder.

There are two types of :material-alpha-t-box: :material-alpha-l-box-outline: Lower Bay Trays: Short and Long. A Long length tray covers the mount points of two Short trays and must be mounted from front to back of the case.


<figure markdown>
  [![img][img_lower_bay]{ width="480" }][img_lower_bay]
  <figcaption>Long trays fit as pictured on the left side or right. Short trays will also fit in an empty CPU bay.</figcaption>
</figure>

## Buck Converters

Long trays for buck converters often have a 40mm fan mount. This is particularly useful for 2A buck converters that are rated to 3A with cooling.

| Description | Image | Product Link | Tray Sizes | Notes |
|----|---|---|---|---|
| Basic 2A LM2596 Buck Converter | ![img][img_basic_lm2596] | [:material-cart: Example][bom_basic_lm2596] | Short (single, dual), Long (single, dual) | |
| "DROK" 2A LM2596 with LED       | ![img][img_led_lm2596] | [:material-cart: Example][bom_drok_2A] | Short (single), Long (single, dual) | Mounting holes: 60.5mm x 30.5mm |
| "HiLetgo" 2A LM2596 with LED | ![img][img_hiletgo_2a] | [:material-cart: Example][bom_hiletgo_2A] | Short (single), Long (single, dual) | Mounting holes: 49.5mm x 27.5mm |
| "DROK" 5A Buck with LED | ![img][img_drok_5a] | [:material-cart: Example][bom_drok_5A] | Long (single) | Mounting Holes: 63mm x 40.5mm |
| "DROK" 3A Buck with LED | ![img][img_drok_3a] | [:material-cart: Example][bom_drok_3A] | Short (single) | Mounting Holes: 52.5mm x 28.75mm |

## MOSFETs

| Description | Image | Product Link | Tray Sizes | Notes |
|---|---|---|---|---|
| Creality MOSFET | ![img][img_creality_mosfet] | [:material-cart: Example][bom_creality_mosfet] |  Short (single), Long (single) | |

## Solid State Relays (SSRs)

| Description | Image | Product Link | Tray Sizes | Notes |
|---|---|---|---|---|
| Fotek SSR-40 DA | ![img][img_fotek_ssr_40da] | [:material-cart: Example][bom_fotek_ssr_40da] |  Short (single), Long (single) | |

## Other Products

| Description | Image | Product Link | Tray Sizes | Notes |
|---|---|---|---|---|
| BIGTREETECH UPS 24V 1.0 | ![img][img_btt_ups_24v] | [:material-cart: Example][bom_btt_ups_24v] | Short (single) | |
| Wago 221 Lever Nuts | ![img][img_wago_nuts] | [:material-cart: Example][bom_wago_nuts] |  Short, Long | 3 position & 5 position |
| 4010/4020 fans | ![img][img_4010] | [:material-cart: Example][bom_4010] | Short | Also available on long trays for buck converters. |

[img_lower_bay]: ../img/components/lower_bay.png
[img_drok_3a]: ../img/parts/buck_3a_drok.jpg
[img_drok_5a]: ../img/parts/buck_5a_drok.jpg
[img_basic_lm2596]: ../img/parts/lm2596.jpg
[img_led_lm2596]: ../img/parts/lm2596_led.jpg
[img_creality_mosfet]: ../img/parts/mosfet_creality.jpeg
[img_fotek_ssr_40da]: ../img/parts/fotek_ssr-40_da.jpeg
[img_hiletgo_2a]: ../img/parts/lm2596_led_2.jpg
[img_wago_nuts]: ../img/parts/wago_nuts.jpg
[img_btt_ups_24v]: ../img/parts/btt_ups_24v.jpg
[img_4010]: ../img/parts/fan_4010.jpg