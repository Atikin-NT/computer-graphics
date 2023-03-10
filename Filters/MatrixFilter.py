from Filters.Filters import Filter
import numpy as np


class MatrixFilter(Filter):
    """Класс для помтроения матричных фильтров"""
    def __init__(self, kernel: list[list]):
        """
        :param kernel: яндро фильтра - матрица (создается в классе наследнике)
        """
        self.kernel = kernel

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        radiusX = len(self.kernel) // 2
        radiusY = len(self.kernel[0]) // 2

        resultR = 0
        resultG = 0
        resultB = 0

        width, height, _ = sourceImage.shape

        for l in range(-radiusY, radiusY + 1):
            for k in range(-radiusX, radiusX + 1):
                idX = self.Clamp(x + k, 0, width - 1)
                idY = self.Clamp(y + l, 0, height - 1)
                neighborColor = sourceImage[idX][idY]
                resultR += neighborColor[0] * self.kernel[k + radiusX][l + radiusY]
                resultG += neighborColor[1] * self.kernel[k + radiusX][l + radiusY]
                resultB += neighborColor[2] * self.kernel[k + radiusX][l + radiusY]

        return (self.Clamp(resultR, 0, 255),
                self.Clamp(resultG, 0, 255),
                self.Clamp(resultB, 0, 255))


class EmbossingMatrix(Filter):
    def __init__(self, kernel: list[list]):
        """
        :param kernel: яндро фильтра - матрица (создается в классе наследнике)
        """
        self.kernel = kernel

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        radiusX = len(self.kernel) // 2
        radiusY = len(self.kernel[0]) // 2

        resultR = 0
        resultG = 0
        resultB = 0

        width, height, _ = sourceImage.shape

        for l in range(-radiusY, radiusY + 1):
            for k in range(-radiusX, radiusX + 1):
                idX = self.Clamp(x + k, 0, width - 1)
                idY = self.Clamp(y + l, 0, height - 1)
                neighborColor = sourceImage[idX][idY]
                resultR += neighborColor[0] * self.kernel[k + radiusX][l + radiusY]
                resultG += neighborColor[1] * self.kernel[k + radiusX][l + radiusY]
                resultB += neighborColor[2] * self.kernel[k + radiusX][l + radiusY]

        return (self.Clamp((resultR+255) / 2, 0, 255),
                self.Clamp((resultG+255) / 2, 0, 255),
                self.Clamp((resultB+255) / 2, 0, 255))
