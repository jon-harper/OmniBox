---
title: About OmniBox
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

Welcome to the documentation for the OmniBox, a modular electronics case for 3D printers.

This project is derived from the Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751) V3 footprint; OmniBox is a unique design with a lower height and compatibility with larger microcontroller unit (MCU) boards like BIGTREETECH's Octopus. The case is compatible with a wide range of parts and and is meant to be easily upgradeable.

<!-- | Front Left Render | Right Side View |
|-----------------|------------------|
| [![render of the front left][1]][1] | [![right side view][3]][3] | -->

[![gallery of OmniBox part combinations][2]][2]

## Quick Links

:material-github: [GitHub with STLs](https://github.com/jon-harper/OmniBox)

:material-television-guide: [Visual Guided Tour](tour.md)

:octicons-checklist-24: [Supported Part List](support/index.md)

:material-printer-3d-nozzle: [Printing Guide](printing.md)

:octicons-list-ordered-24: [Bill of Materials](bom.md)

:material-directions: [Assembly Guide](assembly/index.md)

## Version Stability Guarantee

Printing OmniBox is a time investment. This makes incompatibility between versions painful; upgrading one printed part should not require others to be reprinted. Thankfully, OmniBox is highly modular and can be upgrade piecemeal.

I've extended that modularity with a "Version Stability Guarantee":

The printed components of OmniBox are "stable" or "frozen" in how they connect with other printed parts. This means that if you choose to print a newer version of a core part, no panels or trays will need to be reprinted.

See the [Visual Guided Tour](tour.md) to see how this works in practice.

## The Requirements

### Enclosed Printing

Enclosed 3D printing requires controlling more hardware than comes with a typical 3D printer:

- Lighting
- Webcam
- Thermistor (temperature sensor)
- Temperature-controlled exhaust fan
- Always-on Filtration fan

Electronics are typically rated to for short periods at high ambient temperatures, but the 50C/120F or more of a well-insulated enclosure is hazardous to electronics. I printed my first of Steve's cases to remove my electronic hardware from such heat.

### Managing Devices

Most common devices like fans and lights (and Raspberry Pis!) need a buck converter to work with a 3D printer's power supply. My printed cases for these printer/enclosure combos became cramped. Each buck converter had to sit on a tray above the microcontroller unit (MCU); wiring changes to the MCU required that I first remove up to three buck converter trays.

### Support for Large Boards

Additionally, I wanted to use the BIGTREETECH's Octopus in a case, which I had used to success with another project. The Octopus 1.1 is a solid board that provides ample power sources and signal pins. The Octopus does not fit the cases I had already printed; I also had several ideas to improve upon Steve's case.

With these requirements and goals in mind, I decided to design my own case.

## Building the OmniBox

This is my second electronics case for the Octopus designed around general shape and layout from Steve's V3 case. I kept full compatibility only with the original display screens. Lids should be easy to modify to fit.

Templates are provided for all trays and panels to allow further customization and support for new products.

## Current Status

OmniBox is currently pre-1.0 but mature enough for everyday use.

See the [Version History][4] page for information on the latest release, fixes, new features, and known issues.

![front right render][2]

[1]: img/gallery_0.9.8/front_left.png
[2]: img/gallery_0.9.8.1/gallery_high.png
[3]: img/gallery_0.9.8/oscar_right.jpg
[4]: history/index.md