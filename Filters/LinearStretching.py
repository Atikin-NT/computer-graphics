from Gistogramma import Gistogramm
from .Filters import Filter
import numpy as np
# import matplotlib.pyplot as plt

class LinearStretching(Filter):
    def __init__(self, sourseImage: np.ndarray):
        minR = 255
        minG = 255
        minB = 255
        maxR = 0
        maxG = 0
        maxB = 0



        gist = Gistogramm(sourseImage)

        self.minBrightness = gist.getMinBrightness()
        self.maxBrightness = gist.getMaxBrightness()

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        pixelColor = sourceImage[x][y]
        # print(pixelColor)

        # R = (pixelColor[0] - self.minBrightness) * (255 / (self.maxBrightness - self.minBrightness))
        # G = (pixelColor[1] - self.minBrightness) * (255 / (self.maxBrightness - self.minBrightness))
        # B = (pixelColor[2] - self.minBrightness) * (255 / (self.maxBrightness - self.minBrightness))

        newPixelColor = (pixelColor - self.minBrightness) * (255 / (self.maxBrightness - self.minBrightness))
        # return (self.Clamp(R, 0, 255),
        #         self.Clamp(G, 0, 255),
        #         self.Clamp(B, 0, 255))
        return self.Clamp(newPixelColor[0], 0, 255)
