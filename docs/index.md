---
title: Overview
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

!!! info
    To switch between :material-lightbulb-on: Light and :material-lightbulb-off-outline: Dark reading mode, click the icon next to the search box.

## About OmniBox

OmniBox is 3D printable, modular electronics case for 3D printers. OmniBox comes with support for a wide variety of parts and includes templates to add support for new ones. 

This project is derived from Steve Burcham's [Stand Alone Main Control Case][bgdog] V3 footprint.

<figure markdown>
  [![gallery of OmniBox part combinations][2]][2]
  <figcaption>Gallery of several possible OmniBox configurations</figcaption>
</figure>

## Quick Links

### Getting Started

[:material-television-guide: Visual Guided Tour][11]{ .md-button }

[:octicons-checklist-24: Supported Parts List][12]{ .md-button }

[:octicons-list-ordered-24: Bill of Materials][13]{ .md-button }

### Printing

[:material-printer-3d-nozzle: Printing Guide][14]{ .md-button }

[:material-github: GitHub with STLs][git_home]{ .md-button }

### Assembly

[:material-directions: Assembly Guide][16]{ .md-button }

## Version Stability Guarantee

!!! note
    Prior versions of this page over-eagerly had the Version Stability Guarantee fully in place. I have relaxed it for now to deprecate M4-mounted parts and to improve the Core design before version 1.0.

Printing OmniBox is a time investment. This makes incompatibility between versions difficult; upgrading one printed part should not require others to be reprinted. Thankfully, OmniBox is highly modular and can be upgraded piece by piece.

### Current Release (Pre-1.0)

Parts issued in a release pre-1.0 will be supported through the development process to 1.0. Some parts may become deprecated but will still be available. Every effort is made to avoid deprecating parts.

### After Version 1.0

Starting with version 1.0, OmniBox will have a "Version Stability Guarantee":

The Core printed components of OmniBox will be "stable" or "frozen" in how they connect with with other parts. If you choose to print a newer version of a Core part, no panels or trays will need to be reprinted.

See the [Guided Tour][11] to see how this works in practice.

## Current Status

OmniBox is currently pre-1.0 but mature enough for everyday use. A complete OmniBox made of parts from one release is tested to fit and work.

See the [Version History][4] page for information on the latest release, fixes, new features, and known issues.

<figure markdown>
  [![front left render][1]{ width="640" }][1]
  <figcaption>Render of an OmniBox with a 3.5" TFT display.</figcaption>
</figure>

[1]: img/gallery_0.9.8/front_left.png
[2]: img/gallery_0.9.8.1/gallery_high.png
[3]: img/gallery_0.9.8/oscar_right.jpg
[4]: history/index.md "Version History (Current Release)"

[11]: tour.md "Guided Tour"
[12]: support/index.md "Supported Parts List"
[13]: bom.md "Bill of Materials"
[14]: printing.md "Printing Guide"

[16]: assembly/index.md "Assembly Guide"