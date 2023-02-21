from abc import ABCMeta, abstractmethod
# from PIL import Image
from skimage import io
import numpy as np

class Filter(metaclass=ABCMeta):
    """Класс филтров"""
    @abstractmethod
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int, avg=0):
        pass

    def processImage(self, sourceImage: np.ndarray):
        resultImage = np.copy(sourceImage)
        avg = self.avg(resultImage)

        width, height, _ = resultImage.shape
        for i in range(width):
            for j in range(height):
                resultImage[i][j] = self.calculateNewPixelColor(sourceImage, i, j, avg)
        return resultImage

    def avg(self, sourceImage: np.ndarray):
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

    def Clam(self, value: int, min: int, max: int) -> int:
        if value < min:
            return min
        if value > max:
            return max
        return int(value)


