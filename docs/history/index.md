---
title: 0.9.8 Release (Current)
summary: Changelog for the current and past releases of OmniBox
authors: Jon Harper
date: 2022-08-04
---

The current release is 0.9.8, released on 2022-08-\[16\].

## Fixes

- Button head screws work for the crossbar now.
- Clarified 6mm/8mm screws for power supplies.
- Documentation greatly improved for newcomers.
- Fan cages provide much more airflow.

## New Features

### Completed Requests
- Lower bay tray for Creality MOSFET added.
- New rear panel for the Ender 5 Plus with an 80mm fan.

### Core
- New front vents for the base and larger side vents.
- Two new optional 40mm fans concealed in the intakes.
- MCU trays can be removed without removing the rear panel.
- Fan cages have a parametric template now.
- Multiple new fan cage sizes.

### Panels and Trays
- New half-length lids.
- New half-length lower bay trays.
- Lower bay trays for buck converters and simple, 4-point mounts are now Fusion 360 templates.
- New trays can be added by modifying the Fusion template and exporting the results.
- The template includes mounts with fans and the new half-length size.
- Added support for 5A DROK buck converter and a single 40mm fan.

### Documentation & Repository
- Broke out product support documentation across three pages. Each product includes images and mounting hardware.
- Divided assembly documentation into three sections and added info for Core variants.
- Improved/better overall folder structure; all panel and tray variations have a separate folder.
- Most git folders now have a `readme.md` to help with navigation and part selection.

## Testing/Preliminary Features

- Mean Well RSP-500 power supply for the Ender 5 Plus.
- Raspberry Pi TFT display mounts and lid mounts.

## Gallery

| Renders and Photos        |   |
|---------------------------|---|
| New base intakes          | [![front right render][1]][1] |
| Optional 40mm base fan    | [![hidden 40mm fan installed in the front base][5]][5]
| Optional 40mm front intake fan | [![hidden 40mm fan installed in the front main body intake][6]][6]
| Better TPU gaskets        | [![closeup of installed TPU gasket on fan and cage][2]][2] |
| Simpler MCU installation and removal | [![installed MCU tray][3]][3] |
| Early 0.9.8 assembly      | [![oscar assembled][4]][4] |

[1]: ../img/gallery_0.9.8/front_right.png
[2]: ../img/gallery_0.9.8/gasket.jpg
[3]: ../img/gallery_0.9.8/mcu_tray.jpg
[4]: ../img/gallery_0.9.8/oscar_front.jpg
[5]: ../img/gallery_0.9.8/fan_base.jpg
[6]: ../img/gallery_0.9.8/fan_front.jpg