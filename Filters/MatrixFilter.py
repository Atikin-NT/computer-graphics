from .Filters import Filter
from PIL import Image


class MatrixFilter(Filter):
    def __init__(self, kernel: list[list]):
        self.kernel = kernel

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        radiusX = int(len(self.kernel) / 2)
        radiusY = int(len(self.kernel[0]) / 2)

        resultR = 0
        resultG = 0
        resultB = 0

        for l in range(-radiusY, radiusY + 1):
            for k in range(-radiusX, radiusX + 1):
                idX = self.Clamp(x + k, 0, sourceImage.width - 1)
                idY = self.Clamp(y + l, 0, sourceImage.height - 1)
                neighborColor = sourceImage.getpixel((idX, idY))
                resultR += neighborColor[0] * self.kernel[k + radiusX][l + radiusY]
                resultG += neighborColor[1] * self.kernel[k + radiusX][l + radiusY]
                resultB += neighborColor[2] * self.kernel[k + radiusX][l + radiusY]

        return (self.Clamp(resultR, 0, 255),
                self.Clamp(resultG, 0, 255),
                self.Clamp(resultB, 0, 255))
