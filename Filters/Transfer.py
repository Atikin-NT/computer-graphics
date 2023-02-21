from Filters.Filters import Filter
from PIL import Image
import numpy as np


class Transfer(Filter):
    def __init__(self, transferX: int = 50, transferY: int = 0):
        self.transferX = transferX
        self.transferY = transferY

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int, avg=0):
        newX = self.transferX + x
        newY = self.transferY + y

        width, height, _ = sourceImage.shape
        if newX >= width or newY >= height:
            return 0, 0, 0
        return sourceImage[newX][newY]


