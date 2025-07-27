# Pixelate: GPU Image Processor 🚀

## Project Overview

Pixelate is a GPU-accelerated image processing pipeline built to run in the Google Colab environment. The application automatically downloads a batch of source images, processes them by applying a grayscale filter and resizing them to a smaller footprint, and saves the results directly to Google Drive. The primary goal is to demonstrate an efficient, GPU-powered workflow for handling batch image operations.

---

## Features

* **GPU Acceleration:** Leverages NVIDIA CUDA through the CuPy library for fast processing.
* **Automated Image Sourcing:** Downloads a fresh batch of images for each run using `requests`.
* **Batch Processing:** Automatically processes all images found in the `input` directory.
* **Image Transformation:** Applies two main transformations:
    1.  **Grayscale Conversion:** Converts color images to black and white.
    2.  **Resizing:** Reduces image dimensions to a fraction of their original size.
* **Seamless Colab/Drive Integration:** Designed to work directly within a user's Google Drive via a Colab notebook.

---

## Technology Stack

* **Language:** Python 3
* **Core Libraries:**
    * `CuPy`: For GPU array computations.
    * `OpenCV`: For image reading, writing, and transformations.
    * `NumPy`: For numerical operations.
    * `Pillow`: For image handling.
* **Environment:** Google Colab (with GPU runtime) & Google Drive

---

## File Descriptions

* `main.py`: The main executable script. It orchestrates the workflow from preparing folders to processing images and saving the results.
* `utils.py`: A module containing helper functions for image manipulation, specifically `apply_grayscale` and `resize_image_gpu`.
* `generate_images.py`: A script responsible for downloading the initial set of images from an online source into the `input` folder.
* `requirements.txt`: Lists all the necessary Python packages required to run the project.
* `MAKEFILE`: Provides simple command-line targets for common tasks like cleaning directories and running the scripts (for local development).
* `README.md`: This file—providing documentation for the project.

---

## How to Run the Project

This project is designed to be run in a Google Colab notebook.

### Step 1: Upload to Google Drive

Upload the entire `Pixelate` project folder to the main directory of your Google Drive (`My Drive`).

### Step 2: Open and Set Up Google Colab

1.  Create a new Colab notebook and select a **GPU runtime** (`Runtime` > `Change runtime type` > `T4 GPU`).
2.  Mount your Google Drive by running this cell:
    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```

### Step 3: Execute the Project

Copy and paste the entire code block below into a new Colab cell and run it. The script handles all subsequent steps automatically.

```python
import os
import shutil


project_folder_name = "Pixelate"


# Define and change to the project path
project_path = os.path.join("/content/drive/MyDrive/", project_folder_name)
os.chdir(project_path)
print(f"Changed directory to: {os.getcwd()}")

# Install requirements
print("\nInstalling requirements...")
!pip install -r requirements.txt -q

# Generate input images
print("\nGenerating new input images...")
!python3 generate_images.py

# Run the main processing script
print("\nStarting image processing (grayscale + resize)...")
!python3 main.py --percent 0.1

print("\n Pixelate has finished processing all images!")
