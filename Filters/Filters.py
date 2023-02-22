from abc import ABCMeta, abstractmethod
from PIL import Image
from progress.bar import IncrementalBar


class Filter(metaclass=ABCMeta):
    """Класс филтров"""
    @abstractmethod
    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        pass

    def processImage(self, sourceImage: Image.Image):
        resultImage = sourceImage.copy()
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
        n = sourceImage.width * sourceImage.height
        return [resultR / n, resultG / n, resultB / n]
    
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


