import numpy as np
import matplotlib.pyplot as plt

class Gistogramm:
    def __init__(self, img: np.ndarray):
        self.img = img
        # print(img.shape)
        width, height, _ = img.shape

        brightness = np.zeros(255 + 1)
        for i in range(width):
            for j in range(height):
                pixel = img[i][j]
                ind = int(pixel[0] * 1/3 + pixel[1] * 1/3 + pixel[2] * 1/3)
                brightness[ind] += 1

        self.listBrightness = brightness

        minBrightness = width * height
        ind = 0
        for i in range(255 + 1):
            if self.listBrightness[i] < minBrightness and self.listBrightness[i] != 0:
                ind = i
                minBrightness = self.listBrightness[i]
        self.minBrightness = ind

        ind = 0
        for i in range(255 + 1):
            # print(i)
            if self.listBrightness[i] > self.listBrightness[ind]:
                ind = i

        self.maxBrightness = ind
        print(self.listBrightness[self.maxBrightness], self.maxBrightness)

        self.show()

        # print(self.minBrightness)
        # print(self.maxBrightness)
    def show(self):
        plt.plot(self.listBrightness)
        plt.show()

    def getBrightnessList(self):
        return self.listBrightness

    def getMinBrightness(self):
        return self.minBrightness

    def getMaxBrightness(self):
        return self.maxBrightness