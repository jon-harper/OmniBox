---
title: Panel Mounts
summary: A list of panel mounted components supported by OmniBox
authors: Jon Harper
date: 2022-07-22
---

## Using Panel Mounts

 Connector panel mounts will typically be on the rear panel and connect with the printer. Extensions can be mounted on the front or rear and are typically for SD Cards and USB ports.

### Front Panels

![front panel example][img_front]{ width="360" }

The front panel is long and slim and can be used for mounting small hardware ports. The most common examples are SD Card extensions and USB extensions. You can find these files in the [:material-git:`Panels/Front Panel`][git_front_panel] git folder.

### Side Panels

![side panel example][img_side]{ width="360" }

Introduced in version 0.9.9, the side panel replaces the old Unused CPU Cover. Side panels can be used for mounting a single 40mm fan, panel mounted connectors, or keystone jacks.

Files for the side panel can be found in the [:material-git:`Panels/Side Panel`][git_side_panel] git folder.

### Rear Panels

![rear panel example][img_rear]{ width="360" }

Rear Panels are the most customizable part of OmniBox. They can mount connectors and fans and modified to suit each end user. There are also a number of generic templates available in the [:material-git:`Panels/Rear Panel`][git_rear_panel] git folder.

## Supported Hardware

In addition to [fans][fans], templates and predesigned panels are available to mount the following hardware:

| Connector or Extension | Typical Location | Notes |
|------------------------|----------|-------|
| [:material-cart: MicroSD panel mount extension][bom_lanmu_micro_sd] | Front | |
| [:material-cart: USB B panel mount extension][bom_usb_b_extension] | Front or Rear | Right angle connector fits most boards more easily. |
| [:material-cart: USB C panel mount extension][bom_usb_c_extension] | Front or Rear | |
| [:material-cart: JST SM panel mount connectors][bom_jst_sm_kit] | Rear | 2-5 pins |
| [:material-cart: Molex Micro Fit 3.0 connectors][bom_molex] | Rear | Supported up to 2-row, 16-position. |
| Keystone Jacks | Front, Side, Rear | Currently only the side panel has a predesigned keystone jack mount. |

[fans]: fans.md

[img_rear]: ../img/components/rear.png
[img_front]: ../img/components/front_panel.png
[img_side]: ../img/components/side.png