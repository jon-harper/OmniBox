---
title: Lower Bay Components
summary: A complete list of parts supported by OmniBox
authors: Jon Harper
date: 2022-07-22
---

Lower Bay Trays may be Short or Long. A Long tray covers the mount points of two Short trays and must be mounted from side-to-side in the case.

The [:material-git: `/Trays/Lower Bay`][git_lower_bay] git folder is organized with subfolders for each supported part. All variations based around that part are in the same folder. 

Every tray (short or long) attaches to the Core case body with four (4) M3 x 6mm screws. Additional materials are listed with each part.

<figure markdown>
  [![img][img_lower_bay]{ width="480" }][img_lower_bay]
  <figcaption>Up to three (3) Long trays will fit in a case, or six (6) Short trays.</figcaption>
</figure>

<!-- Template 
<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: ][git_]{ .md-button }

[:material-cart: Product Link][bom_]{ .md-button }

- Mounting:
- Trays:
</div>
<div markdown class="jh-grid-para">
[![product picture][img_]][img_]
</div>
</div>
-->

## Buck Converters

Long trays for step-down ("buck") converters often have a 40mm fan mount for additional cooling.

The LM2596 step down is rated to 3A **with a heatsink**, enough to power a Raspberry Pi 4B. Most LM2596-based buck converters are sold without heatsinks and are listed as capable of 2A. Stepping down from 24V to 5V generates additional heat; consider purchasing a buck converter [with a heat sink][bom_basic_lm2596] or [add one][bom_lm2596_heatsink].

### Basic LM2596

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_basic_lm2596]{ .md-button }

**Materials:** 2x M3 x 6mm

**Notes:** This converter requires a heat sink to safely output 3A.

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-x-24:{.jh-red} No |
| Short | 2 | :octicons-x-24:{.jh-red} No |
| Long  | 1 | :octicons-check-24:{.jh-green} Yes |
| Long  | 2 | :octicons-x-24:{.jh-red} No |
| Long  | 2 | :octicons-check-24:{.jh-green} Yes |

</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_basic_lm2596]{ .md-button }

[![product picture][img_basic_lm2596]][img_basic_lm2596]
</div>
</div>

### DROK 2A LM2596 with LED

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_drok_2A]{ .md-button }

**Materials:** 4x M3 x 6mm

**Hole Pattern:** 60.5mm x 30.5mm

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-x-24:{.jh-red} No |
| Long  | 1 | :octicons-check-24:{.jh-green} Yes |
| Long  | 2 | :octicons-x-24:{.jh-red} No |
| Long  | 2 | :octicons-check-24:{.jh-green} Yes |

</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_drok_2A]{ .md-button }

[![product picture][img_led_lm2596]][img_led_lm2596]
</div>
</div>

### HiLetGo 2A LM2596 with LED

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: HiLetGo LM2596 with LED][git_hiletgo_2A]{ .md-button }

**Materials:** 4x M3 x 6mm

**Hole Pattern:** 49.5mm x 27.5mm 

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-x-24:{.jh-red} No |
| Long  | 1 | :octicons-check-24:{.jh-green} Yes |
| Long  | 2 | :octicons-x-24:{.jh-red} No |
| Long  | 2 | :octicons-check-24:{.jh-green} Yes |
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_hiletgo_2A]{ .md-button }

[![product picture][img_hiletgo_2a]][img_hiletgo_2a]
</div>
</div>

### DROK 3A LM2596 with LED

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_drok_3A]{ .md-button }

**Materials:** 4x M3 x 6mm

**Hole Pattern:** 52.5mm x 28.75mm

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-x-24:{.jh-red} No |
| Long  | 1 | :octicons-check-24:{.jh-green} Yes |
| Long  | 2 | :octicons-x-24:{.jh-red} No |
| Long  | 2 | :octicons-check-24:{.jh-green} Yes |

</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_drok_3A]{ .md-button }

[![product picture][img_drok_3a]][img_drok_3a]
</div>
</div>

### DROK 5A Buck with LED

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_drok_5A]{ .md-button }

