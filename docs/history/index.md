---
title: 0.9.9 Release (Current)
summary: Changelog for the current and past releases of OmniBox
authors: Jon Harper
date: 2022-10-09
---

!!! tip
    Want to know more about OmniBox and what's next? Follow [@TheOmniBox on :material-twitter: Twitter][twitter]

The current release is 0.9.9, released on 2022-11-??.

## New Features

### Major New Features

- **Base:** [Issue #14][1]: Universal power supply mount
- **Main Body:** Moved CPU bay from front main body to rear, added a second bay on opposite side.
    - Unused second bay is an additional "side panel"
    - Can be used to mount an extra 40mm fan, panel mounts, or leave covered with a blank plate.
- **Main Body:** Zip tie anchors added:
    - Six (6) added to crossbar
    - Four (4) added to front main body (under MCU pillars)
    - Fifteen (15) added to rear main body
        - Four (4) under MCU pillars
        - Six (6) above MCU pillars
        - Five (5) by PSU wiring cutout
- **(New) Bottom Panel:** Removable panels for case underside.
    - Prevents finger-pokey by curious children and dust intrusion (see Completed Requests below).
    - Adds feet to the case.

### Additional Improvements

- **All:** All core parts now have embossed version numbers to help with intermixing version numbers.
- **Main Body** Redesigned intakes and modified exhaust mounts.
    - Easier to print.
    - Made room at base for running wires through to external fans.
- **Base:** Added a third front air vent.
- **Base:** All three front vents how have 40mm fan mounts.
- **CPU Trays:** New template and tray design
    - Old trays still work.
    - New tray is an easier print with fewer supports needed, can be printed in one of two orientations.
    - New releases will only include new trays.
    - Added Raspberry Pi tray with a 40mm fan intake.

### Completed Requests

| Hardware | Mount Location(s) | Notes |
|----------|-------------------|-------|
| Bottom panel | Bottom Panel | Has cutouts for speed/strength, but too small for kids' fingers. |
| Closed bottom panel | Bottom Panel | Solid to prevent dust intrusion. |
| Unified base | Core | This is a one-piece version of the base. |
| Keystone jacks | Front/side/rear panels | Added STEP file for mating part to build into panels and an example side panel. |

### New Hardware Support

| Hardware | Mount Location(s) | Notes |
|----------|-------------------|-------|
| Wago 221 Lever Nuts | Lower Bay | 3-position and 5-position |
| Neopixel (WS2812B) LEDs | Front panel | Backing piece for attaching lights behind front vents. |
| DROK 3A LM2596 with LED Buck Converter | Lower Bay | Single and dual, short and long trays. |
| Duet3D Duet 3 Mini 5+ | MCU Tray | |

### Experimental Hardware Support

These parts still need to be tested for fit and any other issues.

| Hardware | Mount Location(s) | Notes |
|----------|-------------------|-------|
| Mean Well RSP-500 power supply | Main body | For the Ender 5 Plus |
| 92mm fans | Rear panel, lid | 25mm thickness only. |
| 120mm fans | Lid | 25mm thickness only. |
| BIGTREETECH Manta M8P | MCU Tray | |
| BIGTREETECH 5" TFT | Display Panel | |
| BIGTREETECH UPS 24V 1.0 | Lower Bay | Short tray only. |
| BIGTREETECH SKR 3 | MCU Tray | |
| BIGTREETECH SKR 3 EZ | MCU Tray | |
| Duet3D Duet 3 6HC | MCU Tray | |

## Fixes

- [Issue #18][2]: Fan mount blocks screw hole for mounting base
    - Fan mount moved left and up as part of intake redesign.
- [Issue #35][3]: Hex nut for mounting IEC socket is hard to reach
    - Removed hex nuts.
    - Screws attach directly in plastic.
- [Issue #33][4]: Base zip tie anchors need adjustment
    - Removed rearmost zip tie that was troublesome.
    - Adjusted position of others.
- [Issue #39][5]: Display screen partially blocks two front main body/base screws
    - Added cutout for access.
- [Issue #37][6]: Documentation site is missing license page

## Documentation & Repository

- [Documentation site](https://jon-harper.github.io/OmniBox)
    - Added tooltips to links.
    - Consolidated external links and added tooltips.
    - Replaced assembly and illustration pictures with uniformly styled generated graphics.
- Assembly Guide
    - Completely rewritten for 0.9.9.
    - Basic wiring instructions included.
    - **Video overviews** for each section.
- [Repository](https://github.com/jon-harper/OmniBox)
    - Added `/include` subfolder for external documentation files.
    - Renamed "Fan Cages" to "Fans".
    - Further divided lids folders for ease of navigation.
## Gallery

<figure markdown>
  [![front right render][11]{ width="480" }][11]
  <figcaption>1. The CPU bay is now part of the rear body.<br>2. The power supply area has an extra vent in front.<br>3. 40mm, 80mm, 92mm, and 120mm fans are now supported as lid mounts.</figcaption>
</figure>

<figure markdown>
  [![front left render][12]{ width="480" }][12]
  <figcaption>1. There is a matching CPU bay on the opposite side.<br>2. Optional Neopixel LEDs are visible behind the front vent.<br>3. All panels now attach with M3 screws.</figcaption>
</figure>

<figure markdown>
  [![render from front and undearneath][14]{ width="480" }][14]
  <figcaption>New universal power supply mount. The mount is off-center and has a passthrough for power switch wiring.</figcaption>
</figure>

<figure markdown>
  [![render from the side and underneath][13]{ width="480" }][13]
  <figcaption>1. The power supply no longer hangs freely. When installed it adds rigidity to the case.<br>2. Each front vent has an optional fan mount on the inside.</figcaption>
</figure>

<figure markdown>
  [![render from the top right rear without rear or top panels on][15]{ width="480" }][15]
  <figcaption>1. 20+ zip tie anchors added.<br>2. The MCU tray now mounts with M3 screws.<br>3. The rear wiring passthrough no longer exposes the power socket.<br>4. New support for keystone jacks (unoccupied in the render).</figcaption>
</figure>

<figure markdown>
  [![render of the Core of an OmniBox with a Manta MCU mounted][17]{ width="480" }][17]
  <figcaption>1. Experimental support for the BIGTREETECH Manta M8P (CB1 not pictured).<br>2. Hex flooring for better ventilation and sturdier build.</figcaption>
</figure>

<figure markdown>
  [![render of an OmniBox Core from the rear without any panels installed][16]{ width="480" }][16]
  <figcaption>1. The two CPU bays are elevated to make room for lower bay tray mounts in unused bays.<br>2. Optional brass heat set inserts.</figcaption>
</figure>

<figure markdown>
  [![render from below showing the bottom panel][18]{ width="480" }][18]
  <figcaption>The new bottom panel fully encloses the case. It can be printed with holes for airflow or closed to prevent dust intrusion.</figcaption>
</figure>

<figure markdown>
  [![render from below showing the bottom panel][19]{ width="480" }][19]
  <figcaption>1. The new Generic rear panel has two wiring cutouts to let the user run wires from the top, bottom, or both.<br>2. The Generic panel comes in version with and without a 60mm fan (version with the fan pictured).</figcaption>
</figure>

[1]: https://github.com/jon-harper/OmniBox/issues/14
[2]: https://github.com/jon-harper/OmniBox/issues/18
[3]: https://github.com/jon-harper/OmniBox/issues/35
[4]: https://github.com/jon-harper/OmniBox/issues/33
[5]: https://github.com/jon-harper/OmniBox/issues/39
[6]: https://github.com/jon-harper/OmniBox/issues/37

[11]: ../img/gallery_0.9.9/render1.png
[12]: ../img/gallery_0.9.9/render2.png
[13]: ../img/gallery_0.9.9/render3.png
[14]: ../img/gallery_0.9.9/render4.png
[15]: ../img/gallery_0.9.9/render5.png
[16]: ../img/gallery_0.9.9/render6.png
[17]: ../img/gallery_0.9.9/render7.png
[18]: ../img/gallery_0.9.9/render8.png
[19]: ../img/gallery_0.9.9/render9.png