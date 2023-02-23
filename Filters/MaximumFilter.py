from Filters.Filters import Filter
import numpy as np


class MaximumFilter(Filter):
    """Фильтр максимума"""
    def __init__(self, radius: int = 1):
        """
        По сути тоже самое, что и медианный, только мы берем наибольший элемент
        :param radius: радиус для маски (default is 1)
        """
        self.radius = radius

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):

        width, height, _ = sourceImage.shape

        color_arr = []
        for i in range(-self.radius, self.radius + 1):
            for j in range(-self.radius, self.radius + 1):
                idX = self.Clamp(x + i, 0, width - 1)
                idY = self.Clamp(y + j, 0, height - 1)
                neighborColor = sourceImage[idX][idY]
                color_arr.append(neighborColor)
                # print(0.3*neighborColor[0] + 0.59*neighborColor[1] + 0.11*neighborColor[2])

        color_arr.sort(key=lambda brightness: 0.3*brightness[0] + 0.59*brightness[1] + 0.11*brightness[2])
        resultR = color_arr[-1][0]
        resultG = color_arr[-1][1]
        resultB = color_arr[-1][2]

        return resultR, resultG, resultB
