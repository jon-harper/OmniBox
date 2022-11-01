---
title: PSU Wiring
summary: Instructions for wiring the power supply.
authors: Jon Harper
date: 2022-10-31
---

At this point, it is a good idea to wire the power supply, power switch, and IEC socket. There are zip tie anchors available in the sides to secure the power switch wiring. The large hole in the right PSU tray mount allows wiring to pass through.

<figure markdown>
  [![illustration][intro]{width="480"}][intro]
  <figcaption></figcaption>
</figure>

### Materials

| Parts                                         | Qty  | Note                                |
|-----------------------------------------------|------|-------------------------------------|
| 16awg stranded hookup wire                    | 0.5m | 14 or 16 gauge                      |
| Fork connectors, 14-16 awg, female insulated  | 1    |                                     |
| Spade connectors, 14-16 awg, insulated        | 3    |                                     |

!!! important
    For this example, we will use red wires for the power switch and use them for the *positive* (+) run from the power socket to switch to PSU.
    
    If you are using black wires, connect the *negative* (-) terminals with the crimped wires instead.

!!! note
    IEC sockets typically ship with short wires with precrimped connectors attached. If your socket did not come with wiring, you will need two additional wires for the other poles of the IEC socket.

    Preparing and installing these wires is beyond the scope of this guide.

### Directions

!!! caution
    In this section you will need to crimp wires. If you have never performed wiring crimping before, it is strongly recommended that you practice before proceeding.

1. Cut the hookup wire into two equal length pieces approximately 30cm/12" long and strip.
2. Crimp one wire with a spade terminal on each end.
3. Crimp the second wire with a spade terminal on one end. Crimp a fork connector on the other end.
4. Remove the red wire from the IEC socket's positive (+) terminal.
5. Attach one end of the wire with two spade connectors to the socket's positive (+) terminal.
6. Run the wire through the PSU tray's wiring hole and attach it to the power switch.
7. Attach the spade connector on the remaining wire to the remaining free switch terminal.
8. Run the wire back through the PSU tray's wiring hole.
9. Secure the fork terminal to the PSU's positive (+) AC terminal.
10. If desired, use zip ties to secure the wiring.

### Finished Reference

!!! caution
    Be careful of polarity and check your work!

[checklist]: ../printing.md#printed-component-checklist "Print Checklist"

[intro]:   ../img/assembly/core/base/base_final.png