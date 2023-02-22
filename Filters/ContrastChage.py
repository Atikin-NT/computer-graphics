from Filters.Filters import Filter
import numpy as np


class ContrastFilter(Filter):
    def __init__(self, c: int, sourceImage: np.ndarray):
        self.c = c
        self.avg = self.avg(sourceImage)

    def avg(self, sourceImage: np.ndarray) -> float:
        resultR = 0
        resultG = 0
        resultB = 0

        width, height, _ = sourceImage.shape

        for i in range(width):
            for j in range(height):
                neighborColor = sourceImage[i][j]
                resultR += neighborColor[0]
                resultG += neighborColor[1]
                resultB += neighborColor[2]
        return (1/3 * resultR + 1/3 * resultG + 1/3 * resultB) / (width * height)

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        c = self.c
        avg = self.avg
        sourceClolor = sourceImage[x][y]
        resultColor = (self.Clam(avg+(sourceClolor[0]-avg)*c, 0, 255),
                       self.Clam(avg+(sourceClolor[1]-avg)*c, 0, 255),
                       self.Clam(avg+(sourceClolor[2]-avg)*c, 0, 255))
        return resultColor
