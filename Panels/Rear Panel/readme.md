# How do I know which rear panel to use?

## Do you need panel mounted connectors?

If "No", go to the "Generic Rear Panels" section next.

If "Yes", skip to the "Molex Panel Mounts" section below.

## Generic Rear Panels

These have a large cutout for wiring to pass through. They come with two options:

- USB Panel Mount type (None, USB A, or USB C)
- With or without 60mm fan cutout

You can find the generic panels in the `Panels\Rear Panels\Generic` folders. Each combination of USB and fan is present as a subfolder (e.g., `USB C, No Fan`).

## Molex Panel Mounts

This area is in active development. The `Panels\Rear Panels\Template` folder has a Fusion file with panel mount profiles for most Molex Micro Fit 3 connectors (along with many others).

There are two approaches to using panel mounted connectors:

- Single point-to-point panel mounts. Each limit switch or stepper (and so forth) has its own connector on the rear panel.
- "Y splitter"-type connectors, where one many-pin connector attaches to the rear panel and splits into individual runs to each component. For example, a six-pin connector might go to a stepper (four pins) and nearby limit switch (two pins).

I have documentation in process to help create pin orders for the second type of wiring harness. A few common hardware configurations will be added to the `Panels\Rear Panels\Molex` folder along with wiring instructions. The timing of this is dependant upon testing and my own free time.