from Filters.Filters import Filter
from PIL import Image
import math


class Turn(Filter):
    def __init__(self, x0: int = 0, y0: int = 0, angle_of_rotation: float = 0):
        self.x0 = x0
        self.y0 = y0
        self.angle_of_rotation = angle_of_rotation

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int, avg=0):
        newX = (x - self.x0) * math.cos(self.angle_of_rotation) - (y - self.y0) * math.sin(self.angle_of_rotation) + self.x0
        newY = (x - self.x0) * math.sin(self.angle_of_rotation) + (y - self.y0) * math.cos(self.angle_of_rotation) + self.y0

        if newX >= sourceImage.width or newY >= sourceImage.height:
            return (0, 0, 0)
        return sourceImage.getpixel((newX, newY))


