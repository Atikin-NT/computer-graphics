from .Filters import Filter
from PIL import Image


class ContrastFilter(Filter):
    def __init__(self, c = 1.35):
        self.c = c
        super().__init__()
    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int, avg: float = 0):
        sourceClolor = sourceImage.getpixel((x, y))
        resultColor = (self.Clamp(avg+(sourceClolor[0]-avg)*self.c, 0, 255),
                       self.Clamp(avg+(sourceClolor[1]-avg)*self.c, 0, 255),
                       self.Clamp(avg+(sourceClolor[2]-avg)*self.c, 0, 255))
        return resultColor
