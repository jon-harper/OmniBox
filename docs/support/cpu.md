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

If you do not use an SBC, the side of the bay can be used as a [Side Panel][panel_mounts].

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

### Universal Mount

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Raspberry Pi Universal][git_rpi_universal]{ .md-button }

- Materials: 4x M3 x 6mm
- Note: This tray should be compatible with *any* board using the Raspberry Pi mounting hole pattern.
</div>
<!-- <div markdown class="jh-grid-img">
</div> -->
</div>



[cpu]: ../img/components/cpu.png
[img_rpi_3b]: ../img/parts/rpi_3b_plus.jpg
[img_rpi_4b]: ../img/parts/rpi_4b.jpg
[panel_mounts]: panel_mounts.md