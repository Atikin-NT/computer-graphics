from .Filters import Filter
from PIL import Image


class MatrixFilter(Filter):
    def __init__(self, kernel: list[list]):
        self.kernel = kernel

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int, avg):
        radiusX = int(len(self.kernel) / 2)
        radiusY = int(len(self.kernel[0]) / 2)

        resultR = 0
        resultG = 0
        resultB = 0

        for l in range(-radiusY, radiusY + 1):
            for k in range(-radiusX, radiusX + 1):
                idX = self.Clam(x + k, 0, sourceImage.width - 1)
                idY = self.Clam(y + l, 0, sourceImage.height - 1)
                neighborColor = sourceImage.getpixel((idX, idY))
                resultR += neighborColor[0] * self.kernel[k + radiusX][l + radiusY]
                resultG += neighborColor[1] * self.kernel[k + radiusX][l + radiusY]
                resultB += neighborColor[2] * self.kernel[k + radiusX][l + radiusY]

        return (self.Clam(resultR, 0, 255),
                self.Clam(resultG, 0, 255),
                self.Clam(resultB, 0, 255))
