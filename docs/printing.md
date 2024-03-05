---
title: Printing Guide
summary: Guide to successfully printing a case.
authors: Jon Harper
date: 2022-05-15
---

This page has tips and common settings for printing OmniBox.

## Recommended Materials

A complete OmniBox requires approximately 1.5kg of material.

**:octicons-check-circle-fill-16:{.jh-green} Modified PLA**

OmniBox prints best with modified PLA, usually called **PLA+** or **PLA Pro**. Modified PLA is typically advertised
as offering higher impact resistance, heat resistance, or other superior properties to unmodified PLA.

If your PLA filament mentions having additives, it's almost certainly modified.

**:octicons-check-circle-fill-16:{.jh-green} PETG**

Printing in PETG requires more tuning than PLA but offers a higher heat resistance.

**:octicons-x-circle-fill-16:{.jh-red} Unmodified PLA**

Sometimes called **Basic PLA** or just **PLA**, unmodified PLA prints easily but is a rigid and weak material.
If a manufacturer sells multiple PLA lines, the cheapest is sometimes unmodified.

!!! note "Note: Fan Gaskets"
    Fan gaskets are an optional noise reducer and require TPU.

## Tuning

It's worthwhile to invest some time on basic maintenace before putting your printer through printing
an OmniBox. Have you cleaned and lubricated your lead screw(s) lately? Tensioned your belts or cleaned
out the extruder gears? A little maintenance now can save a lot of heartache later with some of the long prints.

Likewise, take a little time to dial in the settings for the (usually two) filament colors you plan to use.
If you need a tuning guide, [Ellis' Print Tuning Guide][ellis] is widely
considered the best.

## 3D Print Settings

These settings are consistent for all parts except the TPU fan gaskets.

| Setting                   | Value        | Notes |
|---------------------------|--------------|------|
| **Layer Height**          | 0.16-0.25mm  | Coarser settings have not been tested. |
| **Adaptive Layer Height** | Optional     | Can improve appearance and reduce print time.    |
| **Perimeters (Walls)**    | [*See below*](#material-specific-settings)   | Correct value depends on material. |
| **Infill**                | 20-25%       | Cubic is a good tradeoff for time and durability. |
| **Nozzle Diameter**       | 0.4mm, 0.6mm | If you print a case with a different nozzle size, please share your results! |
| **Support Overhang Angle** | At least 60 deg | This reduces print time & support material. |

### Material-Specific Settings

**PLA**

Print with 1.2mm or thicker walls (3 perimeters with a 0.4mm nozzle). 1.5mm+ results in solid Main Body side walls.

**PETG**

Use 1.6mm walls/perimeters (1.8mm for 0.6mm nozzles).

### Support Settings

- Leave supports off for all parts.
- The Main Body and Base both contain built-in supports where needed.

### General Tips

- For large parts (e.g., the rear main body) use a brim, adhesive, or both.
- Cantilever bed printers (where the bed is supported by a single Z stepper; e.g., Ender 5 Pro) should move heavier prints to the supported side of the bed.
- If printing in a drafty room, consider a partial enclosure to help layer adhesion.
- Long lids will fit on 220x220mm beds if printed without a skirt or brim.

[tour]: tour.md "Visual Guided Tour"
[base]:         support/base.md
[main_body]:    support/main_body.md
[psu]:          support/psu.md
[cpu]:          support/cpu.md
[mcu]:          support/mcu.md
[lower_bay]:    support/lower_bay.md
[display]:      support/display.md
[lid]:          support/lid.md
[rear_panel]:   support/rear.md
[side_panel]:   support/side.md
[bottom_panel]: support/bottom.md
[ellis]: https://ellis3dp.com/Print-Tuning-Guide/ "Ellis' Print Tuning Guide (ellis3dp.com)"