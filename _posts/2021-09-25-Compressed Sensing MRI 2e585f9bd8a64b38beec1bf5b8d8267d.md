---
layout: post
title: Compressed Sensing MRI
date: 2021-09-25
description: 
tags: Compress_Sensing MRI Paper Review
status: Not started
---

3 requirements for CS application

- Transform Sparsity
- Incoherence of undersampling artifacts
- Nonlinear reconstruction

Sampling must be incoherent, (random ideally). 实际上，sampling trajectory 必须满足hardware和physiological constraints。**Non-Cartesian sampling is highly sensitive to system imperfections.**

uniform random sampling 不是在k-space上均匀采样，而应该考虑能量分布的uniform。所以应该是中心位置密一些，外围采样稀疏一些。

## Measuring Incoherence

## Applications of compressed sensing to MRI

### Rapid 3D angiography