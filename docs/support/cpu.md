---
title: SoC CPUs/SBCs
summary: List of SoC CPUs supported by OmniBox
authors: Jon Harper
date: 2022-07-22
---

This page lists system-on-a-chip (SoC) CPUs currently compatible with OmniBox. These are commonly known as single board computers (SBC).

<figure markdown>
  [![front left render][cpu]{ width="480" }][cpu]
  <figcaption>CPU trays can be mounted on the left or right side of the case.</figcaption>
</figure>

CPU Trays are in the [:material-git: `/Trays/CPU`][git_cpu] git folder; each component has its own subfolder. Currently, SBCs other than the Raspberry Pi are not supported.

The Raspberry Pi model-specific trays mount with the SBC's USB and Ethernet cables facing *outward* (as panel mounts). If you are using Klipper, this will require an external cable running to your MCU; instead, use the [Universal Mount](#universal-mount).

If you do not use an SBC, the side of the CPU bay can be used as a [Side Panel][panel_mounts].

<!-- Template
<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_]{ .md-button }

[:material-cart: Product Link][bom_]{ .md-button }

- Materials:
- Notes:
</div>
<div markdown class="jh-grid-img">
[![product picture][img_]][img_]
</div>
</div>
 -->


## Raspberry Pi

### Raspberry Pi 3B+

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Raspberry Pi 3B Plus][git_rpi_3b_plus]{ .md-button }

[:material-cart: Product Link][bom_rpi_3b_plus]{ .md-button }

Materials: 4x M3 x 6mm

</div>
<div markdown class="jh-grid-img">
[![product picture][img_rpi_3b]][img_rpi_3b]
</div>
</div>

### Raspberry Pi 4B

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Raspberry Pi 4B][git_rpi_4b]{ .md-button }

[:material-cart: Product Link][bom_rpi_4b]{ .md-button }

Materials: 4x M3 x 6mm

</div>
<div markdown class="jh-grid-img">
[![product picture][img_rpi_4b]][img_rpi_4b]
</div>
</div>

## Universal Mount

This tray has the Raspberry Pi mounting hole pattern and is compatible with clones (e.g., Orange Pi, Banana Pi) that use the same hole pattern and PCB dimensions.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Raspberry Pi Universal][git_rpi_universal]{ .md-button }

- Materials:
    - 4x M3 x 6mm
    - *(optional)* [:material-cart: 40mm 5V fan][bom_4010_5V]
    - *(optional)* 4x M3 x 14-16mm
- Note: This tray should be compatible with *any* board using the Raspberry Pi mounting hole pattern.
</div>
<!-- <div markdown class="jh-grid-img">
</div> -->
</div>



[cpu]: ../img/components/cpu.webp
[img_rpi_3b]: ../img/parts/rpi_3b_plus.webp
[img_rpi_4b]: ../img/parts/rpi_4b.webp
[panel_mounts]: panel_mounts.md