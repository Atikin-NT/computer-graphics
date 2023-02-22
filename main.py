from Filters.InvertFilter import InvertFilter
from Filters.ContrastChage import ContrastFilter
from Filters.BlurFilter import BlurrFilter
from Filters.GaussianFilter import GaussianFilter
from Filters.Transfer import Transfer
from Filters.Turn import Turn
# from PIL import Image

# import numpy as np
from skimage import io
import matplotlib.pyplot as plt


def main():
    img = io.imread("data/img1.jpg")
    filter = InvertFilter()
    resultImage = filter.processImage(img)
    filter = ContrastFilter(2, img)
    resultImage = filter.processImage(resultImage)
    filter = BlurrFilter()
    resultImage = filter.processImage(resultImage)
    # filter = GaussianFilter(3, 5)
    # resultImage = filter.processImage(resultImage)
    filter = Transfer(50, 70)
    resultImage = filter.processImage(resultImage)
    filter = Turn(50, 50, 50)
    resultImage = filter.processImage(resultImage)
    plt.imshow(resultImage)
    plt.show()


if __name__ == "__main__":
    main()
