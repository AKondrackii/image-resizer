import os
from PIL import Image

def main():
    params = get_params()
    print(params)
    resize_image(params[0], params[1])

def get_params():
    where_dir = input("Расположение изображения/изображение: \t")

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
    

    return [ where_dir, [ width, height ] ]

def resize_image(image_path, size):
    # original_image = Image.open(image_path)

    width = size[0]
    height = size[1]

    print("Width = {width}\tHeight = {height}".format(width = width, height = height))

if __name__ == "__main__":
    main()