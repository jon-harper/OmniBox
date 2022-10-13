---
title: 0.9.9 Release (Current)
summary: Changelog for the current and past releases of OmniBox
authors: Jon Harper
date: 2022-10-09
---

!!! tip
    Want to know more about OmniBox and what's next? Follow [@jonspaceharper on :material-twitter: Twitter][twitter]

The current release is 0.9.9, released on 2022-10-??.

<!-- ### Completed Requests

| Hardware | Mount Location(s) | Notes |
|----------|-------------------|-------| -->

## New Features

- [Issue #14][1]: Universal power supply mount
- Main body zip tie anchors added:
    - Six (6) added to crossbar
    - Four (4) added to front main body (under MCU pillars)
    - Twelve (12) added to rear main body
        - Four (4) under MCU pillars
        - Six (6) above MCU pillars
        - Two (2) by PSU wiring cutout
- Redesigned side vents for main body:
    - Easier print
    - Looks rad
- Base now has three front vents, all with 40mm fan mounts

### Experimental Hardware Support

These parts still need to be tested for fit and other issues.

| Hardware | Mount Location(s) | Notes |
|----------|-------------------|-------|
| Mean Well RSP-500 power supply | Main body | For the Ender 5 Plus |
| 92mm fans | Rear panel, lid | 25mm thickness; no compatible mount yet. |

### New Hardware Support

| Hardware | Mount Location(s) | Notes |
|----------|-------------------|-------|
| Wago 221 Lever Nuts | Lower Bay | 3-wire and 5-wire |

## Fixes

- [Issue #18][2]: Fan mount blocks screw hole for mounting base
    - Fan mount moved left and up as part of intake redesign
- [Issue #35][3]: IEC socket hex nut is hard to reach
    - Removed hex nuts
    - Screws thread directly in plastic now
- [Issue #33][4]: Base zip tie anchors need adjustment
    - Removed rearmost zip tie that was troublesome
    - Adjusted position of others
- [Issue #39][5]: Display screen partially blocks two front main body/base screws
    - Added cutout for access

## Documentation & Repository

- Documentation site
    - Added tooltips to links
    - Consolidated external links to a reference page for convenience
- Repository
    - Added `/include` subfolder for external documentation files

## Known Issues


## Gallery

<figure markdown>
  [![front right render][11]{ width="480" }][11]
  <figcaption>The CPU bay has moved to the rear. The power supply has additional ventilation in front.</figcaption>
</figure>

<figure markdown>
  [![front left render][12]{ width="480" }][12]
  <figcaption>There is a matching bay on the opposite side, as well. Also note the new fan intake.</figcaption>
</figure>

<figure markdown>
  [![front right render][14]{ width="480" }][14]
  <figcaption>New, universal power supply mount. The mount is off-center and has a passthrough for power switch wiring.</figcaption>
</figure>

<figure markdown>
  [![front left render][13]{ width="480" }][13]
  <figcaption>The power supply no longer hangs freely; instead, it adds rigidity to the case when installed. Also: all three front vents have an optional fan mount on the inside (one occupied in the render).</figcaption>
</figure>

<figure markdown>
  [![front right render][15]{ width="480" }][15]
  <figcaption>The CPU tray is moved slightly forward and now mounts with M3 screws. The rear wiring passthrough no longer exposes the power socket.</figcaption>
</figure>

<figure markdown>
  [![front left render][17]{ width="480" }][17]
  <figcaption>Hex flooring for better ventilation and sturdier build.</figcaption>
</figure>

<figure markdown>
  [![front left render][16]{ width="480" }][16]
  <figcaption>The two CPU bays are elevated to make room for lower bay tray mounts. Unused bays can hold a short lower bay tray.</figcaption>
</figure>

[1]: https://github.com/jon-harper/OmniBox/issues/14
[2]: https://github.com/jon-harper/OmniBox/issues/18
[3]: https://github.com/jon-harper/OmniBox/issues/35
[4]: https://github.com/jon-harper/OmniBox/issues/33
[5]: https://github.com/jon-harper/OmniBox/issues/39

[11]: ../img/gallery_0.9.9/render1.png
[12]: ../img/gallery_0.9.9/render2.png
[13]: ../img/gallery_0.9.9/render3.png
[14]: ../img/gallery_0.9.9/render4.png
[15]: ../img/gallery_0.9.9/render5.png
[16]: ../img/gallery_0.9.9/render6.png
[17]: ../img/gallery_0.9.9/render7.png