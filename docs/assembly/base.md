---
title: Base and PSU
summary: Instructions for assembling the base and PSU tray.
authors: Jon Harper
date: 2024-02-27
steps:
  halves:
    - txt: |
        1) Press the Front Base and Rear Base together as illustrated. The angled screw holes on the
        mating faces should align.
      img: ../img/assembly/core/base1.webp
      img_txt: Align the screw holes
    - txt: |
        2) Insert four (4) M3 x 12mm screws in the angled holes in the top of the Rear Base and
        fasten them to the Front Base.<br>
        Re-check the the alignment of the front and rear before fully tightening.
      img: ../img/assembly/core/base2.webp
      img_txt: Install the center screws
  base_prep:
    - txt: |
        1) Insert the rocker switch into the Power Switch Protector with **"ON" facing up**. The flaps on the switch
        compress during insertion, then snap in place to hold it.
      img: ../img/assembly/core/power1.webp
      img_txt: Join rocker switch to protector.
    - txt: |
        2) Insert the rocker switch and protector into the open slot on the front base.
      img: ../img/assembly/core/power2.webp
      img_txt: Install the rocker switch.
    - txt: |
        3) Remove the fuse cover by sliding it out. Remove the fuse in the holder.
      img: ../img/assembly/core/power3.webp
      img_txt: Remove the fuse cover and fuse.
    - txt: |
        4) Insert the new fuse into the holder and replace the cover. Direction of the fuse does not matter.
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

!!! note "Note: Glass Fuses"
    Replacing the fuse is necessary if the power inlet has a fuse of the wrong capacity (or lacks one entirely).

    [This guide][fuse_guide] can help get you started. Consult with a professional if uncertain what capacity fuse you should use.

{{ assy.render_steps(steps.base_prep, '480px') }}

### Reference

[![illustration][power_final]{width="640"}][power_final]

[base_final]: ../img/assembly/core/base_final.webp
[power_final]: ../img/assembly/core/power_final.webp