from Filters.Filters import Filter
import numpy as np
import math


class Turn(Filter):
    def __init__(self, x0: int = 0, y0: int = 0, angle_of_rotation: float = 0):
        self.x0 = x0
        self.y0 = y0
        self.angle_of_rotation = angle_of_rotation

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int, avg=0):
        newX = int((x - self.x0) * math.cos(self.angle_of_rotation) - (y - self.y0) * math.sin(self.angle_of_rotation) + self.x0)
        newY = int((x - self.x0) * math.sin(self.angle_of_rotation) + (y - self.y0) * math.cos(self.angle_of_rotation) + self.y0)

        width, height, _ = sourceImage.shape
        if newX >= width or newY >= height or newY < 0 or newX < 0:
            return 0, 0, 0
        return sourceImage[newX][newY]


