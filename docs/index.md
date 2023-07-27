---
title: Overview
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
hide: toc
---
# OmniBox v{{ extra.meta.version }}

!!! tip
    To change documentation versions, select a version number from the drop down box at the top of the page.

    To switch between :material-lightbulb-on: Light and :material-lightbulb-off-outline: Dark reading mode, click the icon next to the search box.

## About OmniBox

OmniBox is a 3D printable, modular electronics case for 3D printers. It supports a wide variety of parts and includes templates to add new ones. 

This project is loosely derived from Steve Burcham's [Stand Alone Main Control Case][bgdog] V3. It is released under the [MIT License][license] and is distributed free of charge.


<figure markdown>
  [![gallery of OmniBox part combinations][gallery_thumb]][gallery]
  <figcaption>Renders of a finished OmniBox.</figcaption>
</figure>

## Quick Links

<div markdown class="jh-grid-container jh-grid-3">
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

OmniBox is mature enough for everyday use. A complete OmniBox made of parts from one release is tested to fit and work. Trays and panels are compatibile between releases (see [Compatibility and Upgrades](#compatibility-and-upgrades) for details).

The [Version History][current_release] page contains information on the latest release, fixes, new features, and known issues.

## Compatibility and Upgrades

A finished OmniBox is an investment that can grow with your needs. The Core case is designed for flexibility and reuse.

Until version 1.0, changes *may* occur between releases in how a given panel or tray mounts. If this happens, parts using the old method are considered deprecated. Deprecated parts remain available and supported through the release of 1.0 but will be removed afterwards.

Every effort is made to avoid incompatibilities between versions.

!!! example
    Early releases used M4 screws to mount MCU trays to the case; new trays use M3 screws. The "M4-style" panels were deprecated but remain available.

### Version 1.0

Version 1.0 is a final chance to "lock in" the design. After version 1.0, OmniBox releases will come with a **Version Stability Guarantee**:

If you choose to print a newer version of a Core part, no panels or trays will need to be reprinted. New products added in future releases can likewise be used in the Core case body from a prior release.

### Compatibility Example

As an example, the design for CPU trays was modified for version 0.9.9. Old-style trays are considered deprecated but may still work.

The following shows how trays and Core cases how support works for deprecated panels and trays—a checkmark indicates the part is supported.

|               | 0.9.8      | 0.9.9 until 1.0    | 1.0+                         |
|---------------|:----------:|:------------------:|:----------------------------:|
| **Old trays** | :white_check_mark: | :white_check_mark: | :x:                  |
| **New trays** | :x:                | :white_check_mark: | :white_check_mark:   |

See the [Guided Tour][tour] to see how the components of an OmniBox fit together in practice.

[gallery_thumb]: img/examples/0.9.10/render_thumb.jpg
[gallery]: img/examples/0.9.10/render.jpg

[current_release]: history/index.md "Version History (Current Release)"
[tour]:     tour.md                 "Guided Tour"
[support]:  support/index.md        "Supported Parts List"
[bom]:      bom.md                  "Bill of Materials"
[printing]: printing.md             "Printing Guide"
[assembly]: assembly/index.md       "Assembly Guide"
[license]:  license.md              "Contributing and License"