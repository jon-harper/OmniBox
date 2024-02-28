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
      img: TODO
      img_txt: Align the screw holes
    - txt: |
        2) Install four (4) M3 x 8mm screws in the angled holes in the top of the Rear half.
        These screws join with the Front half.<br>
        Double-check that the halves are aligned before fully tightening the screws.
      img: TODO
      img_txt: Install the center screws
  base_prep:
    - txt: |
        1) Use flush cutters to remove the last rib on both sides of the rocker switch.
      img: todo
      img_txt: Remove the last rib on the rocker switch.
    - txt: |
        2) Insert the rocker switch into the Power Switch Protector. The flaps on the side compress and snap the switch in place once inserted.
      img: todo
      img_txt: Join rocker switch to protector.
    - txt: |
        3) Slide the rocker switch and protector into the open slot on the front base. It should pop into place.
      img: todo
      img_txt: Install the rocker switch.
    - txt: |
        4) Remove the fuse cover by sliding it out. If a fuse is inserted in the fuse holder, remove it.
      img: todo
      img_txt: Remove the fuse cover and fuse.
    - txt: |
        5) Insert a fuse into the fuse holder and replace the cover.
      img: todo
      img_txt: Install the new fuse.
    - txt: |
        6) Slide the IEC socket into the rear of the base and secure with two (2) M3 x 6mm screws.
      img: todo
      img_txt: Install the socket.
  psu_tray:
    - txt: |
        1) Set the power supply with the terminals are facing downwards and away from you.
      img: todo
      img_text: Orient the PSU.
    - txt: |
        2) Place the right PSU tray mount against the right side of the power supply. The printed 'R' should face upwards.
      img: todo
      img_txt: Orient the right tray mount.
    - txt: |
        3) Use two (2) M4 screws to attach the tray mount.
      img: todo
      img_txt: Attach with two M4 screws.
    - txt: |
        4) Set the left tray mount against the opposite side of the power supply. The 'L' should face upwards.
      img: todo
      img_txt: Orient the left tray mount.
    - txt: |
        5) Secure using two (2) M4 screws.
      img: todo
      img_txt: Secure with two M4 screws.
  psu:
    - txt: |
        1) Turn the base over so that the version numbers are visible.
      img: todo
      img_txt: Orient the base.
    - txt: |
        2) Turn the PSU assembly so that the terminals face upwards and slide the assembly into the base.
      img: todo
      img_txt: Secure with two M4 screws.
    - txt: |
        3) Use the side holes in the base and four (4) 12mm M3 screws to attach the base to the PSU tray.
      img: todo
      img_txt: Attach the base with 12mm screws.
---

{% import 'assembly.md' as assy %}

Assembly of the case starts with the Base and PSU Tray.

## Join Base Halves

!!! note "Note: Unified Builds"
    Skip this step if you printed a Unified Base.

{{ assy.overview_video(meta.video_folder + 'base_join.mp4') }}

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

## Prepare the Base

{{ assy.overview_video(meta.video_folder + 'base_prep.mp4') }}

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

[![illustration][base_prep_final]{width="640"}][base_prep_final]

## PSU Tray

{{ assy.overview_video(meta.video_folder + 'psu.mp4') }}

### Materials

=== "As Illustrated"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M4 x 6mm SHCS             | 4   | No longer than 8mm.             |
    | Mean Well LRS-350-24      | 1   |                                 |
    | :material-printer-3d-nozzle: `PSU Mount - LRS-350 - Left HSI.stl`  | 1   | |
    | :material-printer-3d-nozzle: `PSU Mount - LRS-350 - Right HSI.stl`  | 1   | |

=== "Generic"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M4 x 6mm SHCS             | 4-8 | No longer than 8mm.             |
    | Compatible power supply   | 1   |  |
    | :material-printer-3d-nozzle: Left PSU mount | 1 | |
    | :material-printer-3d-nozzle: Right PSU mount | 1 | |

### Directions

{{ assy.render_steps(steps.psu_tray, '480px') }}

### Reference

[![illustration][psu_final]{width="640"}][psu_final]

## Install PSU

{{ assy.overview_video(meta.video_folder + 'base.mp4') }}

### Materials

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 12mm SHCS            | 4   |                                 |

### Directions

{{ assy.render_steps(steps.psu, '480px') }}

### Reference

[![illustration][base_final]{width="640"}][base_final]