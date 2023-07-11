---
title: Power Supplies (PSUs)
summary: List of power supplies supported by OmniBox.
authors: Jon Harper
date: 2022-07-22
---

This page lists power supplies (PSUs) currently supported by OmniBox.

<figure markdown>
  [![front left render][psu]{ width="480" }][psu]
  <figcaption>Power supplies are mounted underneath the case body.</figcaption>
</figure>

PSU trays are found in the [:material-git: `/Trays/PSU`][git_psu] git folder. A template will be available in a future release.

<!-- Template
<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files ][git_]

- Materials: 
- Switch Compatibility:
- Notes:
</div>
<div markdown class="jh-grid-img">
[:material-cart: Product Link][bom_]

[![product picture][img_]][img_]
</div></div>
 -->

## Mean Well

!!! note "Note: Mean Well Clones"
    There are several brands of clones, usually using the same model number as Mean Well. The most common of these is the Landy LRS-350-24. These clones are generally compatible with the Mean Well trays.

### LRS-350 Series

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
[:material-git: Files][git_psu_lrs350]{ .md-button }

- Materials: 4x M4 x 6mm BHCS or SHCS
- Switch Compatibility: Toggle or rocker
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
- Switch Compatibility: Rocker
</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_lrs450]{ .md-button }

[![product picture][img_lrs_450]{width="200"}][img_lrs_450]
</div>
</div>

### LRS-600 Series

{{ issue_tag(116) }}

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
{{ git_button("git_psu_lrs600") }}

- Materials: 4x M4 x 6mm BHCS or SHCS
- Switch Compatibility: Rocker
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
- Switch Compatibility: Rocker
- Notes: Extends 10mm below the base. Requires a [:material-git: base extension][git_base_extension], Unified Extended Base, or other method of raising the case.

</div>
<div markdown class="jh-grid-para">
[:material-cart: Product Link][bom_rsp500]{ .md-button }

[![product picture][img_rsp_500]{width="200"}][img_rsp_500]
</div>
</div>

### SE-450 Series

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Files][git_psu_se450]{ .md-button }

- Materials: 8x M4 x 6mm BHCS or SHCS
- Switch Compatibility: Rocker
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
[img_lrs_350]: ../img/parts/mw_lrs_350_24.webp
[img_rsp_500]: ../img/parts/mw_rsp_500_24.webp
[img_rs_25_5]: ../img/parts/rs_25_5.webp
[img_lrs_450]: ../img/parts/lrs_450_24.webp
[img_lrs_600]: ../img/parts/lrs_600_24.webp
[img_se_450]: ../img/parts/se_450_24.webp