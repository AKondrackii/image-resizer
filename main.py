import os, sys
from PIL import Image

def main():
    params = get_params()
    print(params)
    resize_image(params[0], params[1])

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
    resized_image.save(image_path + '\mountains_resized.jpg')

if __name__ == "__main__":
    main()