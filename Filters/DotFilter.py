from .Filters import Filter
import numpy as np
from math import sqrt


class InvertFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        sourceClolor = sourceImage[x][y]
        resultColor = (255-sourceClolor[0],
                       255-sourceClolor[1],
                       255-sourceClolor[2])
        return resultColor


class GrayScaleFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        sourceClolor = sourceImage[x][y]
        intensity = 0.3 * sourceClolor[0] + 0.59 * sourceClolor[1] + 0.11 * sourceClolor[2]
        resultColor = (self.Clamp(intensity, 0, 255), 
                       self.Clamp(intensity, 0, 255), 
                       self.Clamp(intensity, 0, 255))
        return resultColor


class Sepia(Filter):
    def __init__(self, k=15):
        self.k = k

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        sourceClolor = sourceImage[x][y]
        intensity = 0.36 * sourceClolor[0] + 0.53 * sourceClolor[1] + 0.11 * sourceClolor[2]

        resultColor = (self.Clamp(intensity + 2 * self.k, 0, 255),
                       self.Clamp(intensity + 0.5 * self.k, 0, 255),
                       self.Clamp(intensity - 1 * self.k, 0, 255))
        return resultColor


class LightCorrection(Filter):
    def __init__(self, c=25):
        self.c = c

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        sourceColor = sourceImage[x][y]
        resultColor = (self.Clamp(sourceColor[0] + self.c, 0, 255),
                       self.Clamp(sourceColor[1] + self.c, 0, 255),
                       self.Clamp(sourceColor[2] + self.c, 0, 255))
        return resultColor


class Binarise(Filter):
    def __init__(self, clr=[127, 127, 127], threshold = 127):
        self.clr = clr
        self.threshold = threshold

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        sourceClolor = sourceImage[x][y]
        clr = self.clr
        threshold = self.threshold
        dist = sqrt((sourceClolor[0] - clr[0])**2 + 
                    (sourceClolor[1] - clr[1])**2 + 
                    (sourceClolor[2] - clr[2])**2)
        if dist < threshold:
            resultColor = [255, 255, 255]
        else:
            resultColor = [0, 0, 0]
        return resultColor

class BlackAndWhite(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        pixelColor = sourceImage[x][y]
        resultColor = pixelColor[0] * 1/3 + pixelColor[1] * 1/3 + pixelColor[2] * 1/3

        return self.Clamp(resultColor, 0, 255)
