---
title: Panel Mounts
summary: A list of panel mounted components supported by OmniBox
authors: Jon Harper
date: 2022-07-22
---

## Using Panel Mounts

 Connector panel mounts will typically be on the rear panel and connect with the printer. Extensions can be mounted on the front or rear and are typically for SD Cards and USB ports.

 Each panel type comes with a template for making your own panels. See [Creating New Panels](#creating-new-panels) below for more.

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

## Supported Hardware

In addition to [fans][fans], templates and predesigned panels are available to mount a variety of hardware.

### MicroSD Extensions

These are availabe in short or long versions and are typically used with MCUs. They can also be used to give access to other SD card slots, such as an SoC CPU.

Each MCU lists whether it can use a short extension (about 6" long) or of the longer extension is needed (about 18").

[:material-cart: Short MicroSD Card Reader Extension][bom_lanmu_micro_sd]{ .md-button }

[:material-cart: Long MicroSD Card Reader Extension][bom_electop_micro_sd]{ .md-button }

### USB Extensions

USB extensions are usually USB B or USB C. Some boards still use Micro-USB; for these extensions, a keystone jack extension is needed.

Right angle connectors are often a good choice, particularly for larger boards.

[:material-cart: USB B panel mount extension][bom_usb_b_extension]{ .md-button }

[:material-cart: USB C panel mount extension][bom_usb_c_extension]{ .md-button }
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

These are good, low-curren (3A) connectors for devices such as limit switches, lights, steppers, and fans.

!!! caution
    Avoid use for the hotends on enclosed printers.

[:material-cart: JST SM Connector Kit][bom_jst_sm_kit]{ .md-button }

Further reading: [:material-book-open: JST SM on The Clockmaker Project][clk_jst_sm]

#### Molex Micro Fit 3.0

These make excellent connectors for printers, particularly for hotends. They are rated to 5A (higher with gold pins).

Connectors up to 2 row, 24 positions are available.

[:material-cart: Molex Micro Fit 3.0 connectors][bom_molex]{ .md-button }

Further reading: [:material-book-open: Molex Micro Fit 3.0 on The Clockmaker Project][clk_mf3]

#### XT-60

This connector is most well known for RC electronics and Creality printer beds. They should be used with 12 AWG wire for their rated current, though 13 AWG/2.5mm^2^ is often used for 220W beds.

[:material-cart: Male XT-60 Panel Mounts][bom_xt60]{ .md-button }

Further reading: [:material-book-open: XT-60 on The Clockmaker Project][clk_xt60]

#### Molex Mini Fit Jr.

Mini Fit Jr connectors are commonly seen in computers for the ATX and PCIE connectors. They are reliable connectors rated up to 9.5A with 18 AWG (~1 mm^2^) wires.

[:material-cart: Mini Fit Jr 2 Position Connector Sets][bom_mfj2]{ .md-button }

[:material-cart: Mini Fit Jr 4 Position Connector Sets][bom_mfj4]{ .md-button }

Further reading: [:material-book-open: Mini Fit Jr on The Clockmaker Project][clk_mfj]

## Creating New Panels

In addition to templates for the panels, there are also templates for the cutouts needed to add panels mounts available in the git folder below.

[:material-git: Panel Mounts][git_panel_mounts]{ .md-button }

The solid bodies in the `STEP` and Fusion 360 files:

- Have sufficient clearance to insert the connector; and
- Are the correct thickness for the connector (e.g. for panel mount ears to engage).

The Fusion 360 file also contains sketches for cut-and-paste.

[fans]: fans.md

[img_rear]: ../img/components/rear.png
[img_front]: ../img/components/front_panel.png
[img_side]: ../img/components/side.png