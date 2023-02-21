from .Filters import Filter
from PIL import Image


class ContrastFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int, avg: float = 0):
        c = 8
        sourceClolor = sourceImage.getpixel((x, y))
        resultColor = (self.Clamp(avg+(sourceClolor[0]-avg)*c, 0, 255),
                       self.Clamp(avg+(sourceClolor[1]-avg)*c, 0, 255),
                       self.Clamp(avg+(sourceClolor[2]-avg)*c, 0, 255))
        return resultColor
