---
title: Overview
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---
## About OmniBox

OmniBox is a 3D printable, modular electronics case for 3D printers. It supports a wide variety of parts and includes templates to add new ones. 

This project is derived from Steve Burcham's [Stand Alone Main Control Case][bgdog] V3 footprint. It is released under the [MIT License][license].

!!! info
    To switch between :material-lightbulb-on: Light and :material-lightbulb-off-outline: Dark reading mode, click the icon next to the search box.

<figure markdown>
  [![gallery of OmniBox part combinations][gallery_thumb]][gallery]
  <figcaption>Gallery of several possible OmniBox configurations</figcaption>
</figure>

## Quick Links

### Getting Started

[:material-television-guide: Visual Guided Tour][tour]{ .md-button }

[:octicons-checklist-24: Supported Parts List][support]{ .md-button }

[:octicons-list-ordered-24: Bill of Materials][bom]{ .md-button }

### Printing

[:material-printer-3d-nozzle: Printing Guide][printing]{ .md-button }

[:material-github: GitHub with STLs][git_home]{ .md-button }

### Assembly

[:material-directions: Assembly Guide][assembly]{ .md-button }

## Current Status

Although OmniBox has not reached version 1.0, it is mature enough for everyday use. A complete OmniBox made of parts from one release is tested to fit and work. Trays and panels are compatible with all releases (see [Version Stability Guarantee](#version-stability-guarantee) for details).

The [Version History][current_release] page contains information on the latest release, fixes, new features, and known issues.

## Version Stability Guarantee

Printing OmniBox is an investment. The way trays and panels attach to OmniBox between versions is carefully fixed. The result is a modular case that can be upgraded piece by piece.

!!! note
    Prior versions of this page had the Version Stability Guarantee fully in place. I have relaxed it until version 1.0 in order to deprecate M4-mounted parts.

    No reprinting is necessary to use legacy M4 panels with M3 screws.

### Currently (Before Version 1.0)

Prior to version 1.0, changes may still be made to how panels and trays interface with the Core case. If this happens, parts using the old method are considered "deprecated". Deprecated parts remain available and supported through the release of 1.0 but will be removed after. 

Every effort is made to avoid incompatibilities between versions.

Thus far, all deprecated printed parts remain compatible with new cases.

### Version 1.0

With version 1.0, changes may be made that cause deprecated parts to lose compatibility. This is a final chance to "lock in" the design.

### After Version 1.0

Starting with version 1.0, OmniBox will have a "Version Stability Guarantee":

The Core printed components of OmniBox will be "stable" or "frozen" in how they connect with with other parts. If you choose to print a newer version of a Core part, no panels or trays will need to be reprinted. New products added in future releases can likewise be used in the Core case body from a prior release.

!!! example
    As an example, the design for CPU trays was modified for 0.9.9.
    
    A CPU tray from 0.9.8 will:

    - Work with a case from 0.9.9 and
    - May not work with version 1.0.

    A version 0.9.9 case:

    - Can use CPU trays from any release.

See the [Guided Tour][tour] to see how the components of an OmniBox fit together in practice.

[gallery_thumb]: img/examples/gallery_thumb.png
[gallery]: img/examples/gallery.png

[current_release]: history/index.md "Version History (Current Release)"
[tour]:     tour.md                 "Guided Tour"
[support]:  support/index.md        "Supported Parts List"
[bom]:      bom.md                  "Bill of Materials"
[printing]: printing.md             "Printing Guide"
[assembly]: assembly_v2/index.md       "Assembly Guide"
[license]:  license.md              "Contributing and License"