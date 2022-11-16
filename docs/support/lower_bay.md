---
title: Lower Bay Components
summary: A complete list of parts supported by OmniBox
authors: Jon Harper
date: 2022-07-22
---

Lower Bay Trays mount below the MCU board and are used for a wide range of parts. Parts compatible with the lower bay are listed here. The [:material-git: `Trays/Lower Bay`][git_lower_bay] git folder is organized with subfolders for each supported part. All variations based around that part are in the same folder.

There are two types of Lower Bay Trays: Short and Long. A Long length tray covers the mount points of two Short trays and must be mounted from front to back of the case.

<figure markdown>
  [![img][img_lower_bay]{ width="480" }][img_lower_bay]
  <figcaption>Long trays fit as pictured on the left side or right. Short trays will also fit in an empty CPU bay.</figcaption>
</figure>

<!-- Template
[:material-git: Files: ``][git_]{ .md-button }

[:material-cart: Product Link][bom_]{ .md-button }

[![product picture][img_]{width="200"}][img_]

- Mounting:
- Trays:
 -->

## Buck Converters

Long trays for buck converters often have a 40mm fan mount. This is particularly useful for 2A buck converters that are rated to 3A with cooling.

### Basic 2A LM2596

[:material-git: Files: `Generic LM2596`][git_basic_lm2596]{ .md-button }

[:material-cart: Product Link][bom_basic_lm2596]{ .md-button }

[![product picture][img_basic_lm2596]{width="200"}][img_basic_lm2596]

- Mounting: 2x M3
- Trays:
    - Short (single, dual)
    - Long (single, dual)

### DROK 2A LM2596 with LED

[:material-git: Files: `DROK LM2596 with LED`][git_drok_2A]{ .md-button }

[:material-cart: Product Link][bom_drok_2A]{ .md-button }

[![product picture][img_led_lm2596]{width="200"}][img_led_lm2596]

- Mounting: 4x M3
- Hole Pattern: 60.5mm x 30.5mm
- Tray:
    - Short (single)
    - Long (single, dual)

### HiLetGo 2A LM2596 with LED

[:material-git: Files: `HiLetGo LM2596 with LED`][git_hiletgo_2A]{ .md-button }

[:material-cart: Product Link][bom_hiletgo_2A]{ .md-button }

[![product picture][img_hiletgo_2a]{width="200"}][img_hiletgo_2a]

- Mounting: 4x M3
- Hole Pattern: 49.5mm x 27.5mm 
- Trays:
    - Short (single)
    - Long (single, dual)

### DROK 3A LM2596 with LED

[:material-git: Files: `DROK 3A LM2596 with LED`][git_drok_3A]{ .md-button }

[:material-cart: Product Link][bom_drok_3A]{ .md-button }

[![product picture][img_drok_3a]{width="200"}][img_drok_3a]

- Mounting: 4x M3
- Hole Pattern: 52.5mm x 28.75mm
- Trays:

    - Short (single)

### DROK 5A Buck with LED

[![product picture][img_drok_5a]{width="200"}][img_drok_5a]

[:material-git: Files: `DROK 5A Buck with LED`][git_drok_5A]{ .md-button }

[:material-cart: Product Link][bom_drok_5A]{ .md-button }

Mounting: 4x M3, 63mm x 40.5mm

Trays:

- Long (single)

## MOSFETs


### Creality MOSFET 

[:material-git: Files: `Creality MOSFET`][git_creality_mosfet]{ .md-button }

[:material-cart: Product Link][bom_creality_mosfet]{ .md-button }

[![product picture][img_creality_mosfet]{width="200"}][img_creality_mosfet]

- Mounting: 2x M3
- Trays:
    - Short (single)
    - Long (single)

## Solid State Relays

### Fotek SSR-40 DA 

[:material-git: Files: `Fotek SSR-40 DA`][git_fotek_ssr40da]{ .md-button }

[:material-cart: Product Link][bom_fotek_ssr_40da]{ .md-button }

[![product picture][img_fotek_ssr_40da]{width="200"}][img_fotek_ssr_40da]

- Mounting: 2x M3
- Trays:
    - Short (single)
    - Long (single)

## Other Products

<!-- ### BIGTREETECH UPS 24V 1.0 

[:material-git: Files: ``][git_]{ .md-button }

[:material-cart: Product Link][bom_btt_ups_24v]{ .md-button }

[![product picture][img_btt_ups_24v]{width="200"}][img_btt_ups_24v]

- Mounting:
- Trays:
    - Short (single) -->

### Wago 221 Lever Nuts 

[:material-git: Files: `Wago Lever Nuts`][git_wago_221]{ .md-button }

[:material-cart: Product Link][bom_wago_nuts]{ .md-button }

[![product picture][img_wago_nuts]{width="200"}][img_wago_nuts]

- Notes: 3 position & 5 position
- Trays:
    - Short, 4x 3 position
    - Long, 4x 5 position
    - Long, 4x 5 position, 2x 3 position

### 4010/4020 Fans 

[:material-git: Files: `40mm Fan`][git_tray_4010]{ .md-button }

[:material-cart: Product Link][bom_4010]{ .md-button }

[![product picture][img_4010]{width="200"}][img_4010]

- Notes: Also available on long trays for buck converters.
- Trays:
    - Short (single)

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