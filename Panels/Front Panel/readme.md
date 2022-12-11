# How do I know which front panel to use?

| Folder           | Description | Use If... |
|------------------|-------------|-----------|
| `MicroSD Extension`  | **Recommended** Mounts a MicroSD extension and optionally a USB connector. | ...You need quick and easy access to your MCU's SD card slot. |
| `Vent Only`   | Plain intake vents in several styles. | ...You do not need any panel mounted accessories. |
| `Template` | A blank template and a master Fusion file for the existing panels. | ...You want to create your own panel. |

Note: each variant of the front panel comes with three vent types to choose from.

- Hexagon
- Slats
- Slots

## Do you need panel mounted MicroSD or USB connectors?

If "No", choose an STL file from the `Vent Only` folder.

If "Yes", see below.

## `MicroSD Extension`

This folder contains panels that extend your MCU's SD card reader and optionally your MCU's USB port.

There are three variants:

- USB B
- USB C
- No USB panel mount

All three variants require printing the holder and cap files in [`Misc/MicroSD Extension`](../../Misc/MicroSD%20Extension).

*If you do not have an SD card extension, flashing your MCU will require removing the lid or display to access the SD card slot.*

## `Template`

To create a custom front panel, head to the `Template` folder to start from a blank template. You can use the master Fusion 360 file in this folder to modify an existing design.