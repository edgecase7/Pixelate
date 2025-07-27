# Makefile for the Pixelate Project

# Phony targets are not actual files
.PHONY: install run generate process clean

# Install all dependencies from requirements.txt
install:
	pip install -r requirements.txt

# Run the entire pipeline: generate images then process them
run: generate process

# Generate the input images
generate:
	python3 generate_images.py

# Process the images (grayscale and resize)
process:
	python3 main.py --percent 0.1

# Clean up by deleting the input and output directories
clean:
	python3 -c "import os, shutil; [shutil.rmtree(d) for d in ['input', 'output'] if os.path.exists(d)]"