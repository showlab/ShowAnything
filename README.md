
<p align="center">
<img src="./assets/1681232055007.jpg" width="700px"/>  
<br>
</p>

# ShowAnything
Edit and Generate Anything In Any Image and Video.

**Motivation of this repo**: [Segment Anything](https://github.com/facebookresearch/segment-anything) offers powerful perception capabilities and interfaces with points and boxes. We believe that the interface ability has the potential to greatly drive the development of generation and editing applications. We will be posting some application developments from our lab here that are compatible with both Segment Anything and Generation, thanks.
 
## ToDo
- [ ] Customization (Lora or dreambooth)
- [ ] Video editing with point interaction
- [ ] Hugging Face Demo
- [ ] ...


## Installation
Please follow the [segment anything](https://github.com/facebookresearch/segment-anything#model-checkpoints) to creating the environment and download the model checkpoint (vit_l, vit_l or vit_b)


## Image

[Hugging Face Demo](https://huggingface.co/spaces/weijiawu/ImageEditAnything) is now available, but please note that it may run slowly due to being currently executed on a low-end CPU.


<p align="center">
<img src="./assets/1681314820494.jpg" width="800px"/>  
<br>
</p>




### Edit with point click
The ultimate goal of this task is to achieve control over the generation of complex scenes, such as dense crowds and department stores.

See the [here](./ImageEdit). Using points to edit and control. Enjoy it! 


<p align="center">
<img src="./assets/fig1.png" width="700px"/>  
<br>
</p>


### Object Merge


<p align="center">
<img src="./assets/fig2.png" width="700px"/>  
<br>
</p>


### Object Remove

<p align="center">
<img src="./assets/fig3.png" width="700px"/>  
<br>
</p>

## Video

### Zero-shot Editing Anything in Any Video

Replace the person in the video: 

<p align="center">
<img src="./assets/video/showcase_1.gif" width="700px"/>  
<br>
</p>

Customize the clothes of the person in the video:

<p align="center">
<img src="./assets/video/showcase_3.gif" width="700px"/>  
<br>
</p>

<p align="center">
<img src="./assets/video/showcase_2.gif" width="700px"/>  
<br>
</p>

More results:

<table class="center">
<tr>
  <td style="text-align:center;"><b>Input Video</b></td>
  <td style="text-align:center;" colspan="3"><b>Output Video</b></td>
</tr>
<tr>
  <td><img src="./assets/video/original.gif"></td>
  <td><img src="./assets/video/A soldier is dancing_crop.gif"></td>      
  <td><img src="./assets/video/Donald Trump is dancing_crop.gif"></td>
  <td><img src="./assets/video/Iron Man is dancing_crop.gif"></td>
</tr>
<tr>
  <td width=25% style="text-align:center;color:gray;">"Input Video"</td>
  <td width=25% style="text-align:center;">"A soldier is dancing"</td>
  <td width=25% style="text-align:center;">"Donald Trump is dancing"</td>
  <td width=25% style="text-align:center;">"Iron Man is dancing"</td>
</tr>
</table>

<table class="center">
<tr>
  <td style="text-align:center;"><b>Input Video</b></td>
  <td style="text-align:center;" colspan="3"><b>Output Video</b></td>
</tr>
<tr>
  <td><img src="./assets/video/original.gif"></td>
  <td><img src="./assets/video/A man is dancing in skirt and wearing black stockings.gif"></td>      
  <td><img src="./assets/video/A man is dancing in jeans.gif"></td>
  <td><img src="./assets/video/A man is dancing in shorts.gif"></td>
</tr>
<tr>
  <td width=25% style="text-align:center;color:gray;">"Input Video"</td>
  <td width=25% style="text-align:center;">"A man is dancing in skirt and wearing black stockings"</td>
  <td width=25% style="text-align:center;">"A man is dancing in jeans"</td>
  <td width=25% style="text-align:center;">"A man is dancing in shorts"</td>
</tr>
</table>


## Transform Image Into Unique Paragraph
Image to paragraph is available, please refer to [Image2Paragraph](https://github.com/showlab/Image2Paragraph), and enjoy!


<p align="center">
<img src="./assets/1681360400667.jpg" width="700px"/>  
<br>
</p>

## Acknowledgements
- [Segment Anything](https://github.com/facebookresearch/segment-anything)
- [Caption-Anything](https://github.com/ttengwang/Caption-Anything) (hugging face demo)
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion)

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