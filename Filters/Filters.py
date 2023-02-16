from abc import ABCMeta, abstractmethod
from PIL import Image


class Filter(metaclass=ABCMeta):
    """Класс филтров"""
    @abstractmethod
    def calculateNewPixelColor(self, sourceImage: Image, x: int, y: int):
        pass

    @abstractmethod
    def processImage(self, sourceImage: Image):
        pass

    def Clam(self, value: int, max: int, min: int):
        if value < min:
            return min
        if value > max:
            return max
        return value