**Materials:** 4x M3 x 6mm

**Hole Pattern:** 63mm x 40.5mm

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Long  | 1 | :octicons-x-24:{.jh-red} No |

</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_drok_5A]{ .md-button }

[![product picture][img_drok_5a]][img_drok_5a]
</div>
</div>

## MOSFETs

### Creality MOSFET 

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Creality MOSFET][git_creality_mosfet]{ .md-button }

**Materials:** 2x M3 x 6mm

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-x-24:{.jh-red} No |
| Long  | 1 | :octicons-x-24:{.jh-red} No |
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_creality_mosfet]{ .md-button }

[![product picture][img_creality_mosfet]][img_creality_mosfet]
</div>
</div>

## Solid State Relays

### Omron G3A/G3NA Puck Relays

!!! caution "Fit Test Pending"

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Files][git_48mm_ssr]{ .md-button }

**Materials:** 2x M4 x 6mm

**Hole Pattern:** Tray holes are 48mm apart.

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-x-24:{.jh-red} No |
| Long  | 1 | :octicons-x-24:{.jh-red} No |

</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_omron_ssr]{ .md-button }

[![product picture][img_omron_ssr]][img_omron_ssr]
</div>
</div>

### Fotek SSR-40 DA 

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_fotek_ssr40da]{ .md-button }

**Materials:** 2x M4 x 6mm

**Notes:**

- Mounting holes distance is 47mm to about 52mm.
- Long tray has zip tie anchors.

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-x-24:{.jh-red} No |
| Long  | 1 | :octicons-x-24:{.jh-red} No |
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_fotek_ssr_40da]{ .md-button }

[![product picture][img_fotek_ssr_40da]][img_fotek_ssr_40da]
</div>
</div>

## CAN Adapters

### BIGTREETECH U2C

!!! info "Contributed by [edgy][contrib_edgy]"

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:octicons-link-external-24: Files][src_btt_u2c]{ .md-button }

**Materials:** 4x M3 x 6mm *BHCS*

**Notes:** 

- Socket head screws are too large for the screw terminals.
- See the [Printables][src_btt_u2c] page for more details.

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-x-24:{.jh-red} No |
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_btt_u2c]{ .md-button }

[![product picture][img_btt_u2c]][img_btt_u2c]
</div>
</div>

## Other Products

### BIGTREETECH UPS 24V 1.0 

!!! caution "Fit Test Pending [:material-git: Issue #24](https://github.com/jon-harper/OmniBox/issues/24)"

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Files][git_btt_ups_24v]{ .md-button }

**Materials:** 4x M3 x 6mm

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-x-24:{.jh-red} No |
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_btt_ups_24v]{ .md-button }

[![product picture][img_btt_ups_24v]][img_btt_ups_24v]
</div>
</div>

### BIGTREETECH Relay 1.2

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: BTT Relay 1.2][git_btt_relay_1.2]{ .md-button }

**Materials:** 4x M3 x 6mm

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Long  | 1 | :octicons-x-24:{.jh-red} No |
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_btt_relay_1.2]{ .md-button }

[![product picture][img_btt_relay]][img_btt_relay]
</div>
</div>

### Wago 221 Lever Nuts 

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_wago_221]{ .md-button }

**Materials:** None, snap-in

**Trays**

| Length | 3 Position | 5 Position |
|--------|------------|------------|
| Short  | 4          | 0          |
| Long   | 0          | 4          |
| Long   | 2          | 4          |

</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_wago_nuts]{ .md-button }

[![product picture][img_wago_nuts]][img_wago_nuts]
</div>
</div>

### 4010/4020 Fans 

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_tray_4010]{ .md-button }

**Materials:** 4x M3

**Notes:** Screw length depends on mounting direction and thickness of the fan.

**Trays**

| Length | Qty Mounted | 40mm Fan |
|-------|---|---|
| Short | 1 | :octicons-check-24:{.jh-green} Yes |
    
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_4010]{ .md-button }

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
[img_btt_u2c]: ../img/parts/btt_u2c.webp