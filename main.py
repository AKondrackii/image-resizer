# -*- coding:utf -8 -*-
import os
from PIL import Image

def main():
    params = get_params()
    print(params)
    # resize_image(params[0], params[1])
    scale_image(params[0], params[1][0], params[1][1])

def get_params():
    # project_dir = input("Расположение изображения/изображение: \t")
    project_dir = os.getcwd()

    while True:
        try:
            width = int(input("Введите ширину изображения\t"))
        except ValueError:
            print("Это не число, введите заново")
        else:
            break

    while True:
        try:
            height = int(input("Введите высоту изображения\t"))
        except ValueError:
            print("Это не число, введите заново")
        else:
            break
    
    return [ project_dir, ( width, height ) ]

def resize_image(image_path, size):
    original_image = Image.open(image_path + "\mountains.jpg")
    width, height = original_image.size
    
    print("Width = {width}\tHeight = {height}".format(width = width, height = height))

    resized_image = original_image.resize(size)
    width, height = resized_image.size

    print("Width = {width}\tHeight = {height}".format(width = width, height = height))

    resized_image.show()
    resized_image.save(image_path + "\mountains_resized.jpg")

def scale_image(image_path, width = None, height = None):
    original_image = Image.open(image_path + "\mountains.jpg")
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))
 
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')
 
    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(image_path + "\mountains_resized.jpg")
 
    scaled_image = Image.open(image_path + "\mountains_resized.jpg")
    width, height = scaled_image.size
    print('The scaled image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))

if __name__ == "__main__":
    main()