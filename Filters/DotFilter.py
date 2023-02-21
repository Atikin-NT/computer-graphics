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

class Sepia(Filter):
    def __init__(self, k = 15):
        self.k = k
        super().__init__()

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        sourceClolor = sourceImage.getpixel((x, y))
        intesity = 0.36 * sourceClolor[0] + 0.53 * sourceClolor[1] + 0.11 * sourceClolor[2]
        
        resultColor = (self.Clamp(intesity + 2 * self.k, 0, 255), 
                       self.Clamp(intesity + 0.5 * self.k, 0, 255), 
                       self.Clamp(intesity - 1 * self.k, 0, 255))
        return resultColor    


class LightCorrection(Filter):
    def __init__(self, c = 25):
        self.c = c
        super().__init__()

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        sourceClolor = sourceImage.getpixel((x, y))
        resultColor = (self.Clamp(sourceClolor[0] + self.c, 0, 255), 
                       self.Clamp(sourceClolor[1] + self.c, 0, 255), 
                       self.Clamp(sourceClolor[2] + self.c, 0, 255))
        return resultColor