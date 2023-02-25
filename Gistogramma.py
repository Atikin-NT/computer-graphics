import numpy as np
import matplotlib.pyplot as plt

class Gistogramm:
    def __init__(self, data: np.ndarray):
        # print(data.shape)
        if len(data.shape) == 3:
            self.img = data
            width, height, _ = data.shape

            brightness = np.zeros(256)
            for i in range(width):
                for j in range(height):
                    pixel = data[i][j]
                    ind = int(pixel[0] * 1/3 + pixel[1] * 1/3 + pixel[2] * 1/3)
                    brightness[ind] += 1

            self.listBrightness = brightness
        else:
            self.listBrightness = data

        # -------------------------------------------------------------------

        ind = 0
        for i in range(255 + 1):
            # print(self.listBrightness[i])
            if self.listBrightness[i] > self.listBrightness[ind]:
                ind = i

        self.maxBrightness = ind

        # -------------------------------------------------------------------

        ind = 0
        minBrightness = self.listBrightness[self.maxBrightness]
        for i in range(255 + 1):
            if self.listBrightness[i] < minBrightness and self.listBrightness[i] != 0:
                ind = i
                minBrightness = self.listBrightness[i]
        self.minBrightness = ind

        # print(self.listBrightness[self.maxBrightness], self.maxBrightness)
        # length = type(self.listBrightness)
        # print(length)

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