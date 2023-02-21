from Filters.Filters import Filter
from PIL import Image
import numpy as np
import math
import random


class GlassFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int, avg=0):
        newX = x + (random.random() - 0.5) * 10
        newY = y + (random.random() - 0.5) * 10
        return sourceImage.getpixel((
            self.Clamp(int(newX), 0, sourceImage.width - 1),
            self.Clamp(int(newY), 0, sourceImage.height - 1)))    


