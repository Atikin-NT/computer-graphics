from Filters.InvertFilter import InvertFilter
from PIL import Image


def main():
    img = Image.open("data/img1.jpg")
    filter = InvertFilter()
    resultImage = filter.processImage(img)
    resultImage.show()


if __name__ == "__main__":
    main()