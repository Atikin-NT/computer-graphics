from .Filters import Filter
# from PIL import Image

import numpy as np

class ContrastFilter(Filter):
    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int, avg=0):
        c = 8
        sourceClolor = sourceImage[x][y]
        resultColor = (self.Clam(avg+(sourceClolor[0]-avg)*c, 0, 255),
                       self.Clam(avg+(sourceClolor[1]-avg)*c, 0, 255),
                       self.Clam(avg+(sourceClolor[2]-avg)*c, 0, 255))
        return resultColor
