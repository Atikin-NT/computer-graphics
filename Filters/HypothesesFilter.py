from Filters.Filters import Filter
from PIL import Image


class GrayWorld(Filter):
    def __init__(self, sourceImage: Image.Image):
        self.r_avg, self.g_avg, self.b_avg = self.avg(sourceImage)
        self.l_avg = (self.r_avg + self.g_avg + self.b_avg) / 3
        super().__init__()

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        sourceClolor = sourceImage.getpixel((x, y))
        resultColor = (self.Clamp(sourceClolor[0] * self.l_avg / self.r_avg, 0, 255),
                       self.Clamp(sourceClolor[1] * self.l_avg / self.g_avg, 0, 255),
                       self.Clamp(sourceClolor[2] * self.l_avg / self.b_avg, 0, 255))
        return resultColor


class RefColorCor(Filter):
    def __init__(self, sourceImage: Image.Image, src: list, dstrgb: list):
        self.src_rgb = sourceImage.getpixel(tuple(src))
        self.dst_rgb = dstrgb
        super().__init__()

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        sourceClolor = sourceImage.getpixel((x, y))
        resultColor = (self.Clamp(sourceClolor[0] * self.dst_rgb[0] / self.src_rgb[0], 0, 255),
                       self.Clamp(sourceClolor[1] * self.dst_rgb[1] / self.src_rgb[1], 0, 255),
                       self.Clamp(sourceClolor[2] * self.dst_rgb[2] / self.src_rgb[2], 0, 255))
        return resultColor


class PerfectReflector(Filter):
    def __init__(self, sourceImage: Image.Image):
        self.maxes = self.maximums(sourceImage) # [255, 255, 255], если есть белый (и смысл тогда?)
        super().__init__()

    def calculateNewPixelColor(self, sourceImage: Image.Image, x: int, y: int):
        sourceClolor = sourceImage.getpixel((x, y))
        resultColor = (self.Clamp(sourceClolor[0] * 255 / self.maxes[0], 0, 255),
                       self.Clamp(sourceClolor[1] * 255 / self.maxes[1], 0, 255),
                       self.Clamp(sourceClolor[2] * 255 / self.maxes[2], 0, 255))
        return resultColor