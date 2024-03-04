---
title: PSU
summary: Instructions for assembling and installing the PSU tray.
authors: Jon Harper
date: 2024-03-04
steps:
  psu_tray:
    - txt: |
        1) Set the power supply with the terminals are facing downwards and away from you.
      img: ../img/assembly/core/psu1.webp
      img_txt: Orient the PSU.
    - txt: |
        2) Place the left PSU tray mount against the left side of the power supply. The printed 'L' should face upwards.
      img: ../img/assembly/core/psu2.webp
      img_txt: Orient the left tray mount.
    - txt: |
        3) Use two (2) M4 screws to attach the tray mount.
      img: ../img/assembly/core/psu3.webp
      img_txt: Attach with two M4 screws.
    - txt: |
        4) Set the right tray mount against the opposite side of the power supply. The 'R' should face upwards.
      img: ../img/assembly/core/psu4.webp
      img_txt: Orient the right tray mount.
    - txt: |
        5) Secure using two (2) M4 screws.
      img: ../img/assembly/core/psu5.webp
      img_txt: Secure with two M4 screws.
  psu:
    - txt: |
        1) Turn the base over so that the version numbers are visible.
      img: ../img/assembly/core/base_psu1.webp
      img_txt: Orient the base.
    - txt: |
        2) Turn the PSU assembly so that the terminals face upwards and slide the assembly into the base.
      img: ../img/assembly/core/base_psu2.webp
      img_txt: Insert the PSU.
    - txt: |
        3) Use the side holes in the base and four (4) 12mm M3 screws to attach the base to the PSU tray.
      img: ../img/assembly/core/base_psu3.webp
      img_txt: Attach the base with 12mm screws.
---

{% import 'assembly.md' as assy %}

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

[![illustration][base_psu_final]{width="640"}][base_psu_final]

[base_psu_final]: ../img/assembly/core/base_psu_final.webp
[psu_final]: ../img/assembly/core/psu_final.webp