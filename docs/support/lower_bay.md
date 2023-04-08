---
title: Lower Bay Components
summary: A complete list of parts supported by OmniBox
authors: Jon Harper
date: 2022-07-22
---

Lower Bay Trays mount below the MCU board and are used for a wide range of parts. Parts compatible with the lower bay are listed here. The [:material-git: `/Trays/Lower Bay`][git_lower_bay] git folder is organized with subfolders for each supported part. All variations based around that part are in the same folder.

There are two types of Lower Bay Trays: Short and Long. A Long length tray covers the mount points of two Short trays and must be mounted from the front to the back of the case.

Every tray (short or long) attaches to the Core case body with four (4) M3 x 6mm screws. Additional fasteners are listed with each component.

<figure markdown>
  [![img][img_lower_bay]{ width="480" }][img_lower_bay]
  <figcaption>Long trays fit as pictured on the left side or right. Short trays will also fit in an empty CPU bay.</figcaption>
</figure>

<!-- Template 
<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: ][git_]{ .md-button }

[:material-cart: Product Link][bom_]{ .md-button }

- Mounting:
- Trays:
</div>
<div markdown class="jh-grid-img">
[![product picture][img_]][img_]
</div>
</div>
-->

## Buck Converters

Long trays for buck converters often have a 40mm fan mount. This is particularly useful for 2A buck converters that are rated to 3A with cooling.

!!! note "Powering a Raspberry Pi"
    The Raspberry Pi 4B requires up to 3A of power, but typically uses less than 2.5A.  The LM2596 is rated to 2A of current without cooling; adding a heatsink or modest airflow allows it power a Raspberry Pi without issue.

### Basic 2A LM2596

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Generic LM2596][git_basic_lm2596]{ .md-button }

[:material-cart: Product Link][bom_basic_lm2596]{ .md-button }

- Materials: 2x M3 x 6mm
- Trays:
    - Short (single, dual)
    - Long (single, dual)
</div>
<div markdown class="jh-grid-img">
[![product picture][img_basic_lm2596]][img_basic_lm2596]
</div>
</div>

### DROK 2A LM2596 with LED

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: DROK LM2596 with LED][git_drok_2A]{ .md-button }

[:material-cart: Product Link][bom_drok_2A]{ .md-button }

- Materials: 4x M3 x 6mm
- Hole Pattern: 60.5mm x 30.5mm
- Tray:
    - Short (single)
    - Long (single, dual)
</div>
<div markdown class="jh-grid-img">
[![product picture][img_led_lm2596]][img_led_lm2596]
</div>
</div>

### HiLetGo 2A LM2596 with LED

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: HiLetGo LM2596 with LED][git_hiletgo_2A]{ .md-button }

[:material-cart: Product Link][bom_hiletgo_2A]{ .md-button }

- Materials: 4x M3 x 6mm
- Hole Pattern: 49.5mm x 27.5mm 
- Trays:
    - Short (single)
    - Long (single, dual)
</div>
<div markdown class="jh-grid-img">
[![product picture][img_hiletgo_2a]][img_hiletgo_2a]
</div>
</div>

### DROK 3A LM2596 with LED

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: DROK 3A LM2596 with LED][git_drok_3A]{ .md-button }

[:material-cart: Product Link][bom_drok_3A]{ .md-button }

- Materials: 4x M3 x 6mm
- Hole Pattern: 52.5mm x 28.75mm
- Trays:
    - Short (single)
</div>
<div markdown class="jh-grid-img">
[![product picture][img_drok_3a]][img_drok_3a]
</div>
</div>

### DROK 5A Buck with LED

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: DROK 5A Buck with LED][git_drok_5A]{ .md-button }

[:material-cart: Product Link][bom_drok_5A]{ .md-button }

- Materials: 4x M3 x 6mm
- Hole Pattern: 63mm x 40.5mm
- Trays: 
    - Long (single)
