from Filters.InvertFilter import InvertFilter
from Filters.ContrastChage import ContrastFilter
from Filters.BlurFilter import BlurrFilter
# from PIL import Image

# import numpy as np
from skimage import io
import matplotlib.pyplot as plt

def main():
    img = io.imread("data/img1.jpg")
    # filter = InvertFilter()
    filter = ContrastFilter()
    resultImage = filter.processImage(img)
    plt.imshow(resultImage)
    plt.show()


if __name__ == "__main__":
    main()
