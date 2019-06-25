import os, glob
from PIL import Image

class EditImage():
    def __init__(self):
        # super().__init__(self)
        self.init_edit_image()

    def init_edit_image(self):
        print("edit image module load and work")

    def resize(self, image_path, resolution):
        original_image = Image.open(image_path)
        original_image.thumbnail(resolution, Image.ANTIALIAS)
        original_image.save(image_path.replace(".jpg", "") + "_resized.jpg")

# EditImage().resize(image_path="C:/Users/chebu/Pictures/D5dBZsIXxSY.jpg", resolution=(800, 600))