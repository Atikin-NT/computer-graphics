from .Filters import Filter
from tqdm import tqdm
import numpy as np


class MedianFilter(Filter):
    def __init__(self, size: int = 2):
        self.size = size

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int, avg=0):
        print(x, y)

        copyImage = np.copy(sourceImage)
        width, height, _ = copyImage.shape

        radiusX = self.size // 2
        radiusY = self.size // 2

        listOfPixels = []
        # print(listOfPixels)

        for i in range(-radiusY, radiusY + 1):
            for j in range(-radiusX, radiusX + 1):
                idX = self.Clamp(x + j, 0, width - 1)
                idY = self.Clamp(y + i, 0, height - 1)

                neighborColor = sourceImage[idX][idY]
                # print(neighborColor)
                listOfPixels.append([neighborColor[0] * 1/3 + neighborColor[1] * 1/3 + neighborColor[2] * 1/3,
                                     neighborColor.tolist()])
                # print(listOfPixels)

        listOfPixels.sort(key=lambda el: el[0])
        # print(len(listOfPixels))
        # print(listOfPixels)

        # resColor = neighborColor[len(listOfPixels) // 2][1]
        return listOfPixels[len(listOfPixels) // 2][1]


