---
layout: project
title: Subspace reconstruction for high-temporal resolution ASL
description: Using subspace to reconstruct high-temporal resolution angiography based on the kinetic model
img: /assets/img/subspace.png
importance: 1
category: MRI reconstruction
date: 2022-10-01
enddate: 2023-06-01
supervisor: Thomas Okell
---

4D combined angiography and perfusion using radial imaging and arterial spin labelling (CAPRIA) allows dynamic angiograms to be reconstructed. However, the current approach uses a relatively low temporal resolution to ensure sufficient k-space coverage within each frame. Therefore, the dynamic angiograms change abruptly between adjacent frames. In addition, the signal variations within the long temporal window introduce additional artefacts to each frame. In this work, we use a kinetic model of the angiographic signal to provide additional information to constrain the reconstruction of highly undersampled data. A subspace reconstruction was developed to compress the signal representation during reconstruction to reduce computational requirements. In-vivo results showed smoother variation of the angiographic signal in the temporal dimension compared to the original approach.