## What are these abbreviations on the rear panels? SY? PC?

The abbreviations are part of an attempt to standardize naming conventions for 3D printer components when discussing connections and wiring. Below is a chart:

| Abbr.  | Description                                             |
|--------|---------------------------------------------------------|
| HE[#]  | Hotend with optional enumerator                         |
| CF[#]  | Hotend cooling fan with optional enumerator             |
| PF[#]  | Part cooling fan with optional enumerator               |
| TH[#]  | Hotend thermistor with optional enumerator              |
| TB     | Bed thermistor                                          |
| TC[#]  | Chamber/enclosure temperature with optional enumerator  |
| TE     | Electronics case thermistor (not used on panel)         |
| FC[#]  | Chamber/enclosure fan with optional enumerator          |
| ABL    | Automated bed leveling, e.g. BLTouch                    |
| LGT[#] | Lights with optional enumerator                         |
| ME[#]  | Extruder motor with optional enumerator                 |
| MX/MA  | X (or Alpha on CoreXY) stepper motor                    |
| MY/MB  | Y (or Beta on CoreXY) stepper motor                     |
| MZ[#]  | Z stepper with optional enumerator                      |
| SX     | X limit switch/end stop                                 |
| SY     | Y limit switch/end stop                                 |
| SZ[#]  | Z limit switch/end stop with optional enumerator        |
| USB    | USB port for communicating with the MCU                 |

## What is an optional enumerator?

Basically, if there's only one of something, for example the hotend (`HE`), just use the abbreviation. If you have two or more, add a number to the end. Hotends are typically numbered from zero, so on a dual extruding printer, you would label `HE0` and `HE1`.

## Do I have to follow this pattern?

No, but it is used on the stock rear panel configurations. This page is simply informative.