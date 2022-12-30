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

!!! note "Note: M4 Screws"
    Power supplies will only work with M4 *button head* screws. Socket head cap screws have heads that are too tall to fit the PSU in the case.

<!-- Template
[![product picture][img_btt_skr_3]{width="200"}][img_]

[:material-git: Files: ][git_]

[:material-cart: Product Link][bom_]
 -->

## Mean Well

There are several brands of clones, usually using the same model number. The model common of these is the Landy LRS-350-24. These clones are generally compatible with the Mean Well trays.

### LRS-350 Series

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: LRS-350 Files][git_rpi_3b_plus]{ .md-button }

[:material-cart: Product Link][bom_lrs350]{ .md-button }

- Materials: 4x M4 x 6mm button head screws
</div>
<div markdown class="jh-grid-img">
[![product picture][img_lrs_350]{width="200"}][img_lrs_350]
</div>
</div>

### RSP-500 Series

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
!!! caution "Fit Test Pending: [:material-git: Issue #14](https://github.com/jon-harper/OmniBox/issues/14)"

[:material-git: RSP-500 Files][git_psu_rsp500]{ .md-button }

[:material-cart: Product Link][bom_rsp500]{ .md-button }

- Materials: 8x M4 x 6mm button head screws
- Notes: Requires a [:material-git: base extension][git_base_extension].
</div>
<div markdown class="jh-grid-img">
[![product picture][img_rsp_500]{width="200"}][img_rsp_500]
</div>
</div>

[psu]: ../img/components/psu.png
[img_lrs_350]: ../img/parts/mw_lrs_350_24.jpg
[img_rsp_500]: ../img/parts/mw_rsp_500_24.jpg