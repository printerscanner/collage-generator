# Collage Generator

This is a Python script that generates collages by combining random images from a directory onto an image-sized canvas with a random background color. It uses the Python Imaging Library (PIL) to manipulate images and create the final poster.


## Prerequisites

Before using this script, you need to make sure you have the following:

Python installed on your system (Python 3 is recommended).

The `PIL` (Pillow) library installed. You can install it using `pip`:

    pip install pillow

## How to Use

1. Make a folder called `images`` in the root directory and go out into the world and find materials for your collage. Place your images as PNGs in a the folder.

2. Customize the image paper size by changing the `image_width` and `image_height` variables in the script. The default values are set to 2000x2000 pixels.

Run the script in your terminal or Python environment.
    python poster_generator.py

The script will randomly select 6 images from the "images" directory and place them on the image-sized canvas, adjusting their sizes and positions.

The final poster will be saved as a PNG file with a random name in the same directory as the script.

Script Explanation

    os, secrets, random, and PIL are imported for various functionalities used in the script.

    The script lists all PNG files in the "images" directory using os.listdir and a list comprehension.

    It defines the image paper size as image_width and image_height and generates a random background color.

    A target image is created using Image.new, which will serve as the canvas for the poster.

    Six random images are selected from the "images" directory using random.sample.

    The poster_generator function takes the selected images, canvas size, and the target image as parameters and pastes the images onto the canvas with random positions and sizes.

    The final poster is saved with a random filename using target_img.save.

Please ensure that you have a sufficient number of PNG images in the "images" directory to ensure variety in the generated poster. You can also modify the number of images to be selected or the canvas size according to your preferences.

Enjoy creating your unique posters with this script!