Welcome to the OmniBox repository. This is a modular control case for 3D printing. It is conceptually derived from Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751), but is incompatible except with respect to display screens.

## Background

I had a catastrophic failure of multiple BIGTREETECH SKR 2 boards in a row. I print a lot of ABS, which means controlling an enclosure with lights, fans, etc.--and that equates to a lot of buck converters.

BIGTREETECH's Octopus 1.1 is a solid board that provides ample power sources and signal pins. It also (so far) hasn't blown out any of my equipment or itself. Unfortunately, Steve Burcham's control cases didn't quite fit my needs or the Octopus. This is my second attempt at creating a control case around the Octopus centered around the footprint used by Steve's V3/V5 cases. In the process, I redesigned the entirety from scratch, keeping compatibility only with the original display screens. Lids should be easy to modify to fit, as they maintain the same overall dimensions.

## Components

The component set should be familiar to anyone who has printed one of Steve Burcham's cases:

- Base: front and back
- Main body: front with screen; back with board, bucks, and fans
- Trays for the MCU and CPU
- Display mount
- Lid
- Rear panel for exhaust, fans, and wiring connections
- A front grill/SD card extension mount

Templates are provided for most of the case to allow customization as needed.

## Print Settings

### Layer Height

I have not attempted printed at any coarser a resolution than 0.2mm. I would not recommend going finer. For the main body and base, it should be possible to print at 0.24 or 0.28mm.

### Perimeters

Print with at least 3 perimeters and 20% infill (cubic is fine).

### Material

PLA+ is an excellent material for these cases, both due to its affordability and relative durability. PETG could be used bit is somewhat brittle and would take much longer to print.

## Assembly

### Base

You will need:

- 4x M4 x 16mm screws
- 1x [SPST toggle switch](https://www.amazon.com/gp/product/B07QQ22DTB) (in the same panel mount profile as the Creality Ender printers)
- The printed front and rear base

1. The two pieces of the base both have two (2) M4 screw holes on each side. Use the four (4) M4 screws to fasten them togther. **Note:** The sawtooth air vents should be aligned the same way on the front and back.
2. Insert the power switch into the front. The sides should compress until it snap in place.

### Main Body

You will need:

- 6x M3 x 8-12mm screws (8mm, 10mm, or 12mm are all acceptable)
- 8x M3 x 12-20mm screws **or** 8x M3/#6 sheet metal screws (12mm-20mm or 1/2" to 3/4")
- 2x M3 x 16mm screws
- The printed front and rear main body
- The printed front crossbar
- Your power supply that uses the 150mm x 50mm M4 mounting pattern as the [Meanwell LRS-350-35](https://www.amazon.com/MEAN-WELL-LRS-350-24-350-4W-Switchable/dp/B013ETVO12). Any Creality printer power supply should suffice.
- 4x M4 x 8mm screws for the power suppy

1. Assemble the front and rear using six (6) M3 screws. Any length between 8mm and 12mm will work. Make sure you insert the screws fron the *back* side into the *front* of the case. The holes on the back are larger than the front.
2. Mount the power supply using 4x M4 x 8mm screws. The power supply fits under the main body and is slightly offset towards the front right.
3. Place the assembled main body on top of the base. There are eight (8) ~3mm holes that should line up between the base and main body, four on each side. Fasten these together with your long M3 screws or sheet metal screws.
4. Place the crossbar in place at the joint between the lid and display mounts. Using the two (2) M3 x 16mm screws, attach the crossbar with a screw in each side.

### Dual 40mm Exhaust Fans

You will need:

- 8x M3 x 12mm screws (10mm will also work)
- 2x 40x40x10mm fans
- Two printed 40mm Fan Cages

1. Place a fan inside the cage with the stickered side of the motor facing *away* from the fan cage grill.
2. Insert two M3 screws on opposing sides of the fan cage and through the fan's mounting holes.
3. Thread the fan's wires through the fan cutout, then line up the fan and cage with the mounting holes.
4. Partially tighten both screws until at least two full turns of thread are holding the fan in place.
5. Insert and tighten the other two M3 screws.
6. Finish tightening the screws until all four screws are firmly in place.
7. Ensure the fan wire feeds through the cutout without pinching or binding.
8. Repeat the above process for the second fan.

### CPU Tray

You will need:

- 2-4 M3 x 6mm screws
- 2-4 M3 x 8mm screws
- A Raspberry Pi 3B+ or 4B
- The printed CPU tray for your Raspberry Pi

1. The Raspberry Pi comes with M2.5 screw holes, but can be bored out easily with M3 screws. Mount your Raspberry Pi with 6mm M3 screws onto the tray, using at least two screws.
2. Slide the tray into the side bay on the left side.
3. Use at least two (2) M3 x 8mm screws to fasten the tray in place.

### MCU Tray

You will need:

- 2x M4 x 8mm screws
- 2-4 M3 x 6mm screws
- Your MCU (e.g. BTT Octopus)
- The printed tray for your MCU

1. Attach your MCU with at least two M3 x 6mm screws to the tray. The screw holes face forward when inserted to the case; prefer to align your SD card connector to the front and power connectors to the back. Your likely limitation is the length of the SD card extension connector, if you plan to use one.
2. Slide the tray from the back of the assembled case to the front. Stop when the two screw holes on the sides align.
3. Tighten the tray in place with two (2) M4 x 8mm screws.

### Front Panel

You will need:

- 2x M3 x 8mm screws
- Your printed front panel
- Any accessories that mount to it and fasteners

1. If you have any add-ons for your front panel, like an MicroSD extension, install these first.
2. Insert the front panel and attach with two (2) M3 screws.

### Rear Panel

You will need:

- 4-8 M4 x 8mm screws
- Your printed rear panel
- Any connectors or other accessories for the rear panel

1. If you are using the rear panel to mount connectors, it is strongly advised that you insert the connectors to the panel **first**, before installing the panel or connecting the wires to the board.
2. Line up the rear panel with the cutout on the assembled case. It may pinch near the base--this is due to the walls leaning outwards further up as they cool. The rear panel will help keep the walls aligned.
3. Check where the screw holes line up. If any are clearly unaligned, leave those for last.
4. Starting with a screw hole near the top, partially thread an M4 screw in. Stop once you can feel the screw threads grab the main body at least two full turns.
5. Find another screw hole near the top on the opposite side and partially thread it in two full turns.
6. Fill in a screw hole on each side on the bottom half.
7. Insert screws into the remaining holes. If any of the holes are still unaligned, you can leave them empty or insert a screw at an angle and thread. It *may* eventually work itself straight.
8. Finish tightening all of the screws.

### Display Screen

You will need:

- 4 M4 x 8mm screws
- 4 M3 x 6mm screws
- Your printed display mount
- Your display
- If your display mount contains more than one piece, M3 screws to join them.

1. Remove the knob on the display screen. It should pull off.
2. Slide the screen into place on the mount and fasten with four (4) M3 x 6mm screws.
3. Re-attach the knob to the display screen. Again, it should slide into place with light force.
4. If your display mount has multiple pieces, attach those now (usually only applies to displays with side-mount SD cards).
5. It's usually a good idea to attach your display connectors now and slide the ends in first.
6. Finally, attach the display panel with four (4) M4 x 8mm screws.


### Lid

There are a number of choices for which lid to use and how to assemble them. All of the lids attach with between four (4) and eight (8) M3 x 8mm screws, although any length up to 12mm will work.