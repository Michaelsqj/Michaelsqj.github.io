---
layout: post
title: Free-Breathing Pediatric Chest MRI Performance of Self-Navigated Golden- Angle Ordered Conical Ultrashort Echo Time Acquisition
date: 2021-09-25
description: 
tags: ASL MRI Paper
status: Completed
---

## 问题：

1. 为什么conical UTE 能diffuse motion & aliasing artifacts?
2. 4D flow chest MRI
3. self-navigation: the first few samples of each cone interleaf were processed to compute motion waveforms
4. UTE imaging: can image tissue with very short $T\_2$

## 思考

**UTE + 3D conical golden ratio trajectory**

***An optimal radial profile order based on the golden ratio for time-resolved MRI***

3D radial 的缺点：填满 k-space 比较低效，导致在scan time和undersampling之间取舍

**RF-spoiled gradient echo (SPGR) sequence** + **3D conical k-space sampling trajectory** + **golden ratio permutation**  + **self-navigation**

***Self- gated cardiac cine MRI.***

3 different reconstruction results: 

1. with all data
2. with 50% data
3. with soft-gating motion correction. **coil-clustering**,  select highly correlated coils whose **navigators** most closely matched a dominant respiratory waveform

                              ***Robust self-navigated body MRI using dense coil arrays.***

parallel imaging + compressed sensing reconstruction using ***BART***

**4D flow acquisition**

***Comprehensive motion- compensated highly accelerated 4D flow MRI with ferumoxytol enhancement for pediatric congenital heart disease***