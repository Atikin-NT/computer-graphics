from Gistogramma import Gistogramm
from .Filters import Filter
import numpy as np
# import matplotlib.pyplot as plt

class LinearStretching(Filter):
    def __init__(self, sourseImage: np.ndarray):
        gist = Gistogramm(sourseImage)

        self.minBrightness = gist.getMinBrightness()
        self.maxBrightness = gist.getMaxBrightness()

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        pixelColor = sourceImage[x][y][0]
        # print(pixelColor)

        newPixelColor = (pixelColor - self.minBrightness) * (255 / (self.maxBrightness - self.minBrightness))
        return (self.Clamp(newPixelColor, 0, 255))
        # return newPixelColor