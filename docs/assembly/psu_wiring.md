---
title: PSU Wiring
summary: Instructions for wiring the power supply.
authors: Jon Harper
date: 2022-10-31
---

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

<video controls="">
    <source src="{{meta.video_folder}}psu_wiring.mp4" type="video/mp4">
</video>

### Materials

| Parts                                         | Qty  | Note                                |
|-----------------------------------------------|------|-------------------------------------|
| 16awg/1.5mm^2^ red stranded hookup wire       | 0.7m | 14 or 16 gauge (1.5mm^2^ - 2.5mm^2^) |
| Fork connectors, 14-16 awg, female insulated  | 1    |                                     |
| Spade connectors, 14-16 awg, insulated        | 3    |                                     |

### Preparing Materials

!!! note
    When crimping closed barrel connectors, the bare wire should extend no more than 1mm from the end of the crimp.

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

<figure markdown>
  [![illustration][psu1]{width="480"}][psu1]
  <figcaption>1. Remove the red wire from the IEC socket's line (L) terminal. Note that this view is from the bottom up; the line (L) wire is the red wire on bottom.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu2]{width="480"}][psu2]
  <figcaption>2. Attach the wire with two spade connectors to the socket's line (L) terminal.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu3]{width="480"}][psu3]
  <figcaption>3. Run the other end of the wire through the PSU tray's cutouts and attach it to a terminal on the power switch.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu4]{width="480"}][psu4]
  <figcaption>4. Attach the spade connector on the other crimped wire to the remaining power switch terminal.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu5]{width="480"}][psu5]
  <figcaption>5. Run the wire back through the PSU tray's wiring hole and secure the fork connector to the PSU's line (L) AC terminal.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu6]{width="480"}][psu6]
  <figcaption>6. Connect the remaining IEC socket connectors to the PSU: neutral and protective earth/ground (often yellow or green).</figcaption>
</figure>


### Reference

[![finished illustration][psu_final]][psu_final]

[psu1]: ../img/assembly/core/psu/wire1.webp
[psu2]: ../img/assembly/core/psu/wire2.webp
[psu3]: ../img/assembly/core/psu/wire3.webp
[psu4]: ../img/assembly/core/psu/wire4.webp
[psu5]: ../img/assembly/core/psu/wire5.webp
[psu6]: ../img/assembly/core/psu/wire6.webp
[psu_final]: ../img/assembly/core/psu/wire_finished.webp
[wires]: ../img/assembly/core/psu/wires.webp