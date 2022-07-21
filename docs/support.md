---
title: Supported Parts
summary: A list of parts supported by OmniBox
authors: Jon Harper
date: 2022-07-03
---

This is a list of boards and other components supported by OmniBox, along with the necessary `STL`. The linked git folders *should* contain a `STEP` and to allow modification. Fusion files are also typically available where they can be exported.

## Trays

### MCU Trays

These parts are in the [Trays\MCU][16] git folder. Each component has its own subfolder.

| Component            | Mounting Tray                           |
|----------------------|-----------------------------------------|
| BTT Octopus          | `BTT Octopus`                           |
| BTT SKR 1.3+         | `BTT SKR`                               |
| BTT SKR Mini E3      | `BTT SKR E3`                            |
| Creality boards      | `BTT SKR E3`                            |

### CPU Trays

These parts are in the [Trays\CPU][15] git folder.

| Component            | `STL`                        |
|----------------------|------------------------------|
| Raspberry Pi 3B+     | `CPU Tray - RPi 3B Plus.stl` |
| Raspberry Pi 4B      | `CPU Tray - RPi 4B.stl`      |

### Lower Bay Trays

The files for these trays are stored in the [Trays\Lower Bay][13] git folder.

Some trays include space for 40x40x10mm fans. This is specified in the file name.

| Component | `STL` | Note |
|-----------|-----|------|
| Generic LM2596 | `Lower Bay Tray - 40mm Fan and Two Bucks v2.stl` | Typical current limit of 2.5A max. |
| [DROK LM2596 with LED][12] | `Lower Bay Tray - LM2596 with LED.stl` | Current limit is 3A max, 2A continuous. |

## Panels

### Display Screen Panels

Each display screen has a subfolder in the [Panels/Display][11] git folder. There is an optional `STL` for a [display knob][10], as well.

| Component            | Folder | Notes |
|----------------------|--------|-------|
| Creality 12864 Stock | [Generic 12864][9] | Also known as CR-10 stock display. Ender 3 V2 display not supported. |
| FYSETC Mini 12864    | [Mini 12864][8] | This includes BTT brand and other clones. |
| BTT 2.4" TFT         | [BTT 2.4 TFT][7] | This product is discontinued, but I still use it, so there's a part. |
| BTT 3.5" TFT         | [BTT 3.5 TFT][6] | |


### Front and Rear Panels

Both of these components are highly customizable, so this list may be incomplete.

| Part or Connector | Panel Location | Notes |
|-------------------|----------------|-------|
| [MicroSD panel mount extension][5] | Front | |
| [USB B panel mount extension][4] | Front or Rear | Right angle connector fits most boards more easily. |
| [USB C panel mount extension][3] | Front or Rear | |
| [JST SM panel mount connectors][2] | Rear | 2-5 pins |
| [Molex Micro Fit 3.0 connectors][1] | Rear | Supported up to [2-row, 16-position][14]. |

[1]:  https://www.digikey.com/en/htmldatasheets/production/1626160/0/0/1/0430300007.html
[2]:  https://www.amazon.com/gp/product/B07D9HRDT6
[3]:  https://www.amazon.com/gp/product/B086W7C58P
[4]:  https://www.amazon.com/gp/product/B071P2BGK5
[5]:  https://www.amazon.com/gp/product/B07YYSP5F5
[6]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/BTT%203.5%20TFT
[7]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/BTT%202.4%20TFT
[8]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Mini%2012864
[9]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Generic%2012864
[10]: https://github.com/jon-harper/OmniBox/blob/main/Panels/Display/Display%20Knob.stl
[11]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display
[12]: https://www.amazon.com/Converter-DROK-Transformer-Regulator-Stabilizer/dp/B00JUFJ1GA
[13]: https://github.com/jon-harper/OmniBox/tree/main/Trays/Lower%20Bay
[14]: https://www.digikey.com/en/products/detail/molex/0430200200/252490
[15]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU
[16]: https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU