---
title: SoC CPUs
summary: List of SoC CPUs supported by OmniBox
authors: Jon Harper
date: 2022-07-22
---

This page lists CPUs currently compatible with OmniBox.

<figure markdown>
  [![front left render][cpu]{ width="480" }][cpu]
  <figcaption>CPU trays can be mounted on the left or right side of the case.</figcaption>
</figure>

Single board computers (SBC) like the Raspberry Pi are mounted on :material-alpha-t-box: :material-alpha-c-box-outline: CPU Trays. These parts are in the [`Trays/CPU`][git_cpu] git folder; each component has its own subfolder. Currently, SBCs other than the Raspberry Pi are not supported.

If you do not use an SBC, the side of the bay can be used as a [:material-alpha-p-box: :material-alpha-s-box-outline: Side Panel][panel_mounts].

| Component                           | Image      |
|-------------------------------------|------------|
| [Raspberry Pi 3B+][git_rpi_3b_plus] | ![img][img_rpi_3b] |
| [Raspberry Pi 4B][git_rpi_4b]       | ![img][img_rpi_4b] |

[cpu]: ../img/components/cpu.png
[img_rpi_3b]: ../img/parts/rpi_3b_plus.jpg
[img_rpi_4b]: ../img/parts/rpi_4b.jpg
[panel_mounts]: panel_mounts.md