import sys, os, argparse
from platform import system
from PIL import Image

photo_extensions = ['jpg', 'png']

def get_photos():
  photos = []
  for root, subfolders, files in os.walk(os.getcwd()):
    for file in files:
      filesplit = list(file.split('.'))
      if filesplit[-1] in photo_extensions and 'thumbnail' not in filesplit[-2]:
        photos.append(os.path.join(root, file))
  return photos

def thumbnailing(path, size):
  filename = os.path.split('\\' if system == 'Windows' else '/')[-1]
  photo = Image.open(path)
  photo.thumbnail([size, size], Image.ANTIALIAS)
  photo.save(filename.lower() + ".thumbnail.jpg", "JPEG")
  print(filename)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-s" ,"--size", type=int, help="You must specify the width!", default=512)
  args = parser.parse_args()

  for photo in get_photos():
    thumbnailing(photo, args.size)

if __name__ == "__main__":
  main()
