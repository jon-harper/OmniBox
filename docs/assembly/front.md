---
title: Front Panel
summary: Assembling the front panel.
authors: Jon Harper
date: 2024-02-29
steps:
  front:
    - txt: |
        1) Carefully pry open the outer plastic shell around the MicroSD card reader extension. Discard the shell.
      img: todo
      img_txt: Pry open the MicroSD extension.
    - txt: |
        2) (Not pictured) Place the MicroSD extension PCB in the holder body. The ribbon cable should be flush with the lip on the back of the holder.
      img: todo
      img_txt: Position the SD card extension in the holder.
    - txt: |
        3) Place the holder cap on top of the extension and holder body.
      img: todo
      img_txt: Put the cap on the holder.
    - txt: | 
        4) Use two M3 x 6mm screws to fasten the cap in place.
      img: todo
      img_txt: Fasten the cap.
    - txt: |
        5) Slot the SD card assembly into the front panel and secure with two (2) M3 x 6mm screws. Vertical orientation does not matter.
      img: todo
      img_txt: Install the extension to the front panel.
    - txt: |
        6) Push the front panel into place on the case body. Slip the SD card extension cable through first.
      img: todo
      img_txt: Position the front panel.
    - txt: |
        7) HSI: Attach the panel with two (2) M3 x 8mm screws.<br>Stock: Attach the panel with two (2) M3 x 10mm screws.
      img: todo
      img_txt: Secure the panel.
---

{% import 'assembly.md' as assy %}

{{ assy.overview_video(meta.video_folder + 'front.mp4') }}

## Materials

=== "As Illustrated (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS             | 4   |                                 |
    | M3 x 8mm SHCS             | 2   |                                 |
    | :material-printer-3d-nozzle: `Front Panel - MicroSD, Slats.stl`   | 1 |  |
    | :material-printer-3d-nozzle: `MicroSD Extension Holder Body.stl`  | 1 |  |
    | :material-printer-3d-nozzle: `MicroSD Extension Holder Cap.stl`   | 1 |  |
=== "As Illustrated (Stock)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS             | 4   |                                 |
    | M3 x 10mm SHCS            | 2   | May substitute 12mm or longer.  |
    | :material-printer-3d-nozzle: `Front Panel - MicroSD, Slats.stl`   | 1 |  |
    | :material-printer-3d-nozzle: `MicroSD Extension Holder Body.stl`  | 1 |  |
    | :material-printer-3d-nozzle: `MicroSD Extension Holder Cap.stl`   | 1 |  |
=== "Blank Panel (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm SHCS             | 2   |     |
    | :material-printer-3d-nozzle: Front Panel - Blank.stl | 1 |  |
=== "Blank Panel (Stock)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 10mm SHCS            | 2   | May substitute 12mm.            |
    | :material-printer-3d-nozzle: Front Panel - Blank.stl | 1 |  |

!!! note "Note: LED Backing Panel"
    If are installing the LED backer, substitute M3 x 16mm for the two (2) longer screws.

## Directions

{{ assy.render_steps(steps.front, '480px') }}

## Reference

[![illustration][front_final]][front_final]
