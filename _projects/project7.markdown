---
layout: project
title: Learning 3D models from 2D images in the wild
description: Generate 3D models by learning from 2D images in the wild like ImageNet
img: /assets/img/3d_model.png
importance: 1
category: Generative 3D-aware image synthesis
date: 2022-09-01
enddate: 2023-01-16
supervisor: Guangrun Wang, Philip Torr
---

Generation of 3D models has been a challenge for a long time. Researchers used to learn 3D models in an explicit way using 3D datasets using supervised learning. Recent advances successfully learned 3D models from 2D images. However, unlike 2D generation, these methods still highly rely on the well structured dataset which contains either multi-view of an object or the camera pose of each image. However, such dataset is expensive to acquire, which limits the potential benefit of including more images in the training. Therefore, in this work, we aim to reconstruct images from Imagenet which has much higher diversity and no information on camera pose. Following previous work, we leverage efficient triplane representation to learn 3D models from 2D images in the Imagenet. Many classes in Imagenet do not contain views from certain directions at all. Min-view was adopted to select views most similar to those in the dataset, preventing the model from fitting every view to be similar to the limited views in dataset. We developed the training strategy which uses the stylegan2 discriminator to initialize generator and projected discriminator to refine generated images. We demonstrated generated multi-view images and corresponding 3D models directly learned from different classes in Imagenet.

[Github Repo](https://github.com/Michaelsqj/eg3d)

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/3dmodel_results.png' | relative_url }}" alt="" title="invivo"/>
    </div>
</div>
<div class="caption">
    Examples of comparison on two classes in ImageNet.
</div>