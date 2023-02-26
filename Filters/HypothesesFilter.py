from Filters.Filters import Filter
import numpy as np


class ContrastFilter(Filter):
    def __init__(self, sourceImage: np.ndarray, c: int = 8):
        self.c = c
        r, g, b = self.avg(sourceImage)
        self.l_avg = (r + g + b) / 3

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        c = self.c
        l_avg = self.l_avg
        sourceClolor = sourceImage[x][y]
        resultColor = (self.Clamp(l_avg + (sourceClolor[0] - l_avg) * c, 0, 255),
                       self.Clamp(l_avg + (sourceClolor[1] - l_avg) * c, 0, 255),
                       self.Clamp(l_avg + (sourceClolor[2] - l_avg) * c, 0, 255))
        return resultColor


class GrayWorld(Filter):
    def __init__(self, sourceImage: np.ndarray):
        self.r_avg, self.g_avg, self.b_avg = self.avg(sourceImage)
        self.l_avg = (self.r_avg + self.g_avg + self.b_avg) / 3

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        l_avg = self.l_avg
        sourceClolor = sourceImage[x][y]
        resultColor = (self.Clamp(sourceClolor[0] * l_avg / self.r_avg, 0, 255),
                       self.Clamp(sourceClolor[1] * l_avg / self.g_avg, 0, 255),
                       self.Clamp(sourceClolor[2] * l_avg / self.b_avg, 0, 255))
        return resultColor


class RefColorCor(Filter):
    def __init__(self, sourceImage: np.ndarray, src: list, dstrgb: list):
        self.src_rgb = sourceImage[src[0]][src[1]]
        self.dst_rgb = dstrgb

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        sourceClolor = sourceImage[x][y]
        resultColor = (self.Clamp(sourceClolor[0] * self.dst_rgb[0] / self.src_rgb[0], 0, 255),
                       self.Clamp(sourceClolor[1] * self.dst_rgb[1] / self.src_rgb[1], 0, 255),
                       self.Clamp(sourceClolor[2] * self.dst_rgb[2] / self.src_rgb[2], 0, 255))
        return resultColor


class PerfectReflector(Filter):
    def __init__(self, sourceImage: np.ndarray):
        # [255, 255, 255], если есть белый (и смысл тогда?)
        self.maxes = self.maximums(sourceImage)

    def calculateNewPixelColor(self, sourceImage: np.ndarray, x: int, y: int):
        sourceClolor = sourceImage[x][y]
        maxes = self.maxes
        resultColor = (self.Clamp(sourceClolor[0] * 255 / maxes[0], 0, 255),
                       self.Clamp(sourceClolor[1] * 255 / maxes[1], 0, 255),
                       self.Clamp(sourceClolor[2] * 255 / maxes[2], 0, 255))
        return resultColor
