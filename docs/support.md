---
title: Supported Parts
summary: A list of parts supported by OmniBox
authors: Jon Harper
date: 2022-07-03
---

This is a (mostly complete) list of boards and other components supported by OmniBox, along with the necessary `STL`. The linked git folders *should* contain `STEP` and Fusion files to allow modification. Please open an issue if any are missing.

## Trays

### MCU Trays

These parts are in the [Trays\MCU](https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU) git folder.

| Component            | `STL`                      | Note                                    |
|----------------------|--------------------------|-----------------------------------------|
| BTT Octopus          | MCU Tray - Octopus.stl   |                                         |
| BTT SKR 1.3+         | MCU Tray - BTT SKR 2.stl | Compatible with all SKRs 1.3 and newer. |

### CPU Trays

These parts are in the [Trays\CPU](https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU) git folder.

| Component            | `STL`                        |
|----------------------|----------------------------|
| Raspberry Pi 3B+     | CPU Tray - RPi 3B Plus.stl |
| Raspberry Pi 4B      | CPU Tray - RPi 4B.stl      |

### Lower Bay Trays

The files for these trays are stored in the [Trays\Lower Bay](https://github.com/jon-harper/OmniBox/tree/main/Trays/Lower%20Bay) git folder.

Some trays include space for 40x40x10mm fans. This is specified in the file name.

| Component | `STL` | Note |
|-----------|-----|------|
| Generic LM2596 | Lower Bay Tray - 40mm Fan and Two Bucks v2.stl | Typical current limit of 2.5A max. |
| [DROK LM2596 with LED](https://www.amazon.com/Converter-DROK-Transformer-Regulator-Stabilizer/dp/B00JUFJ1GA) | Lower Bay Tray - LM2596 with LED.stl | Current limit is 3A max, 2A continuous. |

## Panels

### Display Screen Panels

Each display screen has a subfolder in the [Panels/Display](https://github.com/jon-harper/OmniBox/tree/main/Panels/Display) git folder. There is an optional `STL` for a [display knob](https://github.com/jon-harper/OmniBox/blob/main/Panels/Display/Display%20Knob.stl), as well.

| Component            | Folder | Notes |
|----------------------|--------|-------|
| Creality 12864 Stock | [Generic 12864](https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Generic%2012864) | Also known as CR-10 stock display. Ender 3 V2 display not supported. |
| FYSETC Mini 12864    | [Mini 12864](https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Mini%2012864) | This includes BTT and other clones. |
| BTT 2.4" TFT         | [BTT 2.4 TFT](https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/BTT%202.4%20TFT) | This product is discontinued, but I still use it, so there's a part. |
| BTT 3.5" TFT         | [BTT 3.5 TFT](https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/BTT%203.5%20TFT) | |


### Front and Rear Panels

Both of these components are highly customizable, so this list may be incomplete.

| Part or Connector | Panel Location | Notes |
|-------------------|----------------|-------|
| [MicroSD panel mount extension](https://www.amazon.com/gp/product/B07YYSP5F5) | Front | |
| [USB C panel mount extension](https://www.amazon.com/gp/product/B086W7C58P) | Front or Rear | |
| [JST SM panel mount connectors](https://www.amazon.com/gp/product/B07D9HRDT6) | Rear | 2-5 pins |
| Molex Micro Fit 3.0 connectors | Rear | Currently only supported in the [2-pin, 2-row](https://www.digikey.com/en/products/detail/molex/0430200200/252490) configuration. |