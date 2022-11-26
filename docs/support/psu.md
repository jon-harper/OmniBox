---
title: Power Supplies/PSUs
summary: List of power supplies supported by OmniBox.
authors: Jon Harper
date: 2022-07-22
---

This page lists power supplies (PSUs) currently supported by OmniBox.

<figure markdown>
  [![front left render][psu]{ width="480" }][psu]
  <figcaption>Power supplies are mounted underneath the case body.</figcaption>
</figure>

PSU trays are found in the [:material-git: `/Trays/PSU`][git_psu] git folder. Expanding support for new power supplies is an area of focus; a template will be available in future releases.

<!-- Template
[![product picture][img_btt_skr_3]{width="200"}][img_]

[:material-git: Files: ][git_]

[:material-cart: Product Link][bom_]
 -->

## Mean Well

There are several brands of clones, usually using the same model number. The model common of these is the Landy LRS-350-24. These clones are generally compatible with the Mean Well trays.

### LRS-350 Series

[:material-git: LRS-350][git_rpi_3b_plus]{ .md-button }

[:material-cart: Product Link][bom_lrs350]{ .md-button }

[![product picture][img_lrs_350]{width="200"}][img_lrs_350]

- Materials: 4x M4 x 6mm

### RSP-500 Series

!!! caution "Fit Test Pending: [:material-git: Issue #14](https://github.com/jon-harper/OmniBox/issues/14)"

[:material-git: RSP-500][git_psu_rsp500]{ .md-button }

[:material-cart: Product Link][bom_rsp500]{ .md-button }

[![product picture][img_rsp_500]{width="200"}][img_rsp_500]

- Materials: 8x M4 x 6mm
- Notes: Requires a [:material-git: base extension][git_base_extension].

[psu]: ../img/components/psu.png
[img_lrs_350]: ../img/parts/mw_lrs_350_24.jpg
[img_rsp_500]: ../img/parts/mw_rsp_500_24.jpg