# 20P with I2C, XYZ, Enclosed

## Overview

This is for a single-Z axis printer with direct drive and a BLTouch. All unspecified panel mount connectors are Molex Micro Fit 3. 

This panel also includes:

- 12-pin and 8-pin panel mount cutouts for the hotend
- 4-pin I2C cutout for MPU-6050 communication
- Passthru for the bed wires
- USB C panel mount

## Example Use

- Ender 3 or Ender 5 Pro with direct drive, BLTouch
- Klipper and MPU-6050 accelerometer or other I2C device(s)
- Enclosed with two fans
- Toolhead and enclosure lights

## Cutouts Labels and Default Pin Layout

### Toolhead

- **1**: 8 pin signal connector
  - Thermistor
  - BLTouch
  - One (1) unused pin
- **2**: 12 pin power connector
  - Hotend
  - 2-pin LED lights
  - Cooling fan
  - Part fan
  - Extruder stepper
- **I2C**: 4 pin I2C connector
  - 3.3V and GND pins
  - Two (2) signal pins

### Motion

- **3**: 6 pin connector
  - X endstop
  - X stepper
- **4**: 16 pin connector
  - Bed Thermistor
  - Y endstop
  - Z endstop
  - Y stepper
  - Z stepper
  - 2-pin LED
- **5**: 6 pin connector
  - Chamber thermistor
  - Chamber fan 1
  - Chamber fan 2

### Other

- Cutout for bed wire
- USB C panel mount