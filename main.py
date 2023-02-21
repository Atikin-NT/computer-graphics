from Filters.InvertFilter import InvertFilter
# from Filters.ContrastChage import ContrastFilter
from Filters.BlurFilter import BlurrFilter
from Filters.Transfer import Transfer
from Filters.Turn import Turn
from PIL import Image


def main():
    img = Image.open("data/img1.jpg")
    # filter = InvertFilter()
    # filter = ContrastFilter()
    # filter = BlurrFilter()
    # filter = Transfer(100, 70)
    filter = Turn(50, 50, 50)
    resultImage = filter.processImage(img)
    resultImage.show()


if __name__ == "__main__":
    main()
