from .Filters import Filter
from PIL import Image


class InvertFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        sourceClolor = sourceImage.getpixel((x, y))
        resultColor = (255-sourceClolor[0],
                       255-sourceClolor[1],
                       255-sourceClolor[2])
        return resultColor
    
class GrayScaleFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        sourceClolor = sourceImage.getpixel((x, y))
        intesity = 0.36 * sourceClolor[0] + 0.53 * sourceClolor[1] + 0.11 * sourceClolor[2]
        resultColor = (self.Clamp(intesity, 0, 255), self.Clamp(intesity, 0, 255), self.Clamp(intesity, 0, 255))
        return resultColor    


