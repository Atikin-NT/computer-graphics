from Filters.Filters import Filter
from PIL import Image
import numpy as np
import math


class WavesFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int, avg=0):
        newX = self.Clamp(int(x + 20* math.sin(2 * math.pi * y / 60)), 0, sourceImage.width - 1)
        newY = y
        return sourceImage.getpixel((int(newX), newY))    


