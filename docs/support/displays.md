---
title: Displays
summary: List of displays with compatible OmniBox mounts.
authors: Jon Harper
date: 2022-07-22
---

Display Panels mount two different types of display screens:

- MCU displays include various TFT and older 128x64 character LCD diplays.
- Raspberry Pi displays are TFT displays, usually used with OctoPrint or Klipper.

## MCU Displays

<figure markdown>
  [![front left render][img_display]{ width="480" }][img_display]
  <figcaption>12864 TFT display mounted on a panel.</figcaption>
</figure>

Each supported MCU display screen has a subfolder in the [:material-git: `/Panels/Display`][git_display] git folder. There is an optional STL file for a [:material-git: replacement display knob][git_display_knob], as well.

Component names below link to the corresponding git folder. Most mounts require four (4) 6mm M3 screws to fasten the display in place. Some mounts have two or three pieces and require additional materials.

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

 
### Generic 12864 Display

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Generic 12864][git_generic_12864]{ .md-button }

[:material-cart: Product Link][bom_generic_12864]{ .md-button }

- Materials: 4x M3 x 6mm
- Notes: 
    - Also known as Creality CR-10 stock display in Marlin.
    - Common on many older i3-style and Creality printers.
</div>
<div markdown class="jh-grid-img">
[![product picture][img_12864]][img_12864]
</div>
</div>

### FYSETC Mini 12864

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Mini 12864][git_mini_12864]{ .md-button }

[:material-cart: Product Link][bom_mini_12864]{ .md-button }

- Materials: 
    - 4x M3 x 6mm
    - 4x M3 x 20mm
- Notes: This includes BIGTREETECH brand and other clones.
</div>
<div markdown class="jh-grid-img">
[![product picture][img_mini12864]][img_mini12864]
</div>
</div>

### BIGTREETECH 2.4" TFT

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: BTT 2.4 TFT][git_btt_tft_24]{ .md-button }

- Materials: 
    - 4x M3 x 6mm
    - 4x M3 x 8mm
- Notes: This product is discontinued.
</div>
<div markdown class="jh-grid-img">
[![product picture][img_btt_tft24]][img_btt_tft24]
</div>
</div>

### BIGTREETECH 3.5" TFT

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: BTT 3.5 TFT][git_btt_tft_35]{ .md-button }

[:material-cart: Product Link][bom_btt_tft35]{ .md-button }

- Materials: 
    - 4x M3 x 6mm
    - 4x M3 x 8mm
- Notes: This is not the E3 version, which uses the [Generic 12864](#generic-12864-display) display mount. 
</div>
<div markdown class="jh-grid-img">
[![product picture][img_btt_tft35]][img_btt_tft35]
</div>
</div>

### BIGTREETECH 3.5" TFT E3

{{ issue_tag(115) }}

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: BTT 3.5 TFT E3][git_btt_tft_35_e3]{ .md-button }

[:material-cart: Product Link][bom_btt_tft35_e3]{ .md-button }

- Materials: 4x M3 x 6mm
- Notes: *Not* compatible with the generic 12864 mount.

</div>
<div markdown class="jh-grid-img">
[![product picture][img_btt_tft35_e3]][img_btt_tft35_e3]
</div>
</div>

### BIGTREETECH HDMI5

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
!!! info "Contributed by [SirUli][contrib_siruli]"

[:material-git: BTT HDMI5][git_btt_hdmi5]{ .md-button }

[:material-cart: Product Link][bom_btt_hdmi5]{ .md-button }

- Materials:
  - 4x M3 x 15mm
  - 4x M3 x 6mm

</div>
<div markdown class="jh-grid-img">
[![product picture][img_btt_hdmi5]][img_btt_hdmi5]
</div>
</div>

## CPU Displays

Many Klipper and Octoprint users have a CPU display attached to their Raspberry Pi (or other SBC), and some forego an MCU display entirely.

Any TFT designed with mounts points for a Raspberry Pi on the back should be compatible with OmniBox. These can all be mounted on short lids; some can be mounted as display panels. Users have also contributed additional display panel designs for specific TFT models.

=== "On a Short Lid"
    <figure markdown>
    ![display panel tft](../img/components/rpi_tft_lid.png){width="360px"}
    <figcaption markdown>Displays up to 7" can be attached to the lid.</figcaption>
    </figure>
