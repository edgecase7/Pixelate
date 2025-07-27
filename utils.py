import cupy as cp
import cv2
import numpy as np

def resize_image_gpu(image, new_size):
    # Convert image to GPU array
    img_gpu = cp.asarray(image)

    # Resize using OpenCV on CPU (OpenCV GPU resize is less stable across systems)
    img_cpu = cp.asnumpy(img_gpu)
    resized = cv2.resize(img_cpu, new_size, interpolation=cv2.INTER_AREA)

    # Convert back to GPU array (if needed elsewhere)
    return resized

def apply_grayscale(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image