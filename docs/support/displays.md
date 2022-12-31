---
title: Displays
summary: List of displays with compatible OmniBox mounts.
authors: Jon Harper
date: 2022-07-22
---

Display Panels mount two different types of display screens:

- MCU displays include various TFT and older 128x64 character LCD diplays.
- Raspberry Pi displays are TFT displays, usually used with OctoPrint or Klipper.

It is impotant to note that displays larger than 6" are too large for the panel and should be lid-mounted. 7" Raspberry Pi TFTs are an example.

## MCU Displays

<figure markdown>
  [![front left render][img_display]{ width="480" }][img_display]
  <figcaption>12864 TFT display mounted on a panel.</figcaption>
</figure>

Each supported MCU display screen has a subfolder in the [:material-git: `/Panels/Display`][git_display] git folder. There is an optional STL file for a [:material-git: replacement display knob][git_display_knob], as well.

Component names below link to the corresponding git folder. Most mounts require four (4) 6mm or M3 screws to fasten the display in place. Some mounts have two or three pieces and require additional screws.

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
    - Also known as Creality CR-10 stock display; comes on most Creality printers.
    - Called RepRap Discount Smart Controller in Marlin.
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
- Notes: This product is discontinued, but I still use it, so there's a part.
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
- Notes: This is not the E3 version, which uses the Generic 12864 mount. 
</div>
<div markdown class="jh-grid-img">
[![product picture][img_btt_tft35]][img_btt_tft35]
</div>
</div>

### BIGTREETECH 3.5" TFT E3

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Generic 12864][git_generic_12864]{ .md-button }

[:material-cart: Product Link][bom_btt_tft35_e3]{ .md-button }

- Materials: 4x M3 x 6mm
- Notes: Uses the Generic 12864 mount.

</div>
<div markdown class="jh-grid-img">
[![product picture][img_btt_tft35_e3]][img_btt_tft35_e3]
</div>
</div>

<!-- ### BIGTREETECH TFT5

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
!!! caution "Fit Test Pending"
    [:material-git: Issue #24](https://github.com/jon-harper/OmniBox/issues/24)

[:material-git: Files: ][git_btt_tft_50]{ .md-button }

[:material-cart: Product Link][bom_]{ .md-button }

- Materials: 4x M3
</div>
<div markdown class="jh-grid-img">
[![product picture][img_]][img_]
</div>
</div>
-->

## Raspberry Pi Displays

Any TFT designed with mounts points for a Raspberry Pi on the back should be compatible with OmniBox.

These displays can be attached in one of two ways:

- In place of the MCU display as a Display Panel
- Or as a [:material-git: Lid][git_lid_pi_tft] above the MCU display mount. 

Compatibility with the *display panel* depends on size:

| Display / Mounting Location | Display Panel      | Lid                |
|-----------------------------|:------------------:|:------------------:|
| BIGTREETECH PI TFT43        | :white_check_mark: | :white_check_mark: |
| BIGTREETECH PI TFT50        | :white_check_mark: | :white_check_mark: |
| BIGTREETECH PI TFT70        | :x:                | :white_check_mark: |
| Raspberry Pi 7" TFT         | :x:                | :white_check_mark: |

### Materials

Official Raspberry Pi 7" TFT require additional M2.5 10-12mm standoffs. They should come with M2.5 screws.

BIGTREETECH Pi TFT displays come with the necessary standoffs and screws.


[img_display]: ../img/components/display.png
[img_btt_tft35_e3]: ../img/parts/btt_35tft_e3.jpg
[img_12864]: ../img/parts/classic_12864.jpg
[img_mini12864]: ../img/parts/mini12864.jpg
[img_btt_tft24]: ../img/parts/btt_tft_2.4.jpg
[img_btt_tft35]: ../img/parts/btt_tft_3.5.jpg