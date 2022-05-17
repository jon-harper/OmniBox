---
title: About
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

Welcome to the documentation for the OmniBox, a modular control case for 3D printing. This project is conceptually derived from Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751) V3 footprint; it is a unique design with a lower base height and compatibility with newer, larger boards like BIGTREETECH's Octopus.

## Background

### The Requirements

I print quite a bit of ABS using enclosures with lights, fans, and a thermistor. With a 24V power supply, this requires multiple buck converters to control the lights and fans. My control boxes for these enclosures were cramped—the buck converters kept me from accessing the board wiring.

Additionally, after multiple DOA and failed BIGTREETECH SKR 2 boards, I had to find another board to settle on.

### Switching to the Octopus

BIGTREETECH's Octopus 1.1 is a solid board that provides ample power sources and signal pins, eliminating my need for buck convertors. It also (so far) hasn't blown out any of my equipment or itself.

The Octopus will not fit the existing control cases I had already printed; I also had a several improvements in mind for Steve's case concept.

### Building the OmniBox

This is my second control case for the Octopus designed around general shape and layout from Steve's V3 case. I kept full compatibility only with the original display screens. Lids should be easy to modify to fit, as they maintain the same overall dimensions (note that the screw holes are M3 now, however). Templates are provided for further customization, including new boards or mounts for SSRs and MOSFETs.

Other changes:

- Buck converters and other add-ons are mounted below the board instead of above.
- The rear panel is larger and covers most of the base.
- The base is much shorter; wires are meant to exit from the back or top of the control case.
- Case edges are chamfered instead of filleted.
- Some screws that were M4 are now M3.
- The case is designed to draw air upwards and out past the MCU drivers, providing effective cooling with two 40mm fans.

![right side view](img/gallery/view_right.jpg)