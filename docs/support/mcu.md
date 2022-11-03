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

| Component                             | Versions | Image |
|---------------------------------------|----------|-------|
| [BTT Octopus][git_btt_octopus]        | All      | ![img][img_btt_octopus] |
| [BTT SKR][git_btt_skr]                | 1.3-2.0  | ![img][img_btt_skr_2] |
| [BTT SKR 3][git_btt_skr_3]            | 3.0      | ![img][img_btt_skr_3] |
| [BTT SKR 3][git_btt_skr_3_ez]         | 3.0 EZ 1.0 | ![img][img_btt_skr_3_ez] |
| [BTT SKR Mini E3][git_btt_skr_e3]     | All      | ![img][img_btt_skr_mini_e3_v3] |
| [BTT SKR E3/E3 Turbo][git_btt_skr_e3] | All      | ![img][img_btt_skr_e3_turbo] |
| [Creality boards][git_btt_skr_e3]     | 1.x-4.x  | ![img][img_creality] |
| [BTT Manta M8P][git_btt_manta_m8p]    | 1.0      | ![img][img_btt_manta_m8p] |

<!-- TODO: add missing images -->

[img_mcu]: ../img/components/mcu.png

[img_btt_octopus]: ../img/parts/btt_octopus_1.jpg
[img_btt_skr_2]: ../img/parts/btt_skr_2.jpg
[img_btt_skr_3]: ../img/parts/btt_skr_3.jpg
[img_btt_skr_3_ez]: ../img/parts/btt_skr_3_ez.jpg
[img_btt_manta_m8p]: ../img/parts/btt_manta_m8p.jpg
[img_creality]: ../img/parts/creality_board.jpg
[img_btt_skr_e3_turbo]: ../img/parts/btt_skr_e3_turbo.jpg
[img_btt_skr_mini_e3_v3]: ../img/parts/btt_skr_mini_e3_v3.jpg