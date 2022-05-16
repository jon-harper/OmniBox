---
title: About
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

Welcome to the OmniBox documentation, a modular control box for 3D printing. This project is conceptually derived from Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751) and maintains compatiblity with respect to display screens. Numerous improvements are included for a smaller footprint and easier assembly.

![right side view](img/gallery/view_right.jpg)

## Background

### The SKR 2 Fiasco

I had a catastrophic failure of multiple BIGTREETECH SKR 2 boards in a row. I print a lot of ABS, which means controlling an enclosure with lights, fans, etc.--and that equates to a lot of buck converters.

### Switching to the Octopus

BIGTREETECH's Octopus 1.1 is a solid board that provides ample power sources and signal pins, eliminating the need for numerous buck convertors. It also (so far) hasn't blown out any of my equipment or itself. Unfortunately, the existing control cases I had printed didn't fit the Octopus; I also had a few ideas for changes and improvements. This is my second control case for the Octopus centered around the footprint used by Steve's V3 case. 


### Building the OmniBox

Since the source is not availabe for the base or main body, I redesigned the case from scratch, keeping compatibility only with the original display screens. Edges are now chamfered on flat surfaces to give cleaner finishes and fewer fasteners are needed overall. Lids should be easy to modify to fit, as they maintain the same overall dimensions. Templates are provided for further customization, including new boards or mounts for SSRs and MOSFETs.
