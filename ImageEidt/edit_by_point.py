import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
from diffusers import StableDiffusionInpaintPipeline
import imutils
from PIL import Image
import argparse
def show_mask(mask, ax, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30/255, 144/255, 255/255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)
    
def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)   
    
def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2))   

import sys
sys.path.append("..")
from segment_anything import sam_model_registry, SamPredictor



    
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--prompt",
        type=str,
        nargs="?",
        default="a photo of a lion on a mountain top at sunset",
        help="the prompt to render"
    )
    parser.add_argument(
        "--input_image",
        type=str,
        nargs="?",
        help="./"
    ) 
    parser.add_argument(
        "--input_point",
        type=int,
        nargs='+',
        help="./"
    )
    parser.add_argument(
        "--output",
        type=str,
        nargs="?",
        help="./"
    )
    parser.add_argument(
        "--task",
        type=str,
        nargs="?",
        help="inpainting/remove"
    )
    
    opt = parser.parse_args()
    
    
    sam_checkpoint = "./model/sam_vit_h_4b8939.pth"
    model_type = "vit_h"

    device = "cuda"

    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)


    predictor = SamPredictor(sam)


    image = cv2.imread(opt.input_image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    predictor.set_image(image)
    input_point = np.array([[int(i) for i in opt.input_point]])
    input_label = np.array([1])

    plt.figure(figsize=(10,10))
    plt.imshow(image)
    show_points(input_point, input_label, plt.gca())
    plt.axis('on')
    plt.show() 
    plt.savefig('./{}/vis_point.png'.format(opt.output),dpi=100) #save myfig
    
    print(input_point)
    masks, scores, logits = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=True,
    )

    for i, (mask, score) in enumerate(zip(masks, scores)):
        plt.figure(figsize=(5,5))
        plt.imshow(image)
        cv2.imwrite('./{}/mask_{}.png'.format(opt.output,i),mask.astype(np.uint8)*255)


        contours,_ = cv2.findContours(mask.astype(np.uint8),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 

        x, y, w, h = cv2.boundingRect(contours[0])

        show_mask(mask, plt.gca())
        show_points(input_point, input_label, plt.gca())
        plt.title(f"Mask {i+1}, Score: {score:.3f}", fontsize=18)

        plt.savefig('./{}/vis_mask_{}.png'.format(opt.output,i),dpi=100) #save myfig
        plt.axis('off')
        plt.show()  

    # inpainting
    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-inpainting",
        torch_dtype=torch.float32,
    )


    pipe = pipe.to("cuda")


    # "pure background"
    if opt.task == "inpainting":
        prompt = opt.prompt
        mask = (masks[1]*1).astype(np.uint8)
    else:
        prompt = "pure background"
        
        mask = (masks[2]*1).astype(np.uint8)

        kernel = np.ones((7, 7), dtype=np.uint8)
        mask = cv2.dilate(mask, kernel, 1)

    h,w = image.shape[:2]
    image = cv2.resize(image,(512,512))
    mask = cv2.resize(mask,(512,512))

    image = pipe(prompt=prompt, image=image, mask_image=mask).images[0]
    image = image.resize((w,h))
    image.save("./{}/out.png".format(opt.output))
    
    
if __name__ == "__main__":
    main()
    