---
title: PSU Wiring
summary: Instructions for wiring the power supply.
authors: Jon Harper
date: 2022-10-31
steps:
  psu_wire:
    - txt: |
        1) Remove the red wire from the IEC socket's line (L) terminal. Note that this view is from the bottom up; the line (L) wire is the red wire on top.
      img: ../img/assembly/core/psu_wire1.webp
      img_txt: Remove the line wire.
    - txt: |
        2) Attach the wire with two spade connectors to the socket's line (L) terminal.
      img: ../img/assembly/core/psu_wire2.webp
      img_txt: Replace the line wire
    - txt: |
        3. Run the other end of the wire through the PSU tray's cutouts and attach it to a terminal on the power switch.
      img: ../img/assembly/core/psu_wire3.webp
      img_txt: Connect the line to the power switch
    - txt: |
        4. Attach the spade connector on the other crimped wire to the remaining power switch terminal.
      img: ../img/assembly/core/psu_wire4.webp
      img_txt: Connect the other wire to the switch
    - txt: |
        5. Run the wire back through the PSU tray's wiring hole and secure the fork connector to the PSU's line (L) AC terminal.
      img: ../img/assembly/core/psu_wire5.webp
      img_txt: Connect the PSU's line terminal
    - txt: |
        6. Connect the remaining IEC socket connectors to the PSU: neutral and protective earth/ground (often yellow or green).
      img: ../img/assembly/core/psu_wire6.webp
      img_txt: Connect the remaining wires
---

{% import 'assembly.md' as assy %}

At this point, it is a good idea to wire the power supply, power switch, and power socket. The cutouts
in the right PSU tray mount allows wiring to pass through from the power switch. There are zip tie
anchors available in the sides to secure the power switch wiring.

## Considerations

### Cautions

!!! important
    For this example, we will use *red* wires for the power switch and use them for the *line* leg from the power socket to switch to PSU (normally labeled 'L' on the PSU).
    
    It is strongly recommended that the switch operate on the line wire instead of the neutral.

!!! Warning
    Be careful of polarity and always check your work!

### Limitations

!!! warning 
    - **This guide is not meant to be a complete manual for wiring.**
    - **I am not liable for any damage or injury that may result.**

- The Overview video in this section is limited to connecting the prepared wiring.
- This section of the guide does not cover all possible scenarios.
- IEC sockets typically ship with short wires with pre-crimped connectors.
    - If yours is not pre-wired, you will need two additional wires for the other poles of the IEC socket.
    - Preparing and installing these wires is beyond the scope of this guide.

### Crimping

In this section you will need to crimp closed barrel connectors. If you have never performed crimping before, it is strongly recommended that you practice before proceeding.

Cablecraft has an excellent, [:material-book-open-variant: in-depth guide][crimp_guide] to crimping common terminal types.


## Wiring the PSU

The illustrations and video in this section are from a prior release, but the procedure for this release is the same.

###  Overview

{{ assy.overview_video(meta.video_folder + 'psu_wiring.mp4') }}
### Materials

| Parts                                         | Qty  | Note                                |
|-----------------------------------------------|------|-------------------------------------|
| 16awg/1.5mm^2^ red stranded hookup wire       | 0.7m | 14 or 16 gauge (1.5mm^2^ - 2.5mm^2^) |
| Fork connectors, 14-16 awg, female insulated  | 1    |                                     |
| Female spade connectors, 14-16 awg, insulated | 3    |                                     |

### Preparing Materials

!!! note
    When crimping closed barrel connectors, the bare wire should extend no more than 1-2mm from the end of the crimp.

1. Cut one (1) length of hookup wire approximately 30cm (12") long and strip the ends.
2. Crimp a spade terminal on each end and set the wire aside.
3. Cut one (1) length of wire approximately 37cm (15") long and strip the ends.
4. Crimp a spade terminal to one end.
5. Crimp a fork connector on the other end.

<figure markdown>
  [![illustration][wires]{width="480"}][wires]
  <figcaption>The prepared wires should look roughly like the above.</figcaption>
</figure>

### Directions

{{ assy.render_steps(steps.psu_wire, '480px') }}

### Reference

[![finished illustration][psu_final]][psu_final]

[psu_final]: ../img/assembly/core/psu_wire_final.webp
[wires]: ../img/assembly/core/wires.webp