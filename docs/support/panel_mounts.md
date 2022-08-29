---
title: Panel Mounts
summary: A list of panel mounted components supported by OmniBox
authors: Jon Harper
date: 2022-07-22
---

## Using Panel Mounts

 Connector panel mounts will typically be on the rear panel and connect with the printer. Extensions can be mounted on the front or rear and are typically for SD Cards and USB ports.

### :material-alpha-p-box-outline: :material-alpha-f-box: Front Panels

The front panel is long and slim and can be used for mounting small hardware ports. The most common examples are SD Card extensions and USB extensions. You can find these files in the [Panels/Front Panel][8] git folder.

The example below has a Micro SD extension and USB-C extension with slat-style vents.

![front panel example](../img/gallery_0.9.7/front_panel.png)

### :material-alpha-p-box-outline: :material-alpha-r-box: Rear Panels

Rear Panels are the most customizable part of OmniBox. They can mount connectors and fans and modified to suit each end user. There are also a number of generic templates available in the [Panels/Rear Panel][7] git folder.

This rear panel uses Molex Micro Fit 3 connectors. In addition, it has a cutout for a 60mm fan and USB-C extension.

![rear panel example](../img/gallery_0.9.7/panel_mounts.png)

## Supported Hardware

| Connector or Extension | Typical Location | Notes |
|------------------------|----------|-------|
| [MicroSD panel mount extension][5] | Front | |
| [USB B panel mount extension][4] | Front or Rear | Right angle connector fits most boards more easily. |
| [USB C panel mount extension][3] | Front or Rear | |
| [JST SM panel mount connectors][2] | Rear | 2-5 pins |
| [Molex Micro Fit 3.0 connectors][1] | Rear | Supported up to [2-row, 16-position][6]. |

[1]:  https://www.digikey.com/en/htmldatasheets/production/1626160/0/0/1/0430300007.html
[2]:  https://www.amazon.com/gp/product/B07D9HRDT6
[3]:  https://www.amazon.com/Poyiccot-Extension-Female-Extender-Straight/dp/B086W2R8Z6
[4]:  https://www.amazon.com/gp/product/B071P2BGK5
[5]:  https://www.amazon.com/gp/product/B07YYSP5F5
[6]: https://www.digikey.com/en/products/detail/molex/0430200200/252490
[7]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel
[8]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Front%20Panel