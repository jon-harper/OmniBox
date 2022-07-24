---
title: About
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

Welcome to the documentation for the OmniBox, a modular control case for 3D printing.

This project is conceptually derived from Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751) V3 footprint; it is a unique design with a lower height and compatibility with larger microcontroller unit (MCU) boards like BIGTREETECH's Octopus. Smaller boards will also fit.

## Quick Links

- [GitHub with STLs](https://github.com/jon-harper/OmniBox)
- [Supported Part List](support.md)
- [Bill of Materials](bom.md)
- [Printing Guide](printing.md)
- [Assembly Guide](assembly.md)

## About / Background

### The Requirements

Printing Acrylonitrile Butadiene Styrene (ABS) plastic requires the use of an enclosure with filtration. This typically requires connecting additional hardware to a printer's MCU:

- Interior lighting
- Ambient temperature thermistor
- Filtration and exhaust fans

As 24V is the common DC voltage for 3D printers right now, each 12V independantly-controllable or PWM device such as a fan or light strip needs a buck converter. My control cases for these printer/enclosure combos were cramped—the three or more buck converters mounted over the MCU kept me from accessing the wiring underneath.

Additionally, after multiple Dead-On-Arrival (DOA) and failed BIGTREETECH SKR 2 boards, I urgently had to find another board to settle on. Enter the Octopus, which I had used to success with another project.

### Switching to the Octopus

BIGTREETECH's Octopus 1.1 is a solid board that provides ample power sources and signal pins. This includes six PWM pins with a jumper to change the voltage level from 24V to 12V or 5V, eliminating my need for buck converters. It also (so far) hasn't blown out any of my equipment or itself and is similarly priced to the SKR 2.

The Octopus will not fit the existing control cases I had already printed; I also had a several improvements in mind for Steve's case concept.

### Building the OmniBox

This is my second control case for the Octopus designed around general shape and layout from Steve's V3 case. I kept full compatibility only with the original display screens. Lids should be easy to modify to fit, as they maintain the same overall dimensions (note that the screw holes are M3 now, however).

Templates are provided for all trays and panels to allow further customization and support for new products.

### Other Improvements

These are other changes and improvements present in OmniBox:

- Buck converters, solid state relays (SSRs), and other additional hardware can be mounted below the board instead of above.
- The rear panel is larger and covers most of the base.
- The base is approximately 1.2" shorter; wires are meant to exit from the back or top of the control case.
- The case is designed to draw air upwards and out past the MCU drivers, providing effective cooling with two 40mm fans.
- Some screws that were M4 are now M3.

![right side view](img/gallery_0.9.5/close.png)