from .Filters import Filter
import numpy as np


class MedianFilter(Filter):
    def __init__(self, radius: int = 1):
        self.radius = radius

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int, avg=0):
        copyImage = np.copy(sourceImage)
        width, height, _ = copyImage.shape

        listOfPixels = []

        for i in range(-self.radius, self.radius + 1):
            for j in range(-self.radius, self.radius + 1):
                idX = self.Clamp(x + j, 0, width - 1)
                idY = self.Clamp(y + i, 0, height - 1)

                neighborColor = sourceImage[idX][idY]
                listOfPixels.append([neighborColor[0] * 1/3 + neighborColor[1] * 1/3 + neighborColor[2] * 1/3,
                                     neighborColor.tolist()])

        listOfPixels.sort(key=lambda el: el[0])
        return listOfPixels[len(listOfPixels) // 2][1]


