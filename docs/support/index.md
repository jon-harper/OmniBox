---
title: Parts Overview
summary: A list of parts supported by OmniBox
authors: Jon Harper
date: 2022-07-03
---

This is an overview of components supported by OmniBox. The linked git folders should contain both an `STL` for printing and `STEP` files for modification. Fusion 360 source files are also usually available.

## Fit Testing

Before a tray or panel is merged into the `main` or another stable branch, it has to be fit tested. Parts that have not been tested for fit are marked:

!!! caution "Fit Test Pending: Issue #NNN"

If you print one of these parts, please report your results! There is usually an open [:material-git: issue on GitHub][git_issues] for that hardware component.

## Trays

<figure markdown>
  [![the three types of trays][img_trays]{ width="640" }][img_trays]
  <figcaption>The four types of trays in red.</figcaption>
</figure>

Trays mount most of the key hardware in your case.

- [MCU Trays][mcu] mounts MCU boards.
- [CPU Trays][cpu] are for SBCs.
- [PSU Trays][psu] mount power supplies.
- [Lower Bay Trays][lower_bay] contains trays for miscellaneous accessories, such as buck converters and solid state relays.

## Panels

<figure markdown>
  [![the three types of trays][img_panels]{ width="640" }][img_panels]
  <figcaption>Panels cover the outside of the case.</figcaption>
</figure>

### Display Screen Panels

[Display Panels][displays] are used for LCD displays, including Raspberry Pi TFTs.

### Front, Side, and Rear Panels

These panels are typically used for [panel mounted connectors and extensions][panel_mounts] and mounting [fans][fans].

Generic rear panels are available with cutouts to pass wiring directly without using connectors.

## Fans

An assortment of fans are supported and include cages and optional TPU shims. See the [Fans][fans] page for a full list.

The front and rear main bodies come in versions with and without fans. The rear panel and lid can also be used for mounting fans.

See the [Guided Tour][tour] to help choose the best configuration for your available parts.

[panel_mounts]: panel_mounts.md
[cpu]: cpu.md
[mcu]: mcu.md
[psu]: psu.md
[displays]: displays.md
[lower_bay]: lower_bay.md
[fans]: fans.md
[tour]: ../tour.md
[9]: ../tour.md#core-parts-with-variants

[img_trays]:  ../img/components/trays.png
[img_panels]:  ../img/components/panels.png