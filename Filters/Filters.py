from abc import ABCMeta, abstractmethod
import numpy as np
from tqdm import tqdm
from progress.bar import IncrementalBar


class Filter(metaclass=ABCMeta):
    """Базовый класс филтров"""
    @abstractmethod
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        """
        Подсчет нового цвета для конкретного пикселя
        :param sourceImage: массив изображения
        :param x: координата X пикселя
        :param y: координата Y пикселя
        :return:
        """
        pass

    def processImage(self, sourceImage: np.ndarray):
        """
        Запуск фильтра
        :param sourceImage: массив изображения
        :return:
        """
        resultImage = np.copy(sourceImage)

        width, height, _ = resultImage.shape
        # bar = IncrementalBar('Image processing', max=width)
        for i in tqdm(range(width)):
        # for i in range(width):
            for j in range(height):
                resultImage[i][j] = self.calculateNewPixelColor(sourceImage, i, j)
            # bar.next()
        # bar.finish()
        return resultImage

    def avg(self, sourceImage: np.ndarray) -> list:
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
        n = width * height
        return [resultR / n, resultG / n, resultB / n]

    def maximums(self, sourceImage: np.ndarray):
        maxClr = [0, 0, 0]
        maxL = 0
        
        width, height, _ = sourceImage.shape

        for i in range(width):
            for j in range(height):
                clr = sourceImage[i][j].astype('uint16')
                ll = clr[0] + clr[1] + clr[2]
                if ll > maxL:
                    maxL = ll
                    maxClr = clr
        return maxClr

    def Clamp(self, value: float, min: int, max: int) -> int:
        """
        Проверка на вход значения в границы
        :param value: само значение
        :param min: минимум
        :param max: максимум
        :return:
        """
        if value < min:
            return min
        if value > max:
            return max
        return int(value)
