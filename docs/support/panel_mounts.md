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

The front panel is long and slim and can be used for mounting small hardware ports. The most common examples are SD Card extensions and USB extensions. You can find these files in the [:material-git: `/Panels/Front Panel`][git_front_panel] git folder.

### Side Panels

![side panel example][img_side]{ width="360" }

Introduced in version 0.9.9, the side panel replaces the old Unused CPU Cover. Side panels can be used for mounting a single 40mm fan, panel mounted connectors, or keystone jacks.

Files for the side panel can be found in the [:material-git: `/Panels/Side Panel`][git_side_panel] git folder.

### Rear Panels

![rear panel example][img_rear]{ width="360" }

Rear Panels are the most customizable part of OmniBox. They can mount connectors and fans and modified to suit each end user. There are also a number of generic templates available in the [:material-git: `/Panels/Rear Panel`][git_rear_panel] git folder.

The table below breaks down where to get started.

| Folder           | Description | Use If You... |
|------------------|-------------|-----------|
| [:material-git: `Generic`][git_generic_rear]  | These have large holes for passing wires through and come in a number of common variations. | ...Want a simple, off-the-shelf solution and there is not a custom panel that suits. |
| [:material-git: `Custom`][git_custom_rear]   | Designed for users of common printer configurations. | ...Have a configuration available for your printer. |
| [:material-git: `Template`][git_rear_template] | A Fusion 360 template with profiles for panel mounted connectors and fans. | ...Want to create your own panel. |
<!-- | [:material-git: `Micro Fit 3`][git_molex_rear]    | Use Molex Micro Fit 3 panel mounted connectors. Pinout diagrams for each panel are included. | ...Want to create a diconnectable wiring harness for your printer. | -->

!!! note "Note: Micro Fit 3"
    Rear panels using Molex Micro Fit 3 connectors were available in early releases. They have been pulled to continue development.

## Supported Hardware

In addition to [fans][fans], templates and predesigned panels are available to mount a variety of hardware.

### MicroSD Extensions

These are availabe in short or long versions and are typically used with MCUs. They can also be used to give access to other SD card slots, such as an SoC CPU.

Each MCU lists whether it can use a short extension (about 6" long) or of the longer extension is needed (about 18").

- Short: [:material-cart: LANMU MicroSD Card Reader Extension][bom_lanmu_micro_sd]
- Long: [:material-cart: ELECTOP MicroSD Card Reader Extension][bom_electop_micro_sd]

### USB Extensions

USB extensions are usually USB B or USB C. Some boards still use Micro-USB; for these extensions, a keystone jack extension is needed.

Right angle connectors are often a good choice, particularly for larger boards.

- [:material-cart: USB B panel mount extension][bom_usb_b_extension]
- [:material-cart: USB C panel mount extension][bom_usb_c_extension]

### Keystone Jacks

Keystone jacks support a variety of multimedia cables: USB, HDMI, and Ethernet, among others. As a result, keystone jacks offer flexibility in choosing which connectors to mount. A blank plate can occupy an unused jack cutout.

These are commonly used on the front, side, or rear panels. Currently, designs with keystone jack cutouts exist for the front and side panels.

Below are several common keystone jacks.

| Description                                       | External connector  | Internal Connector | Cable Length |
|---------------------------------------------------|---------------------|--------------------|--------------|
| [:material-cart: USB 3.0 extension][bom_key_usb3] | USB 3.0 Type A      | USB 3.0 Type A     | 6"           |
| [:material-cart: HDMI][bom_key_hdmi]              | HDMI                | HDMI               | Coupler only |
| [:material-cart: Ethernet][bom_key_ethernet]      | RJ-45 (Ethernet)    | RJ-45 (Ethernet)   | Coupler only |
| [:material-cart: USB C][bom_key_usb_c]            | USB C               | USB C              | 8"           |


### Other Connectors

JST SM and Molex's Micro Fit 3.0 connectors can both be panel-mounted. These are useful when creating detachable wiring harnesses.

#### JST SM

[:material-cart: JST SM Connector Kit][bom_jst_sm_kit]

[:material-book-open: JST SM on The Clockmaker Project][clk_jst_sm]

#### Molex Micro Fit 3.0

Supported up to 2-row, 16-position, althouhg up to 24 position are available. Larger than 16 pin can be hard to disconnect.

[:material-cart: Molex Micro Fit 3.0 connectors][bom_molex]

[:material-book-open: Molex Micro Fit 3.0 on The Clockmaker Project][clk_mf3]

[fans]: fans.md

[img_rear]: ../img/components/rear.png
[img_front]: ../img/components/front_panel.png
[img_side]: ../img/components/side.png