---
title: Display Panel
summary: Instructions for assembling and installing the display panel.
authors: Jon Harper
date: 2022-10-29
steps:
  display:
    - txt: |
        1) Remove the display knob. It should come off a firm pull.
      img: ../img/assembly/panels/display1.webp
      img_txt: Remove the knob.
    - txt: |
        2) Fit the LCD into the display panel.
      img: ../img/assembly/panels/display2.webp
      img_txt: Position the LCD.
    - txt: |
        3) Attach the LCD to the panel with four (4) M4 x 6mm screws.
      img: ../img/assembly/panels/display3.webp
      img_txt: Attach the display to the panel.
    - txt: |
        4) If you have a printed knob, push it back in place of the original. Otherwise, replace the original knob.
      img: ../img/assembly/panels/display4.webp
      img_txt: Replace the knob.
    - txt: |
        5) Set the assembly into the display mount on the front main body.
      img: ../img/assembly/panels/display5.webp
      img_txt: Position the display assembly.
    - txt: |
        6) Stock: Attach the display with four (4) screws.
        <br>HSI: M3 x 8mm
        <br>Stock: M3 x 10mm
      img: ../img/assembly/panels/display6.webp
      img_txt: Secure the display panel.
---

{% import 'assembly.md' as assy %}

This section covers assembling a generic 12864 display panel, like the kind commonly found on Sovol and older Creality Ender-series printers.

Some displays have an extra step of mounting the display to a cover. The cover then attaches to the panel. Other than this, the installation process remains the same.

{{ assy.overview_video(meta.video_folder + 'display.mp4') }}

## Materials

=== "As Illustrated (HSI)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS             | 4   |                                 |
    | M3 x 8mm SHCS             | 4   | May substitute 10 or 12mm.      |
    | Generic 128x64 Display    | 1   |                                 |
    | :material-printer-3d-nozzle: `Display Panel - Generic 12864.stl` | 1   |   |
    | :material-printer-3d-nozzle: `Display Knob.stl` | 1   |  Optional. |

=== "As Illustrated (Stock)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS             | 4   |                                 |
    | M3 x 10mm SHCS            | 4   | May substitute 12mm.      |
    | Generic 128x64 Display    | 1   | Comes with older Creality printers. |
    | :material-printer-3d-nozzle: `Display Panel - Generic 12864.stl` | 1   |   |
    | :material-printer-3d-nozzle: `Display Knob.stl` | 1   |  Optional. |

=== "Blank Panel (HSI)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm SHCS             | 4   |                                 |
    | :material-printer-3d-nozzle: `Display Panel - Blank V3.stl` | 1   |   |

=== "Blank Panel (Stock)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 10mm SHCS            | 4   | May substitute 12mm.            |
    | :material-printer-3d-nozzle: `Display Panel - Blank V3.stl` | 1   |   |

## Directions

{{ assy.render_steps(steps.display, '480px') }}

## Reference

[![illustration][display_final]][display_final]

[display_final]: ../img/assembly/panels/display_final.webp