</div>
<div markdown class="jh-grid-img">
[![product picture][img_drok_5a]][img_drok_5a]
</div>
</div>

## MOSFETs

### Creality MOSFET 

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Creality MOSFET][git_creality_mosfet]{ .md-button }

[:material-cart: Product Link][bom_creality_mosfet]{ .md-button }

- Materials: 2x M3 x 6mm
- Trays:
    - Short (single)
    - Long (single)
</div>
<div markdown class="jh-grid-img">
[![product picture][img_creality_mosfet]][img_creality_mosfet]
</div>
</div>

## Solid State Relays

### Omron G3A/G3NA Puck Relays

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
!!! caution "Fit Test Pending"

[:material-git: 48mm SSR][git_48mm_ssr]{ .md-button }

[:material-cart: Product Link][bom_omron_ssr]{ .md-button }

- Materials: 2x M4 x 6mm
- Trays:
    - Short (single)
    - Long (single)
- Notes: 
    - Mounting holes distance is 47.5mm to about 52mm.
    - Long tray has zip tie anchors. 
</div>
<div markdown class="jh-grid-img">
[![product picture][img_omron_ssr]][img_omron_ssr]
</div>
</div>

### Fotek SSR-40 DA 

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Fotek SSR-40 DA][git_fotek_ssr40da]{ .md-button }

[:material-cart: Product Link][bom_fotek_ssr_40da]{ .md-button }

- Materials: 2x M4 x 6mm
- Trays:
    - Short (single)
    - Long (single)
- Notes: 
    - Mounting holes distance is 47mm to about 52mm.
    - Long tray has zip tie anchors.
</div>
<div markdown class="jh-grid-img">
[![product picture][img_fotek_ssr_40da]][img_fotek_ssr_40da]
</div>
</div>

## Other Products

### BIGTREETECH UPS 24V 1.0 

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
!!! caution "Fit Test Pending [:material-git: Issue #24](https://github.com/jon-harper/OmniBox/issues/24)"

[:material-git: BTT UPS 24V 1.0][git_btt_ups_24v]{ .md-button }

[:material-cart: Product Link][bom_btt_ups_24v]{ .md-button }

- Mounting: 4x M3 x 6mm
- Trays:
    - Short (single)
</div>
<div markdown class="jh-grid-img">
[![product picture][img_btt_ups_24v]][img_btt_ups_24v]
</div>
</div>

### BIGTREETECH Relay 1.2

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: BTT Relay 1.2][git_btt_relay_1.2]{ .md-button }

[:material-cart: Product Link][bom_btt_relay_1.2]{ .md-button }

- Mounting: 4x M3 x 6mm
- Trays:
    - Long (single)
</div>
<div markdown class="jh-grid-img">
[![product picture][img_btt_relay]][img_btt_relay]
</div>
</div>

### Wago 221 Lever Nuts 

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Wago Lever Nuts][git_wago_221]{ .md-button }

[:material-cart: Product Link][bom_wago_nuts]{ .md-button }

- Notes: 
    - Support for 3 position & 5 position
    - No mounting hardware; snap-in
- Trays:
    - Short, 4x 3 position
    - Long, 4x 5 position
    - Long, 4x 5 position, 2x 3 position
</div>
<div markdown class="jh-grid-img">
[![product picture][img_wago_nuts]][img_wago_nuts]
</div>
</div>

### 4010/4020 Fans 

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: 40mm Fan][git_tray_4010]{ .md-button }

[:material-cart: Product Link][bom_4010]{ .md-button }

- Materials: 4x M3
- Notes:
    - Screw length depends on mounting direction and thickness of the fan.
    - Also available on long trays for buck converters.
- Trays:
    - Short (single)
</div>
<div markdown class="jh-grid-img">
[![product picture][img_4010]][img_4010]
</div>
</div>

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
[img_btt_relay]: ../img/parts/btt_relay_1.2.jpg
[img_omron_ssr]: ../img/parts/omron_ssr.jpg