---
title: About
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

Welcome to the documentation for the OmniBox, a modular control case for 3D printing.

This project is conceptually derived from Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751) V3 footprint; it is a unique design with a lower base height and compatibility with newer, larger MCU boards like BIGTREETECH's Octopus.

## Background

### The Requirements

I print quite a bit of ABS using enclosures with lights, fans, and a thermistor. As 24V is the common DC voltage for 3D printers right now, each 12V independantly-controllable or PWM device such as a fan or light strip needs a buck converter. My control boxes for these enclosures were cramped—the three or more buck converters mounted over the MCU kept me from accessing the wiring underneath.

Additionally, after multiple DOA and failed BIGTREETECH SKR 2 boards, I urgently had to find another board to settle on. Enter the Octopus, which I had already used on another project.

### Switching to the Octopus

BIGTREETECH's Octopus 1.1 is a solid board that provides ample power sources and signal pins, eliminating my need for buck converters. It also (so far) hasn't blown out any of my equipment or itself and is similarly priced to the SKR 2.

The Octopus will not fit the existing control cases I had already printed; I also had a several improvements in mind for Steve's case concept.

### Building the OmniBox

This is my second control case for the Octopus designed around general shape and layout from Steve's V3 case. I kept full compatibility only with the original display screens. Lids should be easy to modify to fit, as they maintain the same overall dimensions (note that the screw holes are M3 now, however). Templates are provided for further customization, including new boards or mounts for SSRs and MOSFETs.

Other changes:

- Bucks, SSRs, and other additional hardware is mounted below the board instead of above.
- The rear panel is larger and covers most of the base.
- The base is approximately 1.5" shorter; wires are meant to exit from the back or top of the control case.
- The case is designed to draw air upwards and out past the MCU drivers, providing effective cooling with two 40mm fans.
- Some screws that were M4 are now M3.

![right side view](img/gallery/view_right.jpg)