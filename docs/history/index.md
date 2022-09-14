---
title: 0.9.8.1 Release (Current)
summary: Changelog for the current and past releases of OmniBox
authors: Jon Harper
date: 2022-08-24
---

The current release is 0.9.8.1, released on 2022-09-xx.

<!-- ## Fixes -->

<!-- ### Completed Requests

| Hardware | Mount Location(s) | Notes |
|----------|-------------------|-------| -->

### Core Improvements

- Print time and material usage is slightly reduced for the front and rear base components.

## Panels and Trays

- Lids for spools!
    - An adaptation of my [Tighter T.U.S.H. spool holder][2] (a remix of the original T.U.S.H.).
    - It mounts on a lid that integrates the spool holder guide.
    - The guide makes the spool holder adjustable to spool width (up to about 120mm).
- Lids for dryboxes!
    - A lid for [Rubbermaid 21 cup containers][1].
    - These containers are about $5 each at Ace Mart.
    - There are often clones of these on Amazon that are slightly more expensive (about $8-10 ea).
    - May have lids for generic containers in the near future as a user contribution.
- Raspberry Pi tray now have a version with a 6-pin Micro Fit 3 panel mount cutout.

### Experimental Hardware Support

These parts still need to be tested for fit and other issues.

| Hardware | Mount Location(s) | Notes |
|----------|-------------------|-------|
| Mean Well RSP-500 power supply | Main body | For the Ender 5 Plus |
| 92mm fans | Rear panel, lid | 25mm thickness; no compatible mount yet. |

### New Hardware Support

This hardware is now fit-tested as working.

| Hardware | Mount Location(s) | Notes |
|----------|-------------------|-------|
| Fotek SSR-60 DA solid state relay | Lower bay | |
| Raspberry Pi TFTs | Display mount or half-lid | See below. |

Note: There are two half-length lids for Raspbery Pi TFTs. Use the XL half-lid for the official 7" and similarly large TFTs. Smaller (e.g., 5") TFTs will fit on the standard half-lid.

## Documentation & Repository

- Documentation site has a modified color scheme and fonts for readability.
- New dark theme for the doc site.
- Implemented several Material for Mkdocs features, including icons to help with part identification.
- Improved documentation readability.

## Known Issues

- The front main body with a 40mm intake fan partially obscures a mounting hole for the base to the main body. This leave seven (7) other mount points and is not a significant issue. The hole can safely be left empty.

## Gallery

| Images and Renders | |
|---|---|
| Lid with built-in spool roller | [![rendering of a case with a spool holder on top][3]][3] |
| Stackable case lid | [![case with a stackable lid][4]][4] |


[1]: https://www.amazon.com/Rubbermaid-LEPUSEMTE469-711717429496-Container-Everyday/dp/B00XJRMW5M
[2]: https://www.thingiverse.com/thing:4737072
[3]: ../img/gallery_0.9.8.1/spool_holder.png
[4]: ../img/gallery_0.9.8.1/stackable_lid.jpg