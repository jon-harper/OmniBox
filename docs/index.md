---
title: About OmniBox
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

Welcome to the documentation for the OmniBox, a modular electronics case for 3D printing.

This project is derived from the Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751) V3 footprint; it is a unique design with a lower height and compatibility with larger microcontroller unit (MCU) boards like BIGTREETECH's Octopus. Smaller boards will also fit and the case is compatible with a wide range of parts.

| Front Left Render | Right Side View |
|-----------------|------------------|
| [![render of the front left][1]][1] | [![right side view][3]][3] |


## Quick Links

- [GitHub with STLs](https://github.com/jon-harper/OmniBox)
- [Visual Guided Tour](tour.md)
- [Supported Part List](support/index.md)
- [Printing Guide](printing.md)
- [Bill of Materials](bom.md)
- [Assembly Guide](assembly/index.md)

## Version Stability Guarantee

OmniBox takes some time to print in its entirety. This makes incompatibility between versions painful; upgrading one printed part should not require others to be reprinted.

The printed components of OmniBox are "stable" or "frozen" in how they connect with other printed parts. This means that if you choose to print a newer version of a Core part, no panels or trays will need to be reprinted.

With version 0.9.8:

- The mounting interfaces for panels and trays are frozen.
- Old panels and trays will always be usable with new Core components and vice versa.

In addition, the interface *between* Core components is frozen across all versions, e.g., a base can be used with a main body of a different version.

## About / Background

### The Requirements

Enclosed 3D printing requires controlling more hardware than comes with a typical 3D printer:

- Lighting
- Webcam
- Thermistor for air termperature
- Filtration and exhaust fans

My enclosures are safe to 60C, but I don't want to expose my electronic hardware to that. I printed my first of Steve's electronics cases to remove my hardware from the heat.

Most common devices like fans and lights (and Raspberry Pis!) need a buck converter to work with a 3D printer's power supply. My printed cases for these printer/enclosure combos became cramped. Each buck converter had to sit on a tray above the microcontroller unit (MCU); wiring changes to the MCU required that I first remove up to three buck converter trays.

Additionally, I wanted to use the BIGTREETECH's Octopus in a case, which I had used to success with another project. The Octopus 1.1 is a solid board that provides ample power sources and signal pins. The Octopus does not fit the cases I had already printed; I also had several ideas to improve upon Steve's case.

With these requirements and goals in mind, I decided to design my own case.

### Building the OmniBox

This is my second electronics case for the Octopus designed around general shape and layout from Steve's V3 case. I kept full compatibility only with the original display screens. Lids should be easy to modify to fit.

Templates are provided for all trays and panels to allow further customization and support for new products.

### Other Improvements

These are other changes and improvements present in OmniBox:

- Buck converters, solid state relays (SSRs), and other additional hardware can be mounted below the board instead of above.
- The rear panel is larger and covers most of the base.
- The base is approximately 1.2" shorter; wires are meant to exit from the back or top of the electronics case.
- The case is designed to draw air upwards and out past the MCU drivers, providing effective cooling with two 40mm fans.
- Some screws that were M4 are now M3.

![front right render][2]

[1]: img/gallery_0.9.8/front_left.png
[2]: img/gallery_0.9.8/front_right.png
[3]: img/gallery_0.9.8/oscar_right.jpg