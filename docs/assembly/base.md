---
title: Base and PSU
summary: Instructions for assembling the base and PSU tray.
authors: Jon Harper
date: 2024-02-27
steps:
  halves:
    - txt: |
        1) Align the angled center screw holes of the front and rear halves as illustrated, then 
        press them together.
      img: ../img/assembly/core/base1.webp
      img_txt: Align the screw holes
    - txt: |
        2) Insert four (4) M3 x 12mm screws in the angled holes in the top of the Rear half and
        fasten them to the front half.<br>
        Double-check that the parts are aligned before fully tightening the screws.
      img: ../img/assembly/core/base2.webp
      img_txt: Install the center screws
  base_prep:
    - txt: |
        1) Insert the rocker switch into the Power Switch Protector. The flaps on the side compress and snap the switch in place once inserted.
      img: ../img/assembly/core/power1.webp
      img_txt: Join rocker switch to protector.
    - txt: |
        2) Slide the rocker switch and protector into the open slot on the front base. It should pop into place.
      img: ../img/assembly/core/power2.webp
      img_txt: Install the rocker switch.
    - txt: |
        3) Remove the fuse cover by sliding it out. If a fuse is inserted in the fuse holder, remove it.
      img: ../img/assembly/core/power3.webp
      img_txt: Remove the fuse cover and fuse.
    - txt: |
        4) Insert a fuse into the fuse holder and replace the cover.
      img: ../img/assembly/core/power4.webp
      img_txt: Install the new fuse.
    - txt: |
        5) Slide the IEC socket into the rear of the base.
      img: ../img/assembly/core/power5.webp
      img_txt: Install the socket.
    - txt: |
        6) Secure the IEC socket with two (2) M3 x 6mm screws.
      img: ../img/assembly/core/power6.webp
      img_txt: Secure with screws.
---

{% import 'assembly.md' as assy %}

Assembly of the case starts with the Base, our foundation.

## Join Base Halves

!!! note "Note: Unified Builds"
    Skip to [Prepare the Base](#prepare-the-base) if you have printed a Unified Base.

{{ assy.overview_video(meta.video_folder + 'base.mp4') }}

### Materials

=== "Illustrated (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | :material-printer-3d-nozzle: `Base - 36mm Front - HSI with Rocker.stl` | 1 |
    | :material-printer-3d-nozzle: `Base - 36mm Rear - IEC HSI.stl` | 1 |   |
    | M3 x 12mm SHCS            | 4   |         |
=== "Stock"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | :material-printer-3d-nozzle: `Base - 36mm Front - HSI with Rocker.stl` | 1 |
    | :material-printer-3d-nozzle: `Base - 36mm Rear - IEC HSI.stl` | 1 |   |
    | M3 x 12mm SHCS            | 4   |         |

### Directions

{{ assy.render_steps(steps.halves, '480px') }}

### Reference

[![illustration][base_final]{width="640"}][base_final]

## Prepare the Base

{{ assy.overview_video(meta.video_folder + 'power.mp4') }}

### Materials

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 6mm SHCS             | 2   |                                 |
| SPST rocker switch        | 1   |                                 |
| IEC C14 socket with fuse holder | 1   |                           |
| Fuse, Glass, 5x20mm, Fast Blow | 1 | |                            |
| :material-printer-3d-nozzle: `Power Switch Protector.stl` | 1 | Prevents accidentally switching off power.  |

### Directions

!!! note
    Replacing the fuse is necessary if the IEC socket lacks a fuse or has a fuse of the wrong capacity.

    [This guide][fuse_guide] can help get you started. Consult with a professional if uncertain what capacity fuse you should use.

{{ assy.render_steps(steps.base_prep, '480px') }}

### Reference

[![illustration][power_final]{width="640"}][power_final]

[base_final]: ../img/assembly/core/base_final.webp
[power_final]: ../img/assembly/core/power_final.webp