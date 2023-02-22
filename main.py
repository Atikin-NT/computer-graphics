from Filters.DotFilter import *
from Filters.BlurFilter import *
from Filters.ContoursFilter import *
from Filters.GeometryFilter import *
from Filters.HypothesesFilter import *
from PIL import Image


def main():
    img = Image.open("data/Lenna600.png")
    # filter = InvertFilter()
    # filter = RefColorCor(img, [250, 150], [173, 204, 194])
    filter = PerfectReflector(img)
    resultImage = filter.processImage(img)
    resultImage.show()


if __name__ == "__main__":
    main()
