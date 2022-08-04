---
title: About OmniBox
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

Welcome to the documentation for the OmniBox, a modular electronics case for 3D printing.

This project is derived from the Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751) V3 footprint; it is a unique design with a lower height and compatibility with larger microcontroller unit (MCU) boards like BIGTREETECH's Octopus. Smaller boards will also fit and the case is compatible with a wide range of parts.

## Quick Links

- [GitHub with STLs](https://github.com/jon-harper/OmniBox)
- [Visual Guided Tour](tour.md)
- [Supported Part List](support/index.md)
- [Printing Guide](printing.md)
- [Bill of Materials](bom.md)
- [Assembly Guide](assembly/index.md)

| Front Left Render | Right Side View |
|-----------------|------------------|
| [![render of the front left][1]][1] | [![right side view][3]][3] |

## About / Background

### The Requirements

Enclosed 3D printing requires controlling more hardware than comes with a typical 3D printer:

- Lighting
- Webcam
- Thermistor for air termperature
- Filtration and exhaust fans

My enclosures are safe to 60C, but I don't want to expose my electronic hardware to that. I printed my first of Steve's electronics cases to remove my hardware from the heat.

As 24 volts is the common DC voltage for 3D printers, each 12V device such as a fan or LED strip needs a buck converter. My printed cases for these printer/enclosure combos were cramped with buck converters. With up to three of each over the microcontroller unit (MCU), I couldn't easily reach the wiring underneath. Additionally, I found myself in need of a new MCU board to use for my printers.

Enter the Octopus, which I had used to success with another project.  BIGTREETECH's Octopus 1.1 is a solid board that provides ample power sources and signal pins. The Octopus will not fit the existing electronics cases I had already printed; I also had a several improvements in mind for Steve's case concept.

### Building the OmniBox

This is my second electronics case for the Octopus designed around general shape and layout from Steve's V3 case. I kept full compatibility only with the original display screens. Lids should be easy to modify to fit, as they maintain the same overall dimensions (note that the screw holes are M3 now, however).

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