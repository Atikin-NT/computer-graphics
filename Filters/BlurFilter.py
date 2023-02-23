from .MatrixFilter import MatrixFilter
import numpy as np

class BlurrFilter(MatrixFilter):
    def __init__(self):
        sizeX = 3
        sizeY = 3
        kernel = [[0]*sizeY]*sizeX
        for i in range(sizeX):
            for j in range(sizeY):
                kernel[i][j] = 1.0 / float(sizeX * sizeY)
        super().__init__(kernel)

class SharpenFilter(MatrixFilter):
    def __init__(self):
        kernel = [[-1, -1, -1],
                  [-1, 9, -1],
                  [-1, -1, -1]]
        super().__init__(kernel)


class SharpenFilter2(MatrixFilter):
    def __init__(self):
        kernel = [[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]]
        super().__init__(kernel)

class SharpenFilter3(MatrixFilter):
    def __init__(self):
        kernel = [[-1/10, -2/10, -1/10],
                  [-2/10, 22/10, -2/10],
                  [-1/10, -2/10, -1/10]]
        super().__init__(kernel)

class MotionFilter(MatrixFilter):
    def __init__(self, n = 3):
        kernel = [ [0 if i!=j else 1/n for j in range(n)] for i in range(n)]
        super().__init__(kernel)

class EdgeDetection(MatrixFilter):
    def __init__(self):
        kernel = [
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]
        ]
        super().__init__(kernel)