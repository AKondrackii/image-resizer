# -*- coding:utf -8 -*-
import os, glob
from PIL import Image

def main():
    params = get_params()
    for picture in glob.glob(os.getcwd() + "\original\*.*"):
        resize_image(picture, params)

def get_params():
    # project_dir = input("Расположение изображения/изображение: \t")

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
    
    return ( width, height )

def resize_image(image_path, size):
    original_image = Image.open(image_path)
    original_image.thumbnail(size, Image.ANTIALIAS)
    original_image.save(image_path.replace("\\original", "\\resized"))

if __name__ == "__main__":
    try:
        os.mkdir("original")
    except:
        print("Папка original уже создана")
    
    try:
        os.mkdir("resized")
    except:
         print("Папка resized уже создана")
    
    main()