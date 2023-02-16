from abc import ABCMeta, abstractmethod
from PIL import Image


class Filter(metaclass=ABCMeta):
    """Класс филтров"""
    @abstractmethod
    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        pass

    def processImage(self, sourceImage: Image.Image):
        resultImage = sourceImage.copy()
        for i in range(resultImage.width):
            for j in range(resultImage.height):
                resultImage.putpixel((i, j), self.calculateNewPixelColor(sourceImage, i, j))
        return resultImage

    def Clam(self, value: int, min: int, max: int) -> int:
        if value < min:
            return min
        if value > max:
            return max
        return int(value)


