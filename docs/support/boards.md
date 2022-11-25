---
title: CPU and MCU Boards
summary: List of SoC CPUs and MCU control boards.
authors: Jon Harper
date: 2022-07-22
---

This page lists CPUs and MCUs that are currently compatible with OmniBox.

## Single Board Computers/CPUs

<figure markdown>
  [![front left render][10]{ width="480" }][10]
  <figcaption>Raspberry Pi on a CPU Tray</figcaption>
</figure>

Single board computers (SBC) like the Raspberry Pi are mounted on :material-alpha-t-box: :material-alpha-c-box-outline: CPU Trays. These parts are in the [Trays/CPU][7] git folder; each component has its own subfolder. Currently, SBCs other than the Raspberry Pi are not supported.

If you do not use a SBC, a [blank slot cover][6] can be used.

| Component             | Image |
|-----------------------|-------|
| [Raspberry Pi 3B+][1] | ![img][11] |
| [Raspberry Pi 4B][2]  | ![img][12] |

## MCU Boards

<figure markdown>
  [![front left render][13]{ width="480" }][13]
  <figcaption>BIGTREETECH Octopus on an MCU Tray</figcaption>
</figure>

Micro-controller unit (MCU) board are mounted on :material-alpha-t-box: :material-alpha-m-box-outline: MCU Trays. These parts are in the [Trays/MCU][8] git folder, with each component in its own subfolder. There are `STEP` and Fusion 360 template files available for adding support for other boards.

| Component             | Supported Versions | Image |
|-----------------------|----------|-------|
| [BTT Octopus][3]      | All      | ![img](../img/parts/btt_octopus_1.jpg) |
| [BTT SKR][4]          | 1.3+     | ![img](../img/parts/btt_skr_2.jpg) |
| [BTT SKR Mini E3][5]  | All      | ![img](../img/parts/btt_skr_mini_e3_v3.jpg) |
| [BTT SKR E3 Turbo][5] | All      | ![img](../img/parts/btt_skr_e3_turbo.jpg) |
| [Creality boards][5]  | All      | ![img](../img/parts/creality_board.jpg) |

[1]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPURaspberry%20Pi%203B%20Plus
[2]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU/Raspberry%20Pi%204B
[3]: https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU/BTT%20Octopus
[4]: https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU/BTT%20SKR
[5]: https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU/BTT%20SKR%20E3
[6]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU/Unused%20Tray%20Cover
[7]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU
[8]: https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU

[10]: ../img/examples/cpu.png
[11]: ../img/parts/rpi_3b_plus.jpg
[12]: ../img/parts/rpi_4b.jpg
[13]: ../img/examples/mcu.png