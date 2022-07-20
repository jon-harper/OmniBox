# DD XYZ with BLTouch

## Overview

This is for a common single-Z axis printer with direct drive and a BLTouch. This panel also includes:

- Passthru for the bed wires
- 6-pin SPI cutout for ADXL communication
- Optional USB C panel mount position

## Cutouts Labels and Default Pin Layout

### Toolhead

- **1**: 10 pin power cable
  - Hotend
  - Cooling fan
  - Part cooling fan
  - BLTouch power and servo pin
  - One (1) unused pin
- **2**: 8 pin signal cable
  - Thermistor
  - BLTouch sensor
  - Extruder pins
- **SPI**: 6 pin SPI cable
  - 3.3V and GND pins
  - 4 SPI signal pins

### Motion

- **3**: 6 pin
  - X endstop
  - X stepper
- **4**: 8 pin
  - Y endstop
  - Z endstop
  - Y stepper
- **5**: 4 pin
  - Z stepper

### Other

- **6**: 2 pin (bed thermistor)
- Cutout for bed wire
- USB panel mount (optional)

## Examples

- Ender 3 with a direct drive mod and BLTouch
- Ender 5 Pro (not Plus) likewise modified
