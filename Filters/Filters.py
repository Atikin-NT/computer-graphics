from abc import ABCMeta, abstractmethod
from PIL import Image
from progress.bar import IncrementalBar


class Filter(metaclass=ABCMeta):
    """Класс филтров"""
    @abstractmethod
    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int, avg=0):
        pass

    def processImage(self, sourceImage: Image.Image):
        resultImage = sourceImage.copy()
        # avg = self.avg(resultImage)
        bar = IncrementalBar('Image processing', max = resultImage.width)
        for i in range(resultImage.width):
            for j in range(resultImage.height):
                resultImage.putpixel((i, j), self.calculateNewPixelColor(sourceImage, i, j))
            bar.next()
        bar.finish()
        return resultImage

    def avg(self, sourceImage: Image.Image):
        resultR = 0
        resultG = 0
        resultB = 0
        for i in range(sourceImage.width):
            for j in range(sourceImage.height):
                neighborColor = sourceImage.getpixel((i, j))
                resultR += neighborColor[0]
                resultG += neighborColor[1]
                resultB += neighborColor[2]
        return (1/3 * resultR + 1/3 * resultG + 1/3 * resultB) / (sourceImage.width * sourceImage.height)

    def Clamp(self, value: int, min: int, max: int) -> int:
        if value < min:
            return min
        if value > max:
            return max
        return int(value)


