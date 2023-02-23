import numpy as np
import matplotlib.pyplot as plt

class Gistogramm:
    def __init__(self, img: np.ndarray):
        self.img = img
        # print(img.shape)
        width, height, _ = img.shape

        brightness = np.zeros(255)
        for i in range(width):
            for j in range(height):
                pixel = img[i][j]
                ind = int(pixel[0] * 1/3 + pixel[1] * 1/3 + pixel[2] * 1/3)
                brightness[ind] = int(brightness[ind] + 1)

        self.listBrightness = brightness

        width, height, _ = self.img.shape
        minBrightness = width * height
        for i in self.listBrightness:
            if i < minBrightness and i != 0:
                minBrightness = i
        self.minBrightness = minBrightness

        maxBrightness = 0
        for i in self.listBrightness:
            if i > maxBrightness:
                maxBrightness = i

        self.maxBrightness = maxBrightness

        self.show()
    def show(self):
        plt.plot(self.listBrightness)
        plt.show()

    def getBrightnessList(self):
        return self.listBrightness

    def getMinBrightness(self):
        return self.minBrightness

    def getMaxBrightness(self):
        return self.maxBrightness