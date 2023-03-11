from index import *
from skimage import io
import matplotlib.pyplot as plt


def main():
    img = io.imread("data/img1.jpg")

    # Тиснение ----------------------
    #res = GrayWorld(img).processImage(img)
    #res = EmbossingKernel().processImage(res)

    # Светящиеся края --------------------
    res = MedianFilterMax().processImage(img)
    res = SobelFilter().processImage(res)
    res = MaximumFilter().processImage(res)
    # res = SobelFilter().processImage(res)

    plt.imshow(res)
    plt.show()


def test():
    img = io.imread("data/Lenna600.png")
    testBlur(img)
    testContour(img)
    testDot(img)
    testGeometry(img)
    testHypotheses(img)
    testOthers(img)


def testBlur(img):
    try:
        BoxBlur().processImage(img)
        GaussianFilter().processImage(img)
        SharpenFilter().processImage(img)
        SharpenFilter2().processImage(img)
        SharpenFilter3().processImage(img)
        MotionFilter().processImage(img)
        EdgeDetection().processImage(img)
    except Exception as e:
        print("BLUR", e)


def testContour(img):
    try:
        EdgeDetection2().processImage(img)
        SobelFilter().processImage(img)
        SharraFilter().processImage(img)
        PrivetaFilter().processImage(img)
    except Exception as e:
        print("CONTOUR", e)


def testDot(img):
    try:
        InvertFilter().processImage(img)
        GrayScaleFilter().processImage(img)
        Sepia().processImage(img)
        LightCorrection().processImage(img)
    except Exception as e:
        print("DOT", e)


def testGeometry(img):
    try:
        WavesFilter().processImage(img)
        GlassFilter().processImage(img)
    except Exception as e:
        print("GEOM", e)


def testHypotheses(img):
    try:
        ContrastFilter(img).processImage(img)
        GrayWorld(img).processImage(img)
        RefColorCor(img, [250, 150], [173, 204, 194]).processImage(img)
        PerfectReflector(img).processImage(img)
    except Exception as e:
        print("HYPO", e)


def testOthers(img):
    try:
        Transfer(50, 70).processImage(img)
        Turn(50, 50, 50).processImage(img)
    except Exception as e:
        print("OTH", e)


if __name__ == "__main__":
    main()
