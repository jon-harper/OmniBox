---
title: MCUs/Control Boards
summary: List of MCU control boards.
authors: Jon Harper
date: 2022-07-22
---

This page lists MCUs that are currently compatible with OmniBox.

!!! tip
    Looking for a board that isn't listed? [Open an issue!][git_issues]

<figure markdown>
  [![front left render][img_mcu]{ width="480" }][img_mcu]
  <figcaption>MCUs are mounted near the lid for accessibility.</figcaption>
</figure>

Micro-controller unit (MCU) board are mounted on :material-alpha-t-box: :material-alpha-m-box-outline: MCU Trays. These parts are in the [`Trays/MCU`][git_mcu] git folder, with each component in its own subfolder. There are `STEP` and Fusion 360 template files available for adding support for other boards.

## BIGTREETECH

| Component                             | Versions | Image                          | Product Link           |
|---------------------------------------|----------|--------------------------------|------------------------|
| [BTT Octopus][git_btt_octopus]        | All      | ![img][img_btt_octopus]        | [:material-cart: Example][bom_btt_octopus] |
| [BTT SKR][git_btt_skr]                | 1.3-2.0  | ![img][img_btt_skr_2]          | [:material-cart: Example][bom_btt_skr_2] |
| [BTT SKR 3][git_btt_skr_3]            | 3.0      | ![img][img_btt_skr_3]          | [:material-cart: Example][bom_btt_skr_3] |
| [BTT SKR 3 EZ][git_btt_skr_3_ez]      | 3.0 EZ 1.0 | ![img][img_btt_skr_3_ez]     | [:material-cart: Example][bom_btt_skr_3_ez] |
| [BTT SKR E3][git_btt_skr_e3]          | All (Mini, Turbo, RRF) | ![img][img_btt_skr_mini_e3_v3] | [:material-cart: Example][bom_btt_skr_e3_mini] |
| [BTT Manta M8P][git_btt_manta_m8p]    | 1.0      | ![img][img_btt_manta_m8p]      | |

## Duet3D

| Component                             | Versions | Image | Product Link           |
|---------------------------------------|----------|-------|------------------------|
| [Duet 3 Mini 5+][git_duet_3_mini_5+]  | All      | ![img][img_duet_3_mini_5+] | [:material-cart: Example][bom_duet_3_mini_5+] |
| [Duet 3 6HC][git_duet_3_6hc]          | All      | ![img][img_duet_3_6hc] | [:material-cart: Example][bom_duet_3_6hc] |

## Other Boards

| Component                             | Versions | Image | Product Link           |
|---------------------------------------|----------|-------|------------------------|
| [Creality boards][git_btt_skr_e3]     | 1.x-4.x  | ![img][img_creality] | [:material-cart: Example][bom_creality_4x] |


[img_mcu]: ../img/components/mcu.png

[img_btt_octopus]: ../img/parts/btt_octopus_1.jpg
[img_btt_skr_2]: ../img/parts/btt_skr_2.jpg
[img_btt_skr_3]: ../img/parts/btt_skr_3.jpg
[img_btt_skr_3_ez]: ../img/parts/btt_skr_3_ez.jpg
[img_btt_manta_m8p]: ../img/parts/btt_manta_m8p.jpg
[img_creality]: ../img/parts/creality_board.jpg
[img_btt_skr_e3_turbo]: ../img/parts/btt_skr_e3_turbo.jpg
[img_btt_skr_mini_e3_v3]: ../img/parts/btt_skr_mini_e3_v3.jpg
[img_duet_3_mini_5+]: ../img/parts/duet3_mini_5plus.jpg
[img_duet_3_6hc]: ../img/parts/duet3_6hc.jpg