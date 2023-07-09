---
title: Power Supplies (PSUs)
summary: List of power supplies supported by OmniBox.
authors: Jon Harper
date: 2022-07-22
---

This page lists power supplies (PSU) currently supported by OmniBox.

<figure markdown>
  [![front left render][psu]{ width="480" }][psu]
  <figcaption>Power supplies are mounted underneath the case body.</figcaption>
</figure>

PSU trays are found in the [:material-git: `/Trays/PSU`][git_psu] git folder. Expanding support for new power supplies is an area of focus; a template will be available in future releases.

!!! note "Note: M4 Screws"
    Power supplies will only work with M4 *button head* screws. Socket head cap screws have heads that are too tall to fit the PSU in the case.

<!-- Template
<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files: ][git_]

[:material-cart: Product Link][bom_]

- Materials: 
</div>
<div markdown class="jh-grid-img">
[![product picture][img_]][img_]
</div>
</div>
 -->

## Mean Well

There are several brands of clones, usually using the same model number. The model common of these is the Landy LRS-350-24. These clones are generally compatible with the Mean Well trays.

### LRS-350 Series

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_psu_lrs350]{ .md-button }

- Materials: 4x M4 x 6mm BHCS or SHCS
- Switch Compatility: Toggle or rocker
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_lrs350]{ .md-button }

[![product picture][img_lrs_350]{width="200"}][img_lrs_350]
</div>
</div>

### LRS-450 Series

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_psu_lrs450]{ .md-button }

- Materials: 4x M4 x 6mm BHCS or SHCS
- Switch Compatility: Rocker
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_lrs450]{ .md-button }

[![product picture][img_lrs_450]{width="200"}][img_lrs_450]
</div>
</div>

### LRS-600 Series

!!! caution "Fit Test Pending: See Issue [#116](https://github.com/jon-harper/OmniBox/issues/116)"

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_psu_lrs600]{ .md-button }

- Materials: 4x M4 x 6mm BHCS or SHCS
- Switch Compatility: Rocker
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_lrs600]{ .md-button }

[![product picture][img_lrs_600]{width="200"}][img_lrs_600]
</div>
</div>

### RSP-500 Series

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Files][git_psu_rsp500]{ .md-button }

- Materials: 8x M4 x 6mm BHCS or SHCS
- Switch Compatility: Rocker
- Notes: Extends 10mm below the base. Requires a [:material-git: base extension][git_base_extension], Unified Extended Base, or other method of raising the case.

</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_rsp500]{ .md-button }

[![product picture][img_rsp_500]{width="200"}][img_rsp_500]
</div>
</div>

### SE-450 Series

!!! caution "Fit Test Pending: See Issue [#119](https://github.com/jon-harper/OmniBox/issues/119)"

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Files][git_psu_se450]{ .md-button }

- Materials: 8x M4 x 6mm BHCS or SHCS
- Switch Compatility: Rocker
- Notes: Extends 10mm below the base. Requires a [:material-git: base extension][git_base_extension], Unified Extended Base, or other method of raising the case.

</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_se450]{ .md-button }

[![product picture][img_se_450]{width="200"}][img_se_450]
</div>
</div>

## Lower Bay PSUs

### Mean Well RS-25-5

The RS-25-5 is a common second power supply for SBCs and fits on a lower bay tray.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

!!! info "Contributed by [edgy][contrib_edgy]"

[:octicons-link-external-24: Printables - Mean Well RS-25-5][src_rs_25_5]{ .md-button }

[:material-cart: Product Link][bom_rs_25_5]{ .md-button }

- Materials: 6x M4 x 6mm screws
- Notes: This is a lower bay tray.
</div>
<div markdown class="jh-grid-img">
[![product picture][img_rs_25_5]{width="200"}][img_rs_25_5]
</div>
</div>

[psu]: ../img/components/psu.webp
[img_lrs_350]: ../img/parts/mw_lrs_350_24.jpg
[img_rsp_500]: ../img/parts/mw_rsp_500_24.jpg
[img_rs_25_5]: ../img/parts/rs_25_5.png
[img_lrs_450]: ../img/parts/lrs_450_24.png
[img_lrs_600]: ../img/parts/lrs_600_24.png
[img_se_450]: ../img/parts/se_450_24.png