---
layout: post
title: Design and Analysis of a Practical 3D Cones Trajectory
date: 2021-09-25
description: 
tags: ASL MRI Paper
status: In progress
---

## 不懂的：

1. 3DPR, UTE
2. more twists → fewer total readouts, readout duty cycle, sampling density, SNR efficiency(**the loss in SNR as compared to uniform density sampling**)
3. 为什么RES和FOV必须满足这样的条件？

<div class="row mt-3"><div class="col-sm mt-3 mt-md-0"><img class="img-fluid rounded z-depth-1" src="{{ site.baseurl }}/assets/img/Design%20and%20Analysis%20of%20a%20Practical%203D%20Cones%20Trajec%2070c1220156c949d0baba3bf2dcd56f96/Untitled.png" data-zoomable></div></div>

1. 为什么两条相邻的interleave最短距离要满足 >1/FOV 的条件？

    non-uniform sampling ，**no sphere of diameter 1/FOV may be empty**

## 思考：

3D Cone Trajectory**优点**：

more twists added in trajectory → higher readout time per repetition (readout duty cycle) → higher overall SNR/ fewer total readouts → sampling density uniform, higher SNR efficiency

设计 Trajectory 要考虑的问题：

1. sufficient to cover the FOV       2.  **anisotropies** (significant anisotropies will **add artifacts** and **increase noise**)

**BURS** , **gridding** reconstruction

1. 选择cone surface
2. 从cone surface上选择trajectory
3. 从采样间隔角度考虑，计算trajectory上每点的最小斜率
4. 从硬件角度考虑，gradient coil有gradient 和 slew rate的大小限制

**non-uniform data weighting of radial trajectories causes an intrinsic loss in SNR**