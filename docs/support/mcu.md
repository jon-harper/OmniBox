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

Micro-controller unit (MCU) board are mounted on MCU Trays. These parts are in the [:material-git: `/Trays/MCU`][git_mcu] git folder, with each component in its own subfolder. There are `STEP` and Fusion 360 template files available for adding support for other boards.

For each entry, `Materials` are the fasteners required to mount the board, while the `MicroSD Extension` for the front panel is optional (but recommended).

!!! tip
    Looking for a board that isn't listed? [:material-git: Open an issue!][git_issues]


<!-- Template 
[![product picture][img_]{width="200"}][img_]

[:material-git: Files: ][git_]{ .md-button }

[:material-cart: Product Link][bom_]{ .md-button }

- Materials:
- MicroSD Extension: 
- Notes:
-->

## BIGTREETECH

### SKR Series

#### SKR 1.3 - 2.0

[:material-git: BTT SKR][git_btt_skr]{ .md-button }

[:material-cart: Product Link][bom_btt_skr_2]{ .md-button }

[![product picture][img_btt_skr_2]{width="200"}][img_btt_skr_2]

- Materials: 4x M3 x 6mm
- MicroSD Extension: [:material-cart: Long][bom_electop_micro_sd]
- Notes: SKR 3 and SKR 3 EZ are incompatible. See below.

#### SKR 3

!!! caution "Fit Test Pending: [:material-git: Issue #48](https://github.com/jon-harper/OmniBox/issues/48)"
    

[:material-git: BTT SKR 3][git_btt_skr_3]{ .md-button }

[:material-cart: Product Link][bom_btt_skr_3]{ .md-button }

[![product picture][img_btt_skr_3]{width="200"}][img_btt_skr_3]

- Materials: 4x M3 x 6mm
- MicroSD Extension: [:material-cart: Long][bom_electop_micro_sd]
- Notes: SKR 3 EZ and earlier SKR models are incompatible.

#### SKR 3 EZ

!!! caution "Fit Test Pending: [:material-git: Issue #48](https://github.com/jon-harper/OmniBox/issues/48)"

[:material-git: BTT SKR 3 EZ][git_btt_skr_3_ez]{ .md-button }

[:material-cart: Product Link][bom_btt_skr_3_ez]{ .md-button }

[![product picture][img_btt_skr_3_ez]{width="200"}][img_btt_skr_3_ez]

- Materials: 4x M3 x 6mm
- MicroSD Extension: [:material-cart: Long][bom_electop_micro_sd]
- Notes: Not compatible with other SKR trays.

### SKR 3 E3 Series

All versions of the SKR E3 series are compatible with one tray, uncluding the Mini, Turbo, and RRF versions.

[:material-git: BTT SKR E3][git_btt_skr_e3]{ .md-button }

[:material-cart: Product Link][bom_btt_skr_e3_mini]{ .md-button }

[![skr mini e3 v3][img_btt_skr_mini_e3_v3]{width="200"}][img_btt_skr_mini_e3_v3]

- Materials: 4-5x M3 x 6mm
- MicroSD Extension: [:material-cart: Short][bom_lanmu_micro_sd]
- Notes: Same mounting hole pattern as Creality boards.

### Manta Series

The Manta M4P is not currently supported, but may be added in a future release.

#### Manta M8P

!!! caution "Fit Test Pending"

[:material-git: BTT Manta M8P][git_btt_manta_m8p]{ .md-button }

[:material-cart: Product Link][bom_btt_manta_m8p]{ .md-button }

[![product picture][img_btt_manta_m8p]{width="200"}][img_btt_manta_m8p]

- Materials: 4x M3 x 6mm
- MicroSD Extension: [:material-cart: Short][bom_lanmu_micro_sd]

### Octopus Series

The Octopus Pro is not currently supported, but may be added in a future release.
#### Octopus

[:material-git: BTT Octopus][git_btt_octopus]{ .md-button }

[:material-cart: Product Link][bom_btt_octopus]{ .md-button }

[![product picture][img_btt_octopus]{width="200"}][img_btt_octopus]

- Materials: 4x M3 x 6mm
- MicroSD Extension: [:material-cart: Short][bom_lanmu_micro_sd]

## Duet3D

### Duet 3 Mini 5+ 

Compatible with all versions.

[:material-git: Duet3D Duet 3 Mini 5+][git_duet_3_mini_5+]{ .md-button }

[:material-cart: Product Link][bom_duet_3_mini_5+]{ .md-button }

[![product picture][img_duet_3_mini_5+]{width="200"}][img_duet_3_mini_5+]

- Materials: 4x M3 x 6mm
- MicroSD Extension: [:material-cart: Short][bom_lanmu_micro_sd]

### Duet 3 6HC

Compatible with all versions.

[:material-git: Duet3D Duet 3 6HC][git_duet_3_6hc]{ .md-button }

[:material-cart: Product Link][bom_duet_3_6hc]{ .md-button }

[![product picture][img_duet_3_6hc]{width="200"}][img_duet_3_6hc]

- Materials: 4x M3 x 6mm
- MicroSD Extension: [:material-cart: Short][bom_lanmu_micro_sd]


## MakerBase

### MKS Monster8

!!! caution "Fit Test Pending: [Issue #74](https://github.com/jon-harper/OmniBox/issues/74)"

[:material-git: BTT Manta M8P][git_mks_monster8]{ .md-button }

[:material-cart: Product Link][bom_mks_monster8]{ .md-button }

[![product picture][img_mks_monster8]{width="200"}][img_mks_monster8]

- Materials: 4x M3 x 6mm
- MicroSD Extension: [:material-cart: Short][bom_lanmu_micro_sd]
- Compatibility: 1.0, 2.0
### MKS Skipr

!!! caution "Fit Test Pending: [Issue #70](https://github.com/jon-harper/OmniBox/issues/70)"

[:material-git: BTT Manta M8P][git_mks_skipr]{ .md-button }

[:material-cart: Product Link][bom_mks_skipr]{ .md-button }

[![product picture][img_mks_skipr]{width="200"}][img_mks_skipr]

- Materials: 4x M3 x 6mm
- MicroSD Extension: [:material-cart: Short][bom_lanmu_micro_sd]

## Other Boards

### Creality

[:material-git: BTT SKR E3][git_btt_skr_e3]{ .md-button }

[:material-cart: Product Link][bom_creality_4x]{ .md-button }

[![product picture][img_creality]{width="200"}][img_creality]

- Materials: 4-5x M3 x 6mm
- MicroSD Extension: [:material-cart: Short][bom_lanmu_micro_sd]
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
[img_mks_monster8]: ../img/parts/mks_monster8.jpg
[img_mks_skipr]: ../img/parts/mks_skipr.jpg