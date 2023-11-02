import os
import secrets
import random
from PIL import Image

# list all png files in directory
image_dir = os.path.abspath("images")
files = [s for s in os.listdir(image_dir) if s.endswith('.png')]

# Get image size
image_width = 2000
image_height = 2000

# Generate random color
random_color = "#" + str(secrets.token_hex(3))


target_img = Image.new("RGBA", (image_width, image_height),
                       random_color)

sample = random.sample(files, 6)


def poster_generator(sample, image_height, image_width, target_img):
    for n in sample:
        try:
            random_size = random.randint(1, 3)
            img = Image.open('images/' + n)

            width, height = img.size
            img.thumbnail((width//random_size, height//random_size))

            # paste the image at the correct position
            i = random.randint(1, image_width//4)
            j = random.randint(1, image_height//4)

            target_img.paste(img, (i, j), mask=img)
        except:
            pass


    target_img.save(str(random.random()) + ".png".format("png"))

poster_generator(sample, image_height, image_width, target_img)
