Welcome to the OmniBox repository. This is a modular control case for 3D printing. It is conceptually derived from Steve Burcham's [Stand Alone Main Control Case](https://www.thingiverse.com/thing:3999751), but is incompatible except with respect to display screens.

## Background

I had a catastrophic failure of multiple BIGTREETECH SKR 2 boards in a row. I print a lot of ABS, which means controlling an enclosure with lights, fans, etc.--and that equates to a lot of buck converters.

BIGTREETECH's Octopus 1.1 is a solid board that provides ample power sources and signal pins. It also (so far) hasn't blown out any of my equipment or itself. Unfortunately, the existing control cases I had printed didn't fit the Octopus; I also had a few ideas for changes and improvements. This is my second control case for the Octopus centered around the footprint used by Steve's V3 case. Since the source is not availabe for the base or main body, I redesigned the case from scratch, keeping compatibility only with the original display screens. Lids should be easy to modify to fit, as they maintain the same overall dimensions.

## TODO

- Finish fit testing version 1.0
- Add pictures

## Components

- [Base](../../tree/main/Base): front and back
- [Main body](../../tree/main/Main%20Body): front with screen; back with board, bucks, and fans
- Trays for the [MCU](../../tree/main/MCU) and [CPU](../../tree/main/CPU)
- [Display mount](../../tree/main/Display)
- [Lid](../../tree/main/Lid)
- [Rear panel](../../tree/main/Rear%20Panel) for exhaust, fans, and wiring connections. See below.
- A [front grill/SD card extension mount](../../tree/main/Front%20Panel)

### Rear Panel Configuration

This is a very printer-specific file. Included are two stock .STL files: a typical Ender 3 or Ender 5 type printer with 5-pin ABL and RGB, and the same setup with the additional of an extra thermistor port and two fan ports for an enclosure. There is a template 

### Note

Templates in both Fusion and STEP format are provided for most of the case to allow customization as needed. If a STEP file is available but not a Fusion archive, this is possibly because the design was recently modified.

## Print Settings

### Layer Height

I have not attempted printed at any coarser a resolution than 0.2mm. I would not recommend going finer. For the main body and base, it should be possible to print at 0.24 or 0.28mm.

### Perimeters and Infill

Print with at least 3 perimeters and 20% infill (cubic is fine).

### Material

PLA+ is an excellent material for these cases, both due to its affordability and relative durability. PETG could be used bit is somewhat brittle and would take much longer to print.

### Nozzle Size

I have only tested with an 0.4mm nozzle, but an 0.6mm nozzle should work. If you print a case with a different nozzle size, please share your results!

## Bill of Materials

There's quite a bit of flexibility in the design to allow for screws of multiple lengths, i.e. to use what's on hand. The assembly process notes where substitutions can be made. This is an "ideal" list.

| Item                              | Qty | UOM |Note |
|-----------------------------------|-----|-----|-----|
| Filament                          | 2   | kg  | Final use is closer to 1kg if printed in 1 color |
| M3 x 6mm screws                   | 12  | ea  | |
| M3 x 8mm screws                   | 12  | ea  | |
| M3 x 12mm screws                  | 20  | ea	 | |
| M3 x 16mm screws                  | 2   | ea  | |
| M3 x 20mm sharp point wood screws | 8 | ea | **OR** #6 x 3/4" |
| M4 x 8mm screws                   | 14 | ea | |
| M4 x 16mm screws                  | 4   | ea  | |
| [SPST toggle switch](https://www.amazon.com/gp/product/B07QQ22DTB) | 1   | ea  | Identical profile to Creality Ender power switch. |
| [Meanwell-type PSU](https://www.amazon.com/MEAN-WELL-LRS-350-24-350-4W-Switchable/dp/B013ETVO12) | 1   | ea  | Meanwell-type refers to mounting pattern (M4, 150mm x 50mm). Compatible with all Ender PSUs. |
| 3D Printer control board (MCU)    | 1   | ea  | Currently only the [BTT Octopus](https://www.amazon.com/BIGTREETECH-Motherboard-Compatible-Firmware-Raspberry/dp/B094NPRYDP) is supported. |
| Raspberry Pi 3B+ or 4B            | 1   | ea  | (Optional for OctoPrint/Klipper users)
| [IEC C14 Socket with Fuse](https://www.amazon.com/gp/product/B081ZFHRGW) | 1   | ea  | Identical profile to Creality Ender series power socket. |
| [40x40x10mm Fans](https://www.amazon.com/dp/B08R9L9YR2) | 2 | ea  | 5V, 12V, or 24V |
| A 12864-style display or emulator | 1   | ea  | Includes: Stock Creality 12864, [BTT 3.5](https://www.amazon.com/BIGTREETECH-Upgrade-Touch-Controller-Display-Motherboard/dp/B07VWGFKLZ) displays |

Additionally, some optional components:

| Item                              | Qty | UOM |Note |
|-----------------------------------|-----|-----|-----|
| [USB C Panel Mount extension cable](https://www.amazon.com/gp/product/B086W7C58P/) | 1 | ea | Not needed if using UART with Klipper, but recommended. |
| [MicroSD to MicroSD extension cable](https://www.amazon.com/gp/product/B09CKRDFTH) | 1 | ea | Unfortunately, this is not the same profile as the more popular LANMU connector. |
 
### Connectors

Connectors are not included in the basic BOM--with the exception of the power connector--because this is up to the end user. The included two panel profiles use JST SM connectors for everything but the hotend, which uses a 2-pin, 2-row [Molex Micro Fit 3.0](https://www.digikey.com/en/product-highlight/m/molex-connector/micro-fit-3-interconnect-system) panel mount connector. I get mine through [Digikey](https://www.digikey.com/en/products/detail/molex/0430200200/252490) along with the [mating pins](https://www.digikey.com/en/products/detail/molex/0430310009/252485).

For the JST SM connectors, you can find [a kit on Amazon for about $15](https://www.amazon.com/gp/product/B07D9HRDT6).

## Assembly

### Base

You will need:

- 4x M4 x 16mm screws
- 1x SPST toggle switch
- The printed front and rear base

1. The two pieces of the base both have two (2) M4 screw holes on each side. Use the four (4) M4 screws to fasten them togther. **Note:** The sawtooth air vents should be aligned the same way on the front and back.
2. Insert the power switch into the front. The sides should compress until it snap in place.

### Main Body

You will need:

- 6x M3 x 10-12mm screws (10mm or 12mm are both acceptable)
- 8x M3 x 12-20mm screws **or** 8x M3/#6 sheet metal screws (12mm-20mm or 1/2" to 3/4")
- 2x M3 x 16mm screws
- The printed front and rear main body
- The printed front crossbar
- Your power supply unit (PSU)
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

1. If you are using the rear panel to mount connectors, it is strongly advised that you insert the connectors to the panel first, before installing the panel or connecting any wires to the board.
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