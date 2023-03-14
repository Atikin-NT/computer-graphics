from .Filters import Filter
import numpy as np

class MiddlePoint(Filter):
    def __init__(self, rad: int = 2):
        self.rad = rad
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        width, height, _ = sourceImage.shape

        tmpArr = []
        for i in range(-self.rad, self.rad + 1):
            for j in range(-self.rad, self.rad + 1):
                idX = self.Clamp(x + i, 0, width - 1)
                idY = self.Clamp(y + j, 0, height - 1)

                tmpArr.append(sourceImage[idX][idY][0])

        tmpArr.sort()
        min = tmpArr[0]
        # print(tmpArr)
        max = tmpArr[len(tmpArr) - 1]
        newColor = np.uint8((int(min) + int(max)) // 2)
        # print(min, max, newColor)
        return [newColor, newColor, newColor, 255]


