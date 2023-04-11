# Image Edit

```bash
CUDA_VISIBLE_DEVICES=1 python edit_by_point.py --prompt "blue cloth" --input_image "./images/1571811257876870.jpg" --input_point 294 151 --task "inpainting" --output "./images/"
```


# Object Remove
```bash
CUDA_VISIBLE_DEVICES=1 python edit_by_point.py --prompt "blue cloth" --input_image "./images/1571811257876870.jpg" --input_point 294 151 --task "remove" --output "./images/"
```


## Citing Segment Anything

If you use SAM or SA-1B in your research, please use the following BibTeX entry. 

```
@article{kirillov2023segany,
  title={Segment Anything}, 
  author={Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C. and Lo, Wan-Yen and Doll{\'a}r, Piotr and Girshick, Ross},
  journal={arXiv:2304.02643},
  year={2023}
}
```
