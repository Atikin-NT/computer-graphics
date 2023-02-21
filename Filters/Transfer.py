from Filters.Filters import Filter
from PIL import Image


class Transfer(Filter):
    def __init__(self, transferX: int = 50, transferY: int = 0):
        self.transferX = transferX
        self.transferY = transferY

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int, avg=0):
        newX = self.transferX + x
        newY = self.transferY + y

        if newX >= sourceImage.width or newY >= sourceImage.height:
            return (0, 0, 0)
        return sourceImage.getpixel((newX, newY))


