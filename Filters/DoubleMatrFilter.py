from .Filters import Filter
from PIL import Image
from math import sqrt


class DoubleMatrFilter(Filter):
    def __init__(self, kernelx, kernely: list[list]):
        self.kernelx = kernelx
        self.kernely = kernely
    
    def calculateNewPixelColorK(self, sourceImage: Image.Image, x: int, y: int, kernel):
        radiusX = len(kernel) // 2
        radiusY = len(kernel[0]) // 2

        resultR = 0
        resultG = 0
        resultB = 0

        for l in range(-radiusY, radiusY + 1):
            for k in range(-radiusX, radiusX + 1):
                idX = self.Clamp(x + k, 0, sourceImage.width - 1)
                idY = self.Clamp(y + l, 0, sourceImage.height - 1)
                neighborColor = sourceImage.getpixel((idX, idY))
                resultR += neighborColor[0] * kernel[k + radiusX][l + radiusY]
                resultG += neighborColor[1] * kernel[k + radiusX][l + radiusY]
                resultB += neighborColor[2] * kernel[k + radiusX][l + radiusY]
        return [resultR, resultG, resultB]

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        Rx, Gx, Bx = self.calculateNewPixelColorK(sourceImage, x, y, self.kernelx)
        Ry, Gy, By = self.calculateNewPixelColorK(sourceImage, x, y, self.kernely)
        intensity1 = sqrt((Rx + Gx + Bx) * (Rx + Gx + Bx) + (Ry + Gy + By) * (Ry + Gy + By)) / 3
        R = sqrt(Rx * Rx + Ry * Ry)
        G = sqrt(Gx * Gx + Gy * Gy)
        B = sqrt(Bx * Bx + By * By)
        intensity2 = (R + G + B) / 3
        return (self.Clamp(intensity1, 0, 255),
                self.Clamp(intensity1, 0, 255),
                self.Clamp(intensity1, 0, 255))