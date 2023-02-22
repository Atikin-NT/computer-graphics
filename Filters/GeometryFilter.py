from Filters.Filters import Filter
from PIL import Image
import numpy as np
from math import sin, pi
import random


class WavesFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        newX = self.Clamp(int(x + 20* sin(2 * pi * y / 60)), 0, sourceImage.width - 1)
        newY = y
        return sourceImage.getpixel((int(newX), newY))    

class GlassFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        newX = x + (random.random() - 0.5) * 10
        newY = y + (random.random() - 0.5) * 10
        return sourceImage.getpixel((
            self.Clamp(int(newX), 0, sourceImage.width - 1),
            self.Clamp(int(newY), 0, sourceImage.height - 1)))   
