from Gistogramma import Gistogramm
from .Filters import Filter
import numpy as np
# import matplotlib.pyplot as plt

class LinearStretching(Filter):
    def __init__(self, gist: Gistogramm):
        self.minBrightness = gist.getMinBrightness()
        self.maxBrightness = gist.getMaxBrightness()

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        pixel = sourceImage[x][y]
        pixelBrightness = pixel[0] * 1/3 + pixel[1] * 1/3 + pixel[2] * 1/3

        pixelBrightness = self.Clamp(pixelBrightness, 0, 255)

        # print(self.maxBrightness, self.minBrightness)
        newBrightness = (pixelBrightness - self.minBrightness) * (255 / (self.maxBrightness - self.minBrightness))
        newBrightness = self.Clamp(newBrightness, 0, 255)

        k = newBrightness / pixelBrightness

        R = pixel[0] * k
        G = pixel[1] * k
        B = pixel[2] * k

        return (self.Clamp(R, 0, 255),
                self.Clamp(G, 0, 255),
                self.Clamp(B, 0, 255))