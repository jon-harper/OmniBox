---
title: Display Panels
summary: List of displays with compatbile OmniBox mounts.
authors: Jon Harper
date: 2022-07-22
---

MCU displays include various TFT and older 128x64 character LCD diplays. Raspberry Pi displays are TFT displays, usually used with OctoPrint or Klipper.

![close-up of a stock display](../img/examples/display.png)

## MCU Displays

Each display screen has a subfolder in the [Panels/Display][11] git folder. There is an optional `STL` for a [display knob][10], as well.

Each component name links to the corresponding git folder.

| Component            | Image | Notes |
|----------------------|--------|-------|
| [Generic 12864][9] | ![img](../img/parts/classic_12864.jpg) | Also known as Creality CR-10 stock display; comes on most Creality printers. |
| [FYSETC Mini 12864][8] | ![img](../img/parts/mini12864.jpg)  | This includes BTT brand and other clones. |
| [BigTreeTech 2.4" TFT][7] | ![img](../img/parts/btt_tft_2.4.jpg)  | This product is discontinued, but I still use it, so there's a part. |
| [BigTreeTech 3.5" TFT][6] | ![img](../img/parts/btt_tft_3.5.jpg)  | Note that this is not the E3 version, which would use the Generic 12864 mount. |

All of these mounts require four (4) 8mm M3 screws to fasten the display in place. Some mounts have two pieces and require additional screws.

## Raspberry Pi Displays

Any TFT meant to attach a Raspberry Pi on the back can be mounted in one of two ways:

- [As a half lid][12] above the MCU display mount,
- Or [in place of the MCU display][13] entirely.

Compatible products include:

- BigTreeTech Pi TFT displays (using included hardware)
- Raspberry Pi-branded 7" TFT (with additional standoffs and M2.5 screws)

[6]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/BTT%203.5%20TFT
[7]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/BTT%202.4%20TFT
[8]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Mini%2012864
[9]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Generic%2012864
[10]: https://github.com/jon-harper/OmniBox/blob/main/Panels/Display/Display%20Knob.stl
[11]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display
[12]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Lid/Pi%20TFT/
[13]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Raspberry%20Pi%20TFT