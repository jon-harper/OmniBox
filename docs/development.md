---
title: The OmniBox Story
summary: Gallery for the initial release of OmniBox.
authors: Jon Harper
date: 2022-08-04
---

## The Requirements

### Enclosed Printing

Enclosed 3D printing requires controlling more hardware than comes with a typical 3D printer:

- Lighting
- Webcam
- Thermistor (temperature sensor)
- Temperature-controlled exhaust fan
- Always-on filtration fan

Electronics are typically rated for short periods at high ambient temperatures, but the 50C (120F) or higher temperatures in a well-insulated enclosure are hazardous to electronics. I printed my first of Steve Burcham's cases to remove my electronics from such heat (OmniBox is derived from his work).

### Managing Devices

Common devices like fans and lights (and Raspberry Pis!) need a buck converter lower the voltage from a 3D printer's power supply. My printed cases for these printer/enclosure combos became cramped with them. Each buck converter had to sit on a tray above the microcontroller unit (MCU); wiring changes to the MCU required that I first remove up to three buck converter trays.

### Support for Large Boards

Additionally, I wanted to use the BIGTREETECH's Octopus in a case, which I had used to success with another project. The Octopus 1.1 is a solid board that provides ample power sources and signal pins. The Octopus does not fit the cases I had already printed; I also had several ideas to improve upon Steve's case.

With these requirements and goals in mind, I decided to design my own case.

## Building the OmniBox

This is my second electronics case designed around general shape and layout from Steve's V3 case. I kept compatibility only with the original display screens. Lids should be easy to modify to fit.

Templates are provided for all trays and panels to allow further customization and support for new products.

## Development Gallery

These photos detail some of the evolution of Steve's original case into OmniBox.

| Development Photos |   |
|--------------------|---|
| The initial main body prototype, looking awkward. | [![original prototype][6]][6] |
| Size comparison: Left is an example of Steve's V5 case (with custom panels). On the right is one of the first OmniBoxes during assembly. | [![size comparison][5]][5] |
| The first and second finished case bodies, waiting for more panels to finish printing. | [![one and two][4]][4] |
| Testing for fit with all of the connectors in place. | [![finished rear panel][3]][3] |
| Closed up for the first time, front view. | [![closed up, front][2]][2] |
| Closed up for the first time, rear view. | [![closed up, front][1]][1] |

[1]:  img/gallery/closed_up.jpg
[2]:  img/gallery/front_view.jpg
[3]:  img/gallery/finished_rear.jpg
[4]:  img/gallery/one_and_two.jpg
[5]:  img/gallery/size_comparison.jpg
[6]:  img/gallery/prototype.jpg