---
title: Overview
summary: OmniBox documentation landing page
authors: Jon Harper
date: 2022-05-15
---

!!! info
    To switch between :material-lightbulb-on: Light and :material-lightbulb-off-outline: Dark reading mode, click the icon next to the search box.

## About OmniBox

OmniBox is 3D printable, modular electronics case for 3D printers. OmniBox comes with [support][support] for a wide variety of parts and includes templates to add support for new ones. 

This project is derived from Steve Burcham's [Stand Alone Main Control Case][bgdog] V3 footprint. It released under the [MIT License][license].

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

OmniBox is currently pre-1.0 but mature enough for everyday use. A complete OmniBox made of parts from one release is tested to fit and work.

See the [Version History][current_release] page for information on the latest release, fixes, new features, and known issues.

## Version Stability Guarantee

Printing OmniBox is a time investment. This makes incompatibility between versions difficult; upgrading one printed part should not require others to be reprinted. Thankfully, OmniBox is highly modular and can be upgraded piece by piece.

!!! note
    Prior versions of this page had the Version Stability Guarantee fully in place. I have relaxed it until version 1.0 to deprecate M4-mounted parts and to improve the Core design before version 1.0.

    No reprinting is necessary to use deprecated M4 panels with M3 screws. Until version 1.0, component mounts will be issued with STLs for both M3 and M4 screws.

### Current Release (Pre-1.0)

Parts issued in a release pre-1.0 will be supported through the development process to 1.0. Some parts may become deprecated but will still be available. Every effort is made to avoid incompatibilities between versions.

### After Version 1.0

Starting with version 1.0, OmniBox will have a "Version Stability Guarantee":

The Core printed components of OmniBox will be "stable" or "frozen" in how they connect with with other parts. If you choose to print a newer version of a Core part, no panels or trays will need to be reprinted.

See the [Guided Tour][tour] to see how this works in practice.

[gallery_thumb]: img/examples/gallery_thumb.png
[gallery]: img/examples/gallery.png
[current_release]: history/index.md "Version History (Current Release)"

[tour]: tour.md "Guided Tour"
[support]: support/index.md "Supported Parts List"
[bom]: bom.md "Bill of Materials"
[printing]: printing.md "Printing Guide"

[assembly]: assembly/index.md "Assembly Guide"
[license]: license.md