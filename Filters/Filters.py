from abc import ABCMeta, abstractmethod
from skimage import io
import numpy as np
from progress.bar import IncrementalBar
from PIL import Image


class Filter(metaclass=ABCMeta):
    """Класс филтров"""
    @abstractmethod
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        pass

    def processImage(self, sourceImage: np.ndarray):
        resultImage = np.copy(sourceImage)

        width, height, _ = resultImage.shape
        bar = IncrementalBar('Image processing', max=resultImage.width)
        for i in range(width):
            for j in range(height):
                resultImage[i][j] = self.calculateNewPixelColor(sourceImage, i, j)
            bar.next()
        bar.finish()
        return resultImage
    
    def maximums(self, sourceImage: Image.Image):
        maxR = 0
        maxG = 0
        maxB = 0
        for i in range(sourceImage.width):
            for j in range(sourceImage.height):
                clr = sourceImage.getpixel((i, j))
                if (clr[0] > maxR): maxR = clr[0]
                if (clr[1] > maxG): maxG = clr[1]
                if (clr[2] > maxB): maxB = clr[2]
        return [maxR, maxG, maxB]

    def Clamp(self, value: int, min: int, max: int) -> int:
        if value < min:
            return min
        if value > max:
            return max
        return int(value)
