---
title: Insert Locations
summary: Heat set insert locations for the Main Body and Base.
authors: Jon Harper
date: 2022-11-01
steps:
  crossbar:
    - txt: Two (2) inserts.
      img: ../img/assembly/hsi/main_crossbar.webp
      img_txt: 
  main_front:
    - txt: Six (6) inserts.<br>Skip this step for a Unified build.
      img: ../img/assembly/hsi/main_front1.webp
      img_txt: Front/rear joint inserts
    - txt: Four (4) inserts.
      img: ../img/assembly/hsi/main_front2.webp
      img_txt: MCU and Lid inserts
    - txt: Eight (8) inserts.
      img: ../img/assembly/hsi/main_front3.webp
      img_txt: Side Panel inserts
    - txt: Two (2) inserts.
      img: ../img/assembly/hsi/main_front4.webp
      img_txt: Front panel inserts
    - txt: |
        Four (4) inserts.
        <br>Note: the surface is at a 50 degree angle.
      img: ../img/assembly/hsi/main_front5.webp
    - txt: |
        Eight (8) inserts.
        <br>Note: Full HSI builds only.
      img: ../img/assembly/hsi/main_front_full.webp
      img_txt: Lower bay inserts
  main_rear:
    - txt: Six (6) inserts.
      img: ../img/assembly/hsi/main_rear1.webp
      img_txt: Lid inserts
    - txt: Eight (8) inserts.
      img: ../img/assembly/hsi/main_rear2.webp
      img_txt: Side Panel inserts
    - txt: Six (6) inserts.
      img: ../img/assembly/hsi/main_rear3.webp
      img_txt: Rear Panel inserts
    - txt: Two (2) inserts.
      img: ../img/assembly/hsi/main_rear4.webp
      img_txt: MCU inserts
    - txt: |
        Sixteen (16) inserts.
        <br>Note: Full HSI builds only.
      img: ../img/assembly/hsi/main_rear5.webp
      img_txt: Lower bay inserts
  base_front:
    - txt: |
        Four (4) inserts.
      img: ../img/assembly/hsi/base_front1.webp
      img_txt: Top inserts.
    - txt: Four (4) inserts.
      img: ../img/assembly/hsi/base_front2.webp
      img_txt: Bottom panel inserts.
    - txt: |
        Four (4) inserts.
        <br>Skip this step for Unified builds.
      img: ../img/assembly/hsi/base_front3.webp
      img_txt: Front/rear joint inserts.
  base_rear:
    - txt: |
        Four (4) inserts.
      img: ../img/assembly/hsi/base_rear1.webp
      img_txt: Top inserts.
    - txt: |
        Four (4) inserts.
      img: ../img/assembly/hsi/base_rear2.webp
      img_txt: Bottom panel inserts.
    - txt: |
        Four (4) inserts.
      img: ../img/assembly/hsi/base_rear3.webp
      img_txt: IEC socket and rear panel inserts.
---

{% import 'assembly.md' as assy %}

This page contains a map of where heat set inserts should be installed for the Main Body and Base, both regular HSI and Full HSI.

## Main Body

### Crossbar

This part requires two (2) inserts.

{{ assy.render_steps(steps.crossbar, '480px') }}

### Front

This part requires twenty-four (24) total inserts for a Front/Rear build and eighteen (18) for a Unified build. Full HSI builds
add another eight (8) inserts.

{{ assy.render_steps(steps.main_front, '480px') }}

### Rear

This part requires twenty-two (22) inserts for an HSI build and thirty-eight (38) for a Full HSI build.

{{ assy.render_steps(steps.main_rear, '480px') }}

## Base 

### Front

This part requires twelve (12) inserts for a Front/Rear build and eight (8) inserts
for a Unified build.

{{ assy.render_steps(steps.base_front, '480px') }}

### Rear

The standard HSI build uses twelve (12) inserts.

{{ assy.render_steps(steps.base_rear, '480px') }}