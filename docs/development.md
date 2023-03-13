---
title: The OmniBox Story
summary: Gallery for the initial release of OmniBox.
authors: Jon Harper
date: 2022-08-04
---

## The Requirements

Enclosed 3D printing requires controlling more hardware than comes with a typical 3D printer:

- Lighting
- Webcam
- Thermistor (temperature sensor)
- Temperature-controlled exhaust fan
- Always-on filtration fan

### Isolation From Heat

Most electronics will overheat in the 50C (120F) or higher ambient temperatures of a well-insulated enclosure. I printed my first of Steve Burcham's cases to remove my electronics from such heat; OmniBox is derived from his work.

### Flexibility and Accessibility

Devices like fans and lights--and Raspberry Pis!--need a buck converter lower the voltage from a 3D printer's power supply. My cases soon were cramped with bucks. Each one mounted on a tray above the microcontroller unit (MCU); wiring changes to the MCU required that I first remove up to three buck converter trays.

### Ample Room

After I discovered BIGTREETECH's Octopus in another project, I wanted a case for it. The Octopus does not fit the cases I had already printed; I also had several ideas to improve upon Steve's case.

With these requirements and goals in mind, I decided to design my own case.

## Early Development Gallery

These photos detail some of the evolution of Steve's original case into OmniBox.

| Development Photos |   |
|--------------------|---|
| The initial main body prototype, looking awkward. | [![original prototype][6]][6] |
| Size comparison: Left is an example of Steve's V5 case (with custom panels). On the right is one of the first OmniBoxes during assembly. | [![size comparison][5]][5] |
| The first and second finished case bodies, waiting for more panels to finish printing. | [![one and two][4]][4] |
| Testing for fit with all of the connectors in place. | [![finished rear panel][3]][3] |
| Closed up for the first time, front view. | [![closed up, front][2]][2] |
| Closed up for the first time, rear view. | [![closed up, front][1]][1] |

[1]:  img/gallery/0.9/closed_up.jpg
[2]:  img/gallery/0.9/front_view.jpg
[3]:  img/gallery/0.9/finished_rear.jpg
[4]:  img/gallery/0.9/one_and_two.jpg
[5]:  img/gallery/0.9/size_comparison.jpg
[6]:  img/gallery/0.9/prototype.jpg