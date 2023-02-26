from Filters.Filters import Filter
import numpy as np

class DilationFilter(Filter):
    def __init__(self, mask=[
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 0]
    ]):
        self.mask = mask
    
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
            mask = self.mask
            MW, MH = len(mask[0]), len(mask)
            res = [0, 0, 0]
            for j in range(-MH // 2, MH // 2 + 1):
                for i in range(-MW // 2, MW // 2 + 1):
                    if 0 <= x + i < len(sourceImage) and 0 <= y + j < len(sourceImage[0]):
                        if mask[i][j]:
                            if sourceImage[x + i][y + j][0] > res[0]:
                                res = sourceImage[x + i][y + j]
            return res
    
class ErosionFilter(Filter):
    def __init__(self, mask=[
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 0]
    ]):
        self.mask = mask
    
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        mask = self.mask
        MW, MH = len(mask[0]), len(mask)
        res = [255, 255, 255]
        for j in range(-MH // 2, MH // 2 + 1):
            for i in range(-MW // 2, MW // 2 + 1):
                if 0 <= x + i < len(sourceImage) and 0 <= y + j < len(sourceImage[0]):
                    if mask[i][j]:
                        if sourceImage[x + i][y + j][0] < res[0]:
                            res = sourceImage[x + i][y + j]
        return res
    

class OpeningFilter():
    def processImage(self, sourceImage: np.ndarray):
        """
        Запуск фильтра
        :param sourceImage: массив изображения
        :return:
        """
        stage1 = ErosionFilter().processImage(sourceImage)
        stage2 = DilationFilter().processImage(stage1)
        return stage2
    

class ClosingFilter():
    def processImage(self, sourceImage: np.ndarray):
        """
        Запуск фильтра
        :param sourceImage: массив изображения
        :return:
        """
        stage1 = DilationFilter().processImage(sourceImage)
        stage2 = ErosionFilter().processImage(stage1)
        return stage2

class TopHatFilter():
    def processImage(self, sourceImage: np.ndarray):
        """
        Запуск фильтра
        :param sourceImage: массив изображения
        :return:
        """
        opened = OpeningFilter().processImage(sourceImage)
        return sourceImage - opened

class BlackHatFilter():
    def processImage(self, sourceImage: np.ndarray):
        """
        Запуск фильтра
        :param sourceImage: массив изображения
        :return:
        """
        closed = ClosingFilter().processImage(sourceImage)
        return closed - sourceImage

class GradFilter():
    def processImage(self, sourceImage: np.ndarray):
        """
        Запуск фильтра
        :param sourceImage: массив изображения
        :return:
        """
        dilated = DilationFilter().processImage(sourceImage)
        erosed = ErosionFilter().processImage(sourceImage)
        return dilated - erosed