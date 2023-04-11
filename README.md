# ShowAnything
Based on [Segment Anything](https://github.com/facebookresearch/segment-anything), we plan to create a very interesting project for image, video generation and editing.

**Motivation of this repo**: Segment Anything offers powerful perception capabilities and interfaces with points and boxes. We believe that the interface ability has the potential to greatly drive the development of generation and editing applications. We will be posting some application developments from our lab here that are compatible with both Segment Anything and Generation, thanks.
 

## Installation
Please follow the [segment anything](https://github.com/facebookresearch/segment-anything#model-checkpoints) to creating the environment and download the model checkpoint (vit_l, vit_l or vit_b)


## Image

### Edit
The ultimate goal of this task is to achieve control over the generation of complex scenes, such as dense crowds and department stores.


![](./assets/fig1.jpg)

### Object Merge
![](./assets/fig2.jpg)

### Object Remove
![](./assets/fig3.jpg)

### Customization


## Video
<img src="./assets/video/original.gif" width="200"/>  <img src="./assets/video/A soldier is dancing_crop.gif" width="200"/>  <img src="./assets/video/Donald Trump is dancing_crop.gif" width="200"/> <img src="./assets/video/Iron Man is dancing_crop.gif" width="200"/>




## Citation
If you find this project helpful for your research, please consider citing the following BibTeX entry.
```BibTex
@article{kirillov2023segany,
  title={Segment Anything}, 
  author={Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C. and Lo, Wan-Yen and Doll{\'a}r, Piotr and Girshick, Ross},
  journal={arXiv:2304.02643},
  year={2023}
}

```