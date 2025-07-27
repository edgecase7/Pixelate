import os
import requests
from PIL import Image
from io import BytesIO
import numpy as np

def download_and_save_image(url, path, image_num, total_images):
    for attempt in range(1, 4):
        print(f"Downloading image {image_num}/{total_images} (Attempt {attempt}/3)...")
        try:
            # Added a user-agent header to be respectful to the API
            headers = {'User-Agent': 'PixelateImageProcessor/1.0'}
            response = requests.get(url, timeout=15, headers=headers)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                img.save(path)
                print(f"Image {image_num}/{total_images} downloaded and saved as {path}\n")
                return True
            else:
                print(f"Failed to download image {image_num}/{total_images}: Status {response.status_code}")
        except Exception as e:
            print(f"Error downloading image {image_num}/{total_images} on attempt {attempt}: {e}")
    print(f"Failed to download image {image_num}/{total_images} after 3 attempts.\n")
    return False

def generate_images(folder='input', limit=20):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created folder: {folder}")
    else:
        # Clean folder if exists
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))
        print(f"Cleared existing images from {folder}")

    for i in range(1, limit + 1):
        # Using Unsplash as the new source
        url = f"https://picsum.photos/seed/{np.random.randint(1000000)}/512/512"
        save_path = os.path.join(folder, f"photo_{i}.jpg")
        download_and_save_image(url, save_path, i, limit)

if __name__ == '__main__':
    generate_images()