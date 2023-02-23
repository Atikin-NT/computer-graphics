from abc import ABCMeta, abstractmethod
from skimage import io
import numpy as np
from tqdm import tqdm


class Filter(metaclass=ABCMeta):
    """Класс филтров"""
    @abstractmethod
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        pass

    def processImage(self, sourceImage: np.ndarray):
        resultImage = np.copy(sourceImage)

        width, height, _ = resultImage.shape
        for i in tqdm(range(width)):
            for j in range(height):
                resultImage[i][j] = self.calculateNewPixelColor(sourceImage, i, j)
        return resultImage

    def Clam(self, value: int, min: int, max: int) -> int:
        if value < min:
            return min
        if value > max:
            return max
        return int(value)


