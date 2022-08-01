---
title: Panels
summary: OmniBox panel assembly intructions.
authors: Jon Harper
date: 2022-07-31
---

All of the panels are customizable, so this section has a less formal Parts section. Each starts with a list of the basics required to attach any type of that panel mount. Any additional parts needed for the panel we are using as an example are listed separately.

## 1. Front Panel

You will need at least:

| Parts                     | Qty | Note                                            |
|---------------------------|-----|-------------------------------------------------|
| Printed front panel       | 1   |                                                 |
| M3 x 8mm screws           | 2   | All front panels mount using two (2) of these.  |

In this example, we will use:

| Parts                                                 | Qty | Note  |
|-------------------------------------------------------|-----|-------|
| [Front Panel - Micro SD Extension with USB C.stl][18] | 1   | Printed front panel example |
| [Micro SD card extension][14]                         | 1   |       |
| [USB C panel mount extension][15]                     | 1   |       |
| M3 x 6mm screws                                       | 2   |       |
| M3 x 8mm screws                                       | 2   |       |

| Step | Example |
|------|---------|
| If you have any add-ons for your front panel (such as a MicroSD extension) assemble and install these first. | [![panel with installed extensions][9]][9] |
| The USB C panel mount comes with screws and attaches directly. | [![adding USB C panel][16]][16] |
| Push the panel into place. | [![placing the front vent][1]][1] |
| Fasten the panel with two (2) M3 screws. | [![front vent installed][2]][2] |

## 2a. Rear Panel

You will need at least:

| Parts                     | Qty | Note                                            |
|---------------------------|-----|-------------------------------------------------|
| A printed rear panel      | 1   |                                                 |
| M4 x 8mm screws           | 8   | All rear panels mount using eight (8) of these. |

Our rear panel in this example is a panel mount test piece, but all rear panels follow the same pattern.

Some rear panels may have a fan to mount. If you are using the rear panel to mount connectors, it is strongly advised that you insert the connectors before installing the panel or connecting any wires to the board.

| Step | Example |
|------|---------|
| Push the rear panel in place against the back of the case. You may need to guide the wires out of the way. | [![first two screws][5]][5] |
| Attach the panel using eight (8) M4 screws. | [![panel with screws inserted][6]][6] | 


## 2b. Rear Panel Wiring

It's a good idea to attach your wiring to the MCU now, before we close up the case further.

## 3. Display Screen

You will need at least:

| Parts                     | Qty | Note                                                     |
|---------------------------|-----|----------------------------------------------------------|
| Printed display panel     | 1   |                                                          |
| LCD display               | 1   |                                                          |
| M4 x 12mm screws          | 4   | All display screen panels mount using four (4) of these. |

For this example, we will use:

| Parts                     | Qty | Note                                            |
|---------------------------|-----|-------------------------------------------------|
| [Generic 12864 Display Mount][19] | 1  | Example of a printed display panel.      |
| Creality 12864 display    | 1   | LCD display example                             |
| M3 x 6mm screws           | 4   |                                                 |

!!! note
    Some display mounts have more than one piece and require additional screws. The below is an example with a stock Creality 12864 display.

| Step | Example |
|------|---------|
| Remove the knob on the display screen. It should pull off. | [![removing the display knob][10]][10] |
| Slide the screen into place on the mount and fasten with four (4) M3 x 6mm screws. | [![attach the screen][3]][3] |
| Re-attach the knob to the display screen. Again, it should slide into place with light force. If your display mount has multiple pieces, attach those now (usually only applies to displays with side-mount SD card readers). | |
| Insert the display connectors and slide the cables in before the display. Fasten the display panel with four (4) M4 x 12mm screws. | [![screws attached][4]][4] |


## 4. Lid

Like the rear panel, the lid is intended for customization. The below is an example for a simple lid with a handle.

You will need for any lid or pair of half-lids:

| Parts                     | Qty | Note                                            |
|---------------------------|-----|-------------------------------------------------|
| M3 x 8mm screws           | 8   | See note below.                                 |
| Printed lid               | 1   |                                                 |

In this example, we also use:

| Parts                     | Qty | Note                                            |
|---------------------------|-----|-------------------------------------------------|
| M3 x 8mm screws           | 2   |                                                 |
| [Carry handle][12]        | 1   |                                                 |
| [Carry handle lid][13]    | 1   | Example of a printed lid.                       |

!!! note
    0.9.8 introduces half-length lids. One half-length lid requires four (4) screws; a full length lid attaches with eight (8) The main body requires two (2) half-length lids or one (1) full-length lid.

!!! note
    Because the screws are threaded directly into plastic, removing and reattaching the lid will eventually wear out the holes in the main body. I recommend starting with shorter (8mm) screws and gradually switching to longer ones over time to get "fresh" plastic.
    
    Lids may use screws up to 16mm in length.

| Step | Example |
|------|---------|
| Attach the handle to the lid using two (2) M3 x 8mm screws. | [![attaching the handle][11]][11] |
| Use eight (8) M3 x 8mm screws to attach the lid. | [![first two screws][8]][8] | 
    
[1]: ../img/assembly/front_panel1.jpg
[2]: ../img/assembly/front_panel2.jpg
[3]: ../img/assembly/display1.jpg
[4]: ../img/assembly/display2.jpg
[5]: ../img/assembly/rear_panel1.jpg
[6]: ../img/assembly/rear_panel2.jpg
[7]: ../img/assembly/lid1.jpg
[8]: ../img/assembly/lid2.jpg
[9]: ../img/assembly/panel_install.jpg
[10]: ../img/assembly/display_knob.jpg
[11]: ../img/assembly/lid_handle.jpg
[12]: https://github.com/jon-harper/OmniBox/blob/main/Panels/Lid/Carry%20Handle.stl
[13]: https://github.com/jon-harper/OmniBox/blob/main/Panels/Lid/Carry%20lid/Carry%20Lid.stl
[14]: https://www.amazon.com/gp/product/B07YYSP5F5
[15]: https://www.amazon.com/Poyiccot-Extension-Female-Extender-Straight/dp/B086W2R8Z6
[16]: 
[17]:
[18]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Front%20Panel/Lanmu%20Micro%20SD%20Extension
[19]: https://github.com/jon-harper/OmniBox/blob/main/Panels/Display/Generic%2012864/Generic%2012864%20Display%20Mount.stl