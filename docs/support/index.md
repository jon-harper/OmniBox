---
title: Support Overview
summary: Introduction to OmniBox product support.
authors: Jon Harper
date: 2022-07-03
prefix: ../
---

OmniBox mounts parts on a set of internal trays and exterior panels.

## Fit Testing

Before a tray or panel is merged into the `main` branch, it has to be tested. Parts that have not been tested for fit are marked like so:

!!! caution "Fit Test Pending: Issue #NNN"

If you print one of these parts, please report your results! There is usually an open [:material-git: issue on GitHub][git_issues] for that hardware component.

## Trays

<figure markdown>
  [![the three types of trays][img_trays]{ width="640" }][img_trays]
  <figcaption>The four types of trays: MCU, CPU, PSU, and lower bay.</figcaption>
</figure>

Trays mount electronics most of your case's electronics.

- [MCUs][mcu] are mounted directly underneath the lid for easy access.
- [CPUs][cpu] sit on trays that can slide out the side of the case.
- [Power supplies (PSUs)][psu] are inserted from below.
- [Lower Bay Trays][lower_bay] are used for parts such as buck converters and solid state relays. These occupy the middle of the case.

## Panels

Panels are generally used for displays, [fans][fans], and [panel-mounted connector extensions][panel_mounts] like USB ports and 
SD card readers. Lids can be put to a wide variety of uses, as well.

<figure markdown>
  [![external panels][img_panels]{ width="640" }][img_panels]
  <figcaption>Panels cover the outside of the case.</figcaption>
</figure>

- [Display Panels][display] mount LCD and TFT displays.
- [Bottom Panels][bottom] protect the PSU and allow airflow, if needed.
- [Front Panels][front] are a user-facing panel for MicroSD, USB ports, or even LED lights.
- [Lids][lid] serve many purposes, including mounting large fans and/or a handle.
- [Rear Panels][rear] pass-through wiring to your printer and can mount medium-sized fines.
- [Side Panels][side] are convenient air inlets and connector panels.

[panel_mounts]: panel_mounts.md
[cpu]: cpu.md
[mcu]: mcu.md
[psu]: psu.md
[display]: display.md
[lower_bay]: lower_bay.md
[fans]: fans.md
[tour]: ../tour.md
[front]: front.md
[rear]: rear.md
[side]: side.md
[lid]: lid.md
[bottom]: bottom.md

[img_trays]:  ../img/components/trays.webp
[img_panels]:  ../img/components/panels.webp