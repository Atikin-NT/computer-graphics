from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from progress.bar import IncrementalBar
import time

def procImg(img, func):
    width = len(img)
    height = len(img[0])
    res = img

    bar = IncrementalBar('Image processing', max = width)
    for i in range(width):
        for j in range(height):
            res[i][j] = func(img, i, j)
        bar.next()
    bar.finish()
    
    return res

def negative(img, x, y):
    return [255 - img[x][y][0], 255 -img[x][y][1], 255 -img[x][y][2]]

def clamp(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def blur(img, x, y, kernel):
    width = len(img)
    height = len(img[0])
    radx = len(kernel) // 2
    rady = len(kernel[0]) // 2
    rgb = [0, 0, 0]
    for l in range(-rady, rady + 1):
        for k in range(-radx, radx + 1):
            nbx = clamp(x + k, 0, width - 1)
            nby = clamp(y + l, 0, height - 1)
            nbweight = kernel[l + rady][k + radx]
            rgb[0] += img[nbx][nby][0] * nbweight
            rgb[1] += img[nbx][nby][1] * nbweight
            rgb[2] += img[nbx][nby][2] * nbweight
    return [clamp(int(a), 0, 255) for a in rgb]

def def_kern(radius = 3):
    return [[1/(radius * radius) for i in range(radius)] for i in range(radius)]

def gauss_kern(radius = 3, sigma = 1.0):
    size = 2 * radius + 1
    gauss_kernel = np.zeros((size, size)) 
    norm = .0
    for i in range(-radius, radius + 1): 
        for j in range(-radius, radius + 1): 
            gauss_kernel[i + radius, j + radius] = np.exp(-((i**2 + j**2) / (sigma**2)))
            norm += gauss_kernel[i + radius, j + radius]
    for i in range(size): 
        for j in range(size): 
            gauss_kernel[i, j] = gauss_kernel[i, j] / norm
    return gauss_kernel

def intensity(rgb):
    return rgb.dot([1/3,1/3,1/3])

def gistogram(img):
    pixels = np.array(np.zeros((256)))
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixels[int(intensity(img[x][y]))] += 1

    pixels = pixels/(len(img) * len(img[0]))
    plt.bar(range(len(pixels)), pixels)
    plt.show()

def light_avg(img):
    rgb = np.array([0,0,0])
    for x in range(len(img)):
        for y in range(len(img[0])):
            rgb += img[x][y]
    return intensity(rgb) / (len(img) * len(img[0]))

def contrast(img, x, y, avg, c = 1.35):
    rgb = [0, 0, 0]
    rgb[0] = avg + (img[x][y][0] - avg) * c
    rgb[1] = avg + (img[x][y][1] - avg) * c
    rgb[2] = avg + (img[x][y][2] - avg) * c
    return [clamp(int(a), 0, 255) for a in rgb]

if __name__ == "__main__":
    img = io.imread("data/pepe.jpg")

    start = time.time()
    avg = light_avg(img)
    end = time.time()
    print(end - start)

    start = time.time()
    img = procImg(img, lambda img, i, j: contrast(img, i, j, avg))
    end = time.time()
    print(end - start)


    plt.imshow(img)
    plt.show()

    