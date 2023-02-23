from Filters.InvertFilter import InvertFilter
from Filters.ContrastChage import ContrastFilter
from Filters.BlurFilter import BlurrFilter
from Filters.GaussianFilter import GaussianFilter
from Filters.Transfer import Transfer
from Filters.MedianFilter import MedianFilter
from Filters.ContoursFilter import SobelFilter
from Filters.Turn import Turn
from Filters.MaximumFilter import MaximumFilter
# from PIL import Image

# import numpy as np
from skimage import io
import matplotlib.pyplot as plt


def main():
    img = io.imread("data/img1.jpg")
    # filter = InvertFilter()
    # resultImage = filter.processImage(img)
    # filter = ContrastFilter(2, img)
    # resultImage = filter.processImage(img)
    # filter = BlurrFilter()
    # resultImage = filter.processImage(img)
    # filter = GaussianFilter(3, 5)
    # resultImage = filter.processImage(img)
    # filter = Transfer(50, 70)
    # resultImage = filter.processImage(img)
    # filter = Turn(50, 50, 50)
    filter = MedianFilter()
    resultImage = filter.processImage(img)

    plt.imshow(resultImage)
    plt.show()

    filter = SobelFilter()
    resultImage = filter.processImage(resultImage)

    plt.imshow(resultImage)
    plt.show()

    filter = MaximumFilter()
    resultImage = filter.processImage(resultImage)
    # filter = SobelFilter()
    # filter = MaximumFilter()
    plt.imshow(resultImage)
    plt.show()


if __name__ == "__main__":
    main()
