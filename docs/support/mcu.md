---
title: MCUs/Control Boards
summary: List of MCU control boards.
authors: Jon Harper
date: 2022-07-22
---

This page lists MCUs that are currently compatible with OmniBox.

<figure markdown>
  [![front left render][img_mcu]{ width="480" }][img_mcu]
  <figcaption>MCUs are mounted near the lid for accessibility.</figcaption>
</figure>

Micro-controller unit (MCU) board are mounted on MCU Trays. These parts are in the [:material-git:`Trays/MCU`][git_mcu] git folder, with each component in its own subfolder. There are `STEP` and Fusion 360 template files available for adding support for other boards.

!!! tip
    Looking for a board that isn't listed? [Open an issue!][git_issues]


<!-- Template 
[![product picture][img_]{width="200"}][img_]

[:material-git: Files: ][git_]{ .md-button }

[:material-cart: Product Link][bom_]{ .md-button }
-->

## BIGTREETECH

### SKR Series

#### SKR 1.3 - 2.0

[:material-git: Files: `BTT SKR`][git_btt_skr]{ .md-button }

[:material-cart: Product Link][bom_btt_skr_2]{ .md-button }

[![product picture][img_btt_skr_2]{width="200"}][img_btt_skr_2]

- Mounting: 4x M3
- Notes: SKR 3 and SKR 3 EZ are incompatible. See below.

#### SKR 3

[:material-git: Files: `BTT SKR 3`][git_btt_skr_3]{ .md-button }

[:material-cart: Product Link][bom_btt_skr_3]{ .md-button }

[![product picture][img_btt_skr_3]{width="200"}][img_btt_skr_3]

- Mounting: 4x M3
- Notes: SKR 3 EZ and earlier SKR models are incompatible.

#### SKR 3 EZ

[:material-git: Files: `BTT SKR 3 EZ`][git_btt_skr_3_ez]{ .md-button }

[:material-cart: Product Link][bom_btt_skr_3_ez]{ .md-button }

[![product picture][img_btt_skr_3_ez]{width="200"}][img_btt_skr_3_ez]

- Mounting: 4x M3
- Notes: Not compatible with other SKR trays.

### SKR 3 E3 Series

All versions of the SKR E3 series are compatible with one tray, uncluding the Mini, Turbo, and RRF versions.

[:material-git: Files: `BTT SKR E3`][git_btt_skr_e3]{ .md-button }

[:material-cart: Product Link][bom_btt_skr_e3_mini]{ .md-button }

[![skr mini e3 v3][img_btt_skr_mini_e3_v3]{width="200"}][img_btt_skr_mini_e3_v3]

- Mounting: 4-5x M3
- Notes: Same mounting hole pattern as Creality boards.

### Manta Series

The Manta M4P is not currently supported, but may be added in a future release.

#### Manta M8P

[:material-git: Files: `BTT Manta M8P`][git_btt_manta_m8p]{ .md-button }

[:material-cart: Product Link][bom_btt_manta_m8p]{ .md-button }

[![product picture][img_btt_manta_m8p]{width="200"}][img_btt_manta_m8p]

- Mounting: 4x M3

### Octopus Series

The Octopus Pro is not currently supported, but may be added in a future release.
#### Octopus

[:material-git: Files: `BTT Octopus`][git_btt_octopus]{ .md-button }

[:material-cart: Product Link][bom_btt_octopus]{ .md-button }

[![product picture][img_btt_octopus]{width="200"}][img_btt_octopus]

- Mounting: 4x M3

## Duet3D

### Duet 3 Mini 5+ 

Compatible with all versions.

[:material-git: Files: `Duet3D Duet 3 Mini 5+`][git_duet_3_mini_5+]{ .md-button }

[:material-cart: Product Link][bom_duet_3_mini_5+]{ .md-button }

[![product picture][img_duet_3_mini_5+]{width="200"}][img_duet_3_mini_5+]

- Mounting: 4x M3

### Duet 3 6HC

Compatible with all versions.

[:material-git: Files: `Duet3D Duet 3 6HC`][git_duet_3_6hc]{ .md-button }

[:material-cart: Product Link][bom_duet_3_6hc]{ .md-button }

[![product picture][img_duet_3_6hc]{width="200"}][img_duet_3_6hc]

- Mounting: 4x M3


## Other Boards

### Creality

[:material-git: Files: `BTT SKR E3`][git_btt_skr_e3]{ .md-button }

[:material-cart: Product Link][bom_creality_4x]{ .md-button }

[![product picture][img_creality]{width="200"}][img_creality]

- Mounting: 4-5x M3
- Notes: Compatible with version 1.x to 4.x.

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