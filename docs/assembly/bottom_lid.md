---
title: Bottom Panel & Lid
summary: Final steps to close up the printer.
authors: Jon Harper
date: 2022-11-15
steps:
  bottom:
    - txt: |
        1) Set the front bottom panel in the recess in the base.
      img: ../img/assembly/panels/bottom1.webp
      img_txt: Align the front panel with the base.
    - txt: |
        2) Use four (4) screws to attach the panel.<br>HSI: M3 x 6mm<br>Stock: M3 x 8mm
      img: ../img/assembly/panels/bottom2.webp
      img_txt: Attach the front panel.
    - txt: |
        3. Use the same procedure for the rear bottom panel with four (4) more screws.
      img: ../img/assembly/panels/bottom3.webp
      img_txt: Attach the rear panel.
  top:
    - txt: |
        1) Place the handle over the screw holes in the center of the carry handle lid.
      img: ../img/assembly/panels/lid1.webp
      img_txt: Position the handle.
    - txt: |
        2) Flip the lid over and fasten the handle in place with two (2) M3 x 8mm screws.
      img: ../img/assembly/panels/lid2.webp
      img_txt: Secure the handle.
    - txt: |
        3) Place the assembled carry handle lid on top of the case. The lid is reversible.
      img: ../img/assembly/panels/lid3.webp
      img_txt: Position the carry handle lid.
    - txt: |
        4) Use four (4) screws to attach the lid.<br>
        HSI: M3 x 6mm
        Stock: M3 x 8mm
      img: ../img/assembly/panels/lid4.webp
      img_txt: Secure with screws.
    - txt: |
        5) Position and install the the vent lid with four (4) screws.
        HSI: M3 x 6mm
        Stock: M3 x 8mm
      img: ../img/assembly/panels/lid5.webp
      img_txt: Install the second lid.
---

{% import 'assembly.md' as assy %}

This page contains the last two sections of the build. Here we close up the bottom and top of the case.

All wiring should be completed before proceeding.

## Bottom Panel

The example below uses a front and rear bottom panel. The procedure for installing a unified bottom panel is effectively the same uses the
the same fasteners.

{{ assy.overview_video(meta.video_folder + 'bottom.mp4') }}

### Materials

=== "As Illustrated (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS   | 8   |                                 |
    | :material-printer-3d-nozzle: `Bottom Panel V3 - Hexagons Front.stl` | 1 | |
    | :material-printer-3d-nozzle: `Bottom Panel V3 - Hexagons Rear.stl` | 1  | |
    

=== "As Illustrated (Stock)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm SHCS   | 8   | May substitute 10mm or 12mm.    |
    | :material-printer-3d-nozzle: `Bottom Panel V3 - Hexagons Front.stl` | 1 | |
    | :material-printer-3d-nozzle: `Bottom Panel V3 - Hexagons Rear.stl` | 1  | |

### Directions

{{ assy.render_steps(steps.bottom, '480px') }}

### Reference

[![illustration][bottom_final]{width="640px"}][bottom_final]

## Lid(s)

The example below uses two short lids. The procedure for installing a single, long lid is effectively the same and requires no additional fasteners.

{{ assy.overview_video(meta.video_folder + 'lid.mp4') }}

### Materials

=== "As Illustrated (HSI)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS   | 10  |                                 |
    | :material-printer-3d-nozzle: Lid - Short Vent.stl | 1 |    |
    | :material-printer-3d-nozzle: Half Carry Lid.stl | 1 |    |
    | :material-printer-3d-nozzle: Carry Handle - HSI.stl | 1 |    |

=== "As Illustrated (Stock)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm SHCS   | 10  |                                 |
    | :material-printer-3d-nozzle: Lid - Short Vent.stl | 1 |    |
    | :material-printer-3d-nozzle: Half Carry Lid.stl | 1 |    |
    | :material-printer-3d-nozzle: Carry Handle - HSI.stl | 1 |    |

### Directions

{{ assy.render_steps(steps.top, '480px') }}                                           

### Reference

[![illustration][lid_final]{width="640px"}][lid_final]

<div align="center" markdown>
# :material-check: That's it!

You've assembled an OmniBox! Congratulations!

![logo][logo]
</div>

[lid_final]: ../img/assembly/final.webp
[bottom_final]: ../img/assembly/panels/bottom_final.webp
[logo]: ../img/favicon.png
