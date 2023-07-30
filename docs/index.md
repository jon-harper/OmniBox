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
[:octicons-list-ordered-24: Bill of Materials][bom]
[:octicons-checklist-24: Supported Products][support]
</div>
</div>
<div markdown class="jh-card">
### Guides

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[:material-printer-3d-nozzle: Printing Guide][printing]
[:material-directions: Assembly Guide][assembly]
[:material-transfer-up: Upgrade Guide][upgrade]
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


[gallery_thumb]: img/examples/0.9.10/render_thumb.jpg
[gallery]: img/examples/0.9.10/render.jpg

[current_release]: history/index.md "Version History (Current Release)"
[tour]:     tour.md                 "Guided Tour"
[support]:  support/index.md        "Supported Parts List"
[bom]:      bom.md                  "Bill of Materials"
[printing]: printing.md             "Printing Guide"
[assembly]: assembly/index.md       "Assembly Guide"
[license]:  license.md              "Contributing and License"
[upgrade]:  upgrade/index.md        "Upgrading Overview"