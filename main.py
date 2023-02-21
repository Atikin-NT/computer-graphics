from Filters.DotFilter import GrayScaleFilter
from Filters.ContrastChage import ContrastFilter
from Filters.BlurFilter import SharpFilter2
from Filters.ContoursFilter import SobelFilter
from PIL import Image


def main():
    img = Image.open("data/img1.jpg")
    # filter = InvertFilter()
    filter = SobelFilter()
    resultImage = filter.processImage(img)
    resultImage.show()


if __name__ == "__main__":
    main()
