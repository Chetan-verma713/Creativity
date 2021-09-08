import time
from PIL import Image, ImageGrab


def takescreenshot():  # make a function
    image = ImageGrab.grab()
    image.show()
    return image


if __name__ == "__main__":
    time.sleep(0)

    image = takescreenshot()
    data = image.load()
    print(data)
    # make  image colourful from 0 to 255

    for i in range(35, 56):
        for j in range(0, 255):
            data
