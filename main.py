import sys, os
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

def thumbnailing(path, size=512):
  filename = os.path.split('\\' if system == 'Windows' else '/')[-1]
  photo = Image.open(path)
  photo.thumbnail([size, size], Image.ANTIALIAS)
  photo.save(filename.lower() + ".thumbnail.jpg", "JPEG")
  print(filename)

def main():
  for photo in get_photos():
    thumbnailing(photo, int(sys.argv[1]))

if __name__ == "__main__":
  if (len(sys.argv) >= 2): main()
  else: print("You must specify the width!")
