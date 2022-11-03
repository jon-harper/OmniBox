---
title: PSU Wiring
summary: Instructions for wiring the power supply.
authors: Jon Harper
date: 2022-10-31
---

At this point, it is a good idea to wire the power supply, power switch, and IEC socket. There are zip tie anchors available in the sides to secure the power switch wiring. The large hole in the right PSU tray mount allows wiring to pass through.

!!! caution
    In this section you will need to crimp closed barrel connectors. If you have never performed crimping before, it is strongly recommended that you practice before proceeding.

    Cablecraft has an excellent, [in-depth guide][crimp_guide] to crimping common terminal types.

<figure markdown>
  [![illustration][intro]{width="480"}][intro]
  <figcaption></figcaption>
</figure>

### Materials

| Parts                                         | Qty  | Note                                |
|-----------------------------------------------|------|-------------------------------------|
| 16awg stranded hookup wire                    | 0.7m | 14 or 16 gauge                      |
| Fork connectors, 14-16 awg, female insulated  | 1    |                                     |
| Spade connectors, 14-16 awg, insulated        | 3    |                                     |

!!! important
    For this example, we will use red wires for the power switch and use them for the *positive* (+) run from the power socket to switch to PSU.
    
    If you are using black wires, connect the *negative* (-) terminals with the crimped wires instead.

!!! caution
    Be careful of polarity and check your work!

!!! note
    IEC sockets typically ship with short wires with precrimped connectors attached. If yours is not pre-wired, you will need two additional wires for the other poles of the IEC socket.

    Preparing and installing these wires is beyond the scope of this guide.

### Directions

#### Preparing Materials

1. Cut one (1) length of hookup wire approximately 30cm (12") long and strip the ends.
2. Crimp a spade terminal on each end.
3. Cut one (1) length of wire approximately 37cm (15") long and strip the ends.
4. Crimp the second wire with a spade terminal on one end.
5. Crimp a fork connector on the other end.

####  Wiring Installation

1. Remove the red wire from the IEC socket's positive (+) terminal.
2. Attach one end of the wire with two spade connectors to the socket's positive (+) terminal.
3. Run the wire through the PSU tray's wiring hole and attach it to the power switch.
4. Attach the spade connector on the remaining wire to the remaining free switch terminal.
5. Run the wire back through the PSU tray's wiring hole.
6. Secure the fork terminal to the PSU's positive (+) AC terminal.
7. If desired, use zip ties to secure the wiring.

### Finished Reference

[checklist]: ../printing.md#printed-component-checklist "Print Checklist"

[intro]:   ../img/assembly/core/base/base_final.png