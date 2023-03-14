from Filters.Filters import Filter
import numpy as np
from math import sin, pi
import random


class WavesFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        width, height, _ = sourceImage.shape
        newX = self.Clamp(int(x + 20 * sin(2 * pi * x / 30)), 0, width - 1)
        newY = y
        return sourceImage[int(newX)][int(newY)]


class GlassFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        width, height, _ = sourceImage.shape
        newX = x + (random.random() - 0.5) * 10
        newY = y + (random.random() - 0.5) * 10
        return sourceImage[
            self.Clamp(int(newX), 0, width - 1)][
            self.Clamp(int(newY), 0, height - 1)]
