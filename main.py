import os
import cv2
import cupy as cp
import numpy as np
import argparse
from utils import resize_image_gpu, apply_grayscale

f_in = 'input'
f_out = 'output'

def prepare_output_folder():
    if not os.path.exists(f_out):
        os.makedirs(f_out)
        print(f"Created output folder: {f_out}")
    else:
        for file in os.listdir(f_out):
            os.remove(os.path.join(f_out, file))
        print(f"Cleared existing images from {f_out}")

def get_file_size(path):
    return os.path.getsize(path)

def process_images(resize_percent):
    prepare_output_folder()

    for file in os.listdir(f_in):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            p_in = os.path.join(f_in, file)
            p_out = os.path.join(f_out, file)

            print(f"Processing {file}...")

            original_size = get_file_size(p_in)
            img = cv2.imread(p_in)

            if img is None:
                print(f"Skipping {file}: Cannot read image.\n")
                continue

            # Apply grayscale filter first
            gray_img = apply_grayscale(img)

            h, w = gray_img.shape[:2]
            scale_factor = (resize_percent) ** 0.5
            new_w = max(int(w * scale_factor), 64)
            new_h = max(int(h * scale_factor), 64)

            img_resized = resize_image_gpu(gray_img, (new_w, new_h))
            cv2.imwrite(p_out, img_resized, [cv2.IMWRITE_JPEG_QUALITY, 80])

            resized_size = get_file_size(p_out)
            print(f"Original: {original_size//1024} KB → Resized: {resized_size//1024} KB\n")

    print(f"All images processed using {int(resize_percent * 100)}% size rule.\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--percent", type=float, default=0.1,
                        help="Resize target as a percentage of original file size (e.g., 0.1 = 10%)")
    args = parser.parse_args()
    process_images(args.percent)