---
title: Display Panels
summary: List of displays with compatbile OmniBox mounts.
authors: Jon Harper
date: 2022-07-22
---

:material-alpha-p-box: :material-alpha-d-box-outline: Display Panels mount two different types of display screens:

- MCU displays include various TFT and older 128x64 character LCD diplays.
- Raspberry Pi displays are TFT displays, usually used with OctoPrint or Klipper.

## MCU Displays

<figure markdown>
  [![front left render][1]{ width="480" }][1]
  <figcaption>12864 TFT display mounted on a panel.</figcaption>
</figure>

Each supported MCU display screen has a subfolder in the [Panels/Display][11] git folder. There is an optional `STL` for a [display knob][10], as well.

Component names below link to the corresponding git folder.

| Component            | Image | Notes |
|----------------------|--------|-------|
| [Generic 12864][9] | ![img](../img/parts/classic_12864.jpg) | Also known as Creality CR-10 stock display; comes on most Creality printers. |
| [FYSETC Mini 12864][8] | ![img](../img/parts/mini12864.jpg)  | This includes BTT brand and other clones. |
| [BigTreeTech 2.4" TFT][7] | ![img](../img/parts/btt_tft_2.4.jpg)  | This product is discontinued, but I still use it, so there's a part. |
| [BigTreeTech 3.5" TFT][6] | ![img](../img/parts/btt_tft_3.5.jpg)  | Note that this is not the E3 version, which would use the Generic 12864 mount. |

All of these mounts require four (4) 8mm M3 screws to fasten the display in place. Some mounts have two pieces and require additional screws.

## Raspberry Pi Displays

## Compatibility

Any TFT designed with mounts points for a Raspberry Pi on the back should be compatible.

Compatible examples include:

- BigTreeTech Pi TFT displays (using included hardware)
- Raspberry Pi-branded 7" TFT (with additional standoffs and M2.5 screws)

## Mounting Methods

These displays can be attached in one of two ways:

- In place of the MCU display as a [:material-alpha-p-box: :material-alpha-d-box-outline: Display Panel][13],
- Or as a [:material-alpha-p-box: :material-alpha-l-box-outline: Lid][12] above the MCU display mount.

See below for examples.

<figure markdown>
  [![render of Raspberry Pi TFT in place of an MCU display][2]{ width="480" }][2]
  <figcaption>Raspberry Pi TFT on a display panel.</figcaption>
</figure>


<figure markdown>
  [![render of Raspberry Pi TFT as a secondary display][3]{ width="480" }][3]
  <figcaption>Raspberry Pi TFT mounted as a lid.</figcaption>
</figure>

[1]: ../img/examples/display.png
[2]: ../img/examples/rpi_display.png
[3]: ../img/examples/rpi_lid.png

[6]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/BTT%203.5%20TFT
[7]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/BTT%202.4%20TFT
[8]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Mini%2012864
[9]:  https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Generic%2012864
[10]: https://github.com/jon-harper/OmniBox/blob/main/Panels/Display/Display%20Knob.stl
[11]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display
[12]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Lid/Pi%20TFT/
[13]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display/Raspberry%20Pi%20TFT