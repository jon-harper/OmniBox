---
title: PSU Wiring
summary: Instructions for wiring the power supply.
authors: Jon Harper
date: 2022-10-31
---

At this point, it is a good idea to wire the power supply, power switch, and IEC socket. There are zip tie anchors available in the sides to secure the power switch wiring. The large hole in the right PSU tray mount allows wiring to pass through.

## Considerations

### Cautions

!!! important
    For this example, we will use *red* wires for the power switch and use them for the *line* run from the power socket to switch to PSU (normally labeled 'L' on the PSU).
    
    If you are using *black* wires, connect the *neutral* (N) terminals with the crimped wires instead.

!!! Warning
    Be careful of polarity and always check your work!

### Limitations

!!! warning 
    - **This guide is not meant to be a complete manual for wiring.**
    - **I am not liable for any damage or injury that may result.**

- The Overview video in this section is limited to attaching the prepared wiring.
- This section of the guide does not cover all possible scenarios.
- IEC sockets typically ship with short wires with precrimped connectors attached.
    - If yours is not pre-wired, you will need two additional wires for the other poles of the IEC socket.
    - Preparing and installing these wires is beyond the scope of this guide.

### Crimping

In this section you will need to crimp closed barrel connectors. If you have never performed crimping before, it is strongly recommended that you practice before proceeding.

Cablecraft has an excellent, [:material-book-open-variant: in-depth guide][crimp_guide] to crimping common terminal types.


## Wiring the PSU

### Materials

| Parts                                         | Qty  | Note                                |
|-----------------------------------------------|------|-------------------------------------|
| 16awg stranded hookup wire                    | 0.7m | 14 or 16 gauge                      |
| Fork connectors, 14-16 awg, female insulated  | 1    |                                     |
| Spade connectors, 14-16 awg, insulated        | 3    |                                     |



### Directions

#### Preparing Materials

!!! note
    When crimping closed barrel connectors, the bare wire should extend no more than 1mm from the end of the crimp.

1. Cut one (1) length of hookup wire approximately 30cm (12") long and strip the ends.
2. Crimp a spade terminal on each end and set the wire aside.
3. Cut one (1) length of wire approximately 37cm (15") long and strip the ends.
4. Crimp a spade terminal on one end.
5. Crimp a fork connector on the other end.

<figure markdown>
  [![illustration][wires]{width="480"}][wires]
  <figcaption>The prepared wires should look roughly like the above.</figcaption>
</figure>

####  Wiring Installation

??? Overview
    <iframe src="https://jon-harper.github.io/OmniBox/video/0.9.9/psu_wiring.mp4" frameborder="0" width="100%" height="600px" allowfullscreen></iframe>

<figure markdown>
  [![illustration][psu1]{width="480"}][psu1]
  <figcaption>1. Remove the red wire from the IEC socket's line (L) terminal. Note that this view is from the bottom up; the line (L) wire is the red wire on bottom.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu2]{width="480"}][psu2]
  <figcaption>2. Attach one end of the wire with two spade connectors to the socket's line (L) terminal.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu3]{width="480"}][psu3]
  <figcaption>3. Run the wire through the PSU tray's wiring hole and attach it to either terminal on the power switch.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu4]{width="480"}][psu4]
  <figcaption>4. Attach the spade connector on the remaining wire to the remaining free switch terminal.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu5]{width="480"}][psu5]
  <figcaption>5. Run the wire back through the PSU tray's wiring hole and secure the fork terminal to the PSU's line (L) AC terminal.</figcaption>
</figure>

!!! note
    There are zip tie anchors in the side walls to secure power switch wiring and any excess.

### Finished Reference

![finished illustration][psu_final]

[checklist]: ../printing.md#printed-component-checklist "Print Checklist"

[intro]:   ../img/assembly/core/base/base_final.png

[psu1]: ../img/assembly/core/psu/wire1.png
[psu2]: ../img/assembly/core/psu/wire2.png
[psu3]: ../img/assembly/core/psu/wire3.png
[psu4]: ../img/assembly/core/psu/wire4.png
[psu5]: ../img/assembly/core/psu/wire5.png
[psu6]: ../img/assembly/core/psu/wire6.png
[psu_final]: ../img/assembly/core/psu/wire_finished.png
[wires]: ../img/assembly/core/psu/wires.png