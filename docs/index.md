---
title: Overview
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

## About OmniBox

OmniBox is a 3D printable, modular electronics case for 3D printers. It supports a wide variety of parts and includes templates to add new ones. 

This project is derived from Steve Burcham's [Stand Alone Main Control Case][bgdog] V3 footprint. It is released under the [MIT License][license].

!!! tip
    To change documentation versions, select a version number from the drop down box at the top of the page.

    To switch between :material-lightbulb-on: Light and :material-lightbulb-off-outline: Dark reading mode, click the icon next to the search box.

<figure markdown>
  [![gallery of OmniBox part combinations][gallery_thumb]][gallery]
  <figcaption>A gallery of several OmniBox configurations.</figcaption>
</figure>

## Quick Links

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-card">
### Getting Started

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[:material-television-guide: Visual Guided Tour][tour]
[:octicons-checklist-24: Supported Parts List][support]
[:octicons-list-ordered-24: Bill of Materials][bom]
</div>
</div>
<div markdown class="jh-card">
### Printing & Assembly

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[:material-printer-3d-nozzle: Printing Guide][printing]
[:material-git: Printable Files on GitHub][git_home]
[:material-directions: Assembly Guide][assembly]
</div>
</div>
<div markdown class="jh-card">
### Community Links

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[:simple-discord: Discord Server][discord]
[:simple-github: GitHub Discussions][git_discussions]
</div>
</div>
</div>

## Current Status

Although OmniBox has not reached version 1.0, it is mature enough for everyday use. A complete OmniBox made of parts from one release is tested to fit and work. Trays and panels are compatibile between releases (see [Compatibility and Upgrades](#compatibility-and-upgrades) for details).

The [Version History][current_release] page contains information on the latest release, fixes, new features, and known issues.

## Compatibility and Upgrades

Printing OmniBox is an investment. The way trays and panels attach to OmniBox between versions is carefully fixed. The result is a modular case that can be upgraded piece by piece.

!!! note
    Prior versions of this page had the Version Stability Guarantee fully in place. I have relaxed it until version 1.0 to allow more design growth.

### Currently
<!-- TODO Reword -->
Until version 1.0, it is still possible for changes to be made to the design of panels and trays. If this happens, parts using the old method are considered "deprecated". Deprecated parts remain available and supported through the release of 1.0 but will be removed after. 

Every effort is made to avoid incompatibilities between versions, and so far all deprecated printed parts remain compatible with new cases.

!!! example
    Early releases used M4 screws to mount some panels to the case; new panels use M3 screws. The "M4-style" panels were deprecated but remain available.

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

See the [Guided Tour][tour] to see how the components of an OmniBox fit together in practice.

[gallery_thumb]: img/examples/gallery_thumb.png
[gallery]: img/examples/gallery.png

[current_release]: history/index.md "Version History (Current Release)"
[tour]:     tour.md                 "Guided Tour"
[support]:  support/index.md        "Supported Parts List"
[bom]:      bom.md                  "Bill of Materials"
[printing]: printing.md             "Printing Guide"
[assembly]: assembly/index.md       "Assembly Guide"
[license]:  license.md              "Contributing and License"