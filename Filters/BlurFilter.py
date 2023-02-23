from .MatrixFilter import MatrixFilter
import numpy as np


class BoxBlur(MatrixFilter):
    def __init__(self):
        sizeX = 3
        sizeY = 3
        kernel = [[0]*sizeY]*sizeX
        for i in range(sizeX):
            for j in range(sizeY):
                kernel[i][j] = 1.0 / float(sizeX * sizeY)
        super().__init__(kernel)


class GaussianFilter(MatrixFilter):
    def __init__(self, radius: int = 3, sigma: float = 2):
        size = 2 * radius + 1
        gauss_kernel = np.zeros((size, size))
        norm = .0
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                gauss_kernel[i + radius, j + radius] = np.exp(-((i ** 2 + j ** 2) / (sigma ** 2)))
                norm += gauss_kernel[i + radius, j + radius]
        for i in range(size):
            for j in range(size):
                gauss_kernel[i, j] = gauss_kernel[i, j] / norm
        super().__init__(gauss_kernel)


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
    def __init__(self, n=3):
        kernel = [[0 if i != j else 1/n for j in range(n)] for i in range(n)]
        super().__init__(kernel)


class EdgeDetection(MatrixFilter):
    def __init__(self):
        kernel = [
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]
        ]
        super().__init__(kernel)