=== "On a Display Panel"
    <figure markdown>
    ![display panel tft](../img/components/rpi_tft_display.png){width="360px"}
    <figcaption markdown>Although any display can be mounted to the panel, 7-inch displays block the mounting holes.</figcaption>
    </figure>
=== "As a Flush-Mount Display Panel"
    <figure markdown>
    ![display panel tft](../img/components/rpi_tft_display_flush.png){width="360px"}
    <figcaption markdown>Flush-mount panels are available for certain models. Illustrated is [MaffooClock][contrib_maffooclock]'s panel for the BIGTREETECH PITFT50.</figcaption>
    </figure>

Known compatible displays are listed below, along with mounting options.

| Display / Mounting Location | Display Panel      | Lid                | Custom Display Panel |
|-----------------------------|:------------------:|:------------------:|:--------------------:|
| BIGTREETECH PI TFT43        | :white_check_mark: | :white_check_mark: | :x:                  |
| BIGTREETECH PI TFT50        | :white_check_mark: | :white_check_mark: | :white_check_mark:   |
| BIGTREETECH PI TFT70        | :x:                | :white_check_mark: | :x:                  |
| Raspberry Pi 7" TFT         | :x:                | :white_check_mark: | :white_check_mark:   |

### Universal Short Lid

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

!!! note "Note: Use the XL file for 7-inch TFTs"

[:material-git: Pi TFT][git_lid_pi_tft]{ .md-button }

- Materials:
    - 4x M2.5 screws
    - 4x M2.5 brass standoffs (10-12mm)
- Notes:
    - The Raspberry Pi 7" TFT may not come with the necessary standoffs.
    - Materials are included with all models of the BIGTREETECH PITFT.
</div>
<div markdown class="jh-grid-img">
![lid tft](../img/components/rpi_tft_lid.png){width="360px"}
</div>
</div>

### Universal Display Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Rasperry Pi TFT][git_display_pi_tft]{ .md-button }

- Materials:
    - 4x M2.5 screws
    - 4x M2.5 brass standoffs (10-12mm)
- Notes:
    - The Raspberry Pi 7" TFT may not come with the necessary standoffs.
    - Materials are included with all models of the BIGTREETECH PITFT.

</div>
<div markdown class="jh-grid-img">
![display panel tft](../img/components/rpi_tft_display.png){width="360px"}
</div>
</div>

### BIGTREETECH 5" Pi TFT

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
!!! info "Contributed by [MaffooClock][contrib_maffooclock]"

[:material-git: BTT PI TFT50][git_btt_pitft_50]{ .md-button }

[:material-cart: Product Link][bom_btt_pitft50]{ .md-button }

- Materials:
    - 8x M2.5 x 6mm screws
    - 4x M3 x 6mm screws
    - *(HSI version)* 4x M3 5mm OD x 4mm heat set inserts

</div>
<div markdown class="jh-grid-img">
[![product picture][img_btt_pitft50]][img_btt_pitft50]
</div>
</div>

### Raspberry Pi 7" TFT

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
!!! info "Contributed by [Anton Chebotaev][contrib_anton]"

[:material-git: Raspberry Pi Touchscreen][git_rpi_tft]{ .md-button }

[:material-cart: Product Link][bom_btt_pitft50]{ .md-button }

- Materials:
    - 4x M3 x 8mm screws **or**
    - 4x M3 x 16mm screws

</div>
<div markdown class="jh-grid-img">
[![product picture][img_rpi_tft]][img_rpi_tft]
</div>
</div>


[img_display]: ../img/components/display.webp
[img_btt_tft35_e3]: ../img/parts/btt_35tft_e3.webp
[img_12864]: ../img/parts/classic_12864.webp
[img_mini12864]: ../img/parts/mini12864.webp
[img_btt_tft24]: ../img/parts/btt_tft_2.4.webp
[img_btt_tft35]: ../img/parts/btt_tft_3.5.webp
[img_btt_pitft50]: ../img/parts/btt_pitft_5.0.webp
[img_btt_hdmi5]: ../img/parts/btt_hdmi5.webp
[img_rpi_tft]: ../img/parts/rpi_tft.webp