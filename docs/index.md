---
title: Overview
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

## About OmniBox

OmniBox is a 3D printable, modular electronics case for 3D printers. OmniBox comes with support for a wide variety of parts and includes templates to add support for new ones. 

This project is derived from Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751) V3 footprint.

!!! info
    To switch between :material-lightbulb-on: Light and :material-lightbulb-off-outline: Dark reading mode, click the icon next to the search box.

<figure markdown>
  [![gallery of OmniBox part combinations][2]][2]
  <figcaption>Gallery of several possible OmniBox configurations</figcaption>
</figure>



## Quick Links

### Getting Started

[:material-television-guide: Visual Guided Tour](tour.md){ .md-button }

[:octicons-checklist-24: Supported Part List](support/index.md){ .md-button }

[:octicons-list-ordered-24: Bill of Materials](bom.md){ .md-button }

### Printing

[:material-printer-3d-nozzle: Printing Guide](printing.md){ .md-button }

[:material-github: GitHub with STLs](https://github.com/jon-harper/OmniBox){ .md-button }

### Assembly

[:material-directions: Assembly Guide](assembly/index.md){ .md-button }


## Current Status

Although OmniBox has not reached version 1.0, it is mature enough for everyday use. A complete OmniBox made of parts from one release is tested to fit and work. Trays and panels are compatible with all releases (see [Version Stability Guarantee](#version-stability-guarantee) below for details).

The [Version History](history/index.md) page contains information on the latest release, fixes, new features, and known issues.

## Version Stability Guarantee

Printing OmniBox is an investment. The way trays and panels attach to OmniBox between versions is carefully fixed. The result is a modular case that can be upgraded piece by piece.

!!! note
    Prior versions of this page had the Version Stability Guarantee fully in place. I have relaxed it until version 1.0 in order to deprecate M4-mounted parts.

    No reprinting is necessary to use legacy M4 panels with M3 screws.

### Currently

Until version 1.0, it is still possible for changes to be made to the design of panels and trays. If this happens, parts using the old method are considered "deprecated". Deprecated parts remain available and supported through the release of 1.0 but will be removed after. 

Every effort is made to avoid incompatibilities between versions, and so far all deprecated printed parts remain compatible with new cases.

### Version 1.0

With version 1.0, changes may be made that cause deprecated parts to lose compatibility. This is a final chance to "lock in" the design.

At this point, OmniBox releases will come with a **Version Stability Guarantee**:

The way that Core components fit together and panels and trays attach to the case will be "frozen" and stable. If you choose to print a newer version of a Core part, no panels or trays will need to be reprinted. New products added in future releases can likewise be used in the Core case body from a prior release.

### Compatibility Example

As an example, the design for CPU trays was modified for 0.9.9. Version 0.9.8-style trays are considered deprecated. The following shows how trays and Core cases and compatible with one another.

| CPU Tray / Core Case  | 0.9.8              | 0.9.9 - 1.0        | 1.0 and Later        |
|-----------------------|:------------------:|:------------------:|:--------------------:|
| **Old (0.9.8) trays** | :white_check_mark: | :white_check_mark: | :x:                  |
| **New (0.9.9) trays** | :x:                | :white_check_mark: | :white_check_mark:   |

See the [Guided Tour](tour.md) to see how the components of an OmniBox fit together in practice.


[1]: img/gallery_0.9.8/front_left.png
[2]: img/gallery_0.9.8.1/gallery_high.png
[3]: img/gallery_0.9.8/oscar_right.jpg
[4]: history/index.md