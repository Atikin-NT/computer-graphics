from .Filters import Filter
# from PIL import Image

import numpy as np

class InvertFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int, avg=0):
        sourceClolor = sourceImage[x][y]
        resultColor = (255-sourceClolor[0],
                       255-sourceClolor[1],
                       255-sourceClolor[2])
        return resultColor


