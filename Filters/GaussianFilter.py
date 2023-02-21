from Filters.MatrixFilter import MatrixFilter
import numpy as np


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
