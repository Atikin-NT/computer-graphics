from .Filters import Filter
from PIL import Image


class InvertFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        sourceClolor = sourceImage.getpixel((x, y))
        resultColor = (255-sourceClolor[0],
                       255-sourceClolor[1],
                       255-sourceClolor[2])
        return resultColor


