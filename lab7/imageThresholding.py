from lab2.basic_image import *
from lab3.gray_sepia import *
from lab4.histogram import Histogram


class Thresholding(BaseImage):

    def __init__(self, baseImage) -> None:
        super().__init__(baseImage.pixels, baseImage.colorModel)

    """
    metoda dokonujaca operacji segmentacji za pomoca binaryzacji
    """
    def threshold(self, value: int) -> BaseImage:
        if self.pixels.ndim == 2:
            self.pixels = np.where(self.pixels < value, 0, 255)
            self.colorModel = ColorModel.gray
            return self
        if self.pixels.ndim == 3:
            grayImage = GrayScaleTransform(self.pixels, ColorModel.rgb)
            grayImage.fromRgbToGray()
            grayImage.pixels = np.where(grayImage.pixels < value, 0, 255)
            self.pixels = grayImage.pixels
            return self
        else:
            raise Exception("Obraz musi być konwertowalny do skali szarości !!")

    def showThresholded(self, value: int) -> None:
        figure, axis = matplotlib.pyplot.subplots(1, 2)
        grayImage = GrayScaleTransform(self.pixels, ColorModel.rgb)
        grayImage.fromRgbToGray()
        axis[0].imshow(grayImage.pixels, cmap='gray')
        axis[0].set_title("Standard GrayScale")
        p = Thresholding(self)
        p.threshold(value)
        axis[1].imshow(p.pixels, cmap='gray')
        axis[1].set_title("p = {result}".format(result=value))
        figure.set_figwidth(16)
        figure.set_figheight(4)
        matplotlib.pyplot.show()

    def showAllThresholded(self) -> None:
        figure, axis = matplotlib.pyplot.subplots(1, 6)
        grayImage = GrayScaleTransform(self.pixels, ColorModel.rgb)
        grayImage.fromRgbToGray()
        axis[0].imshow(grayImage.pixels, cmap='gray')
        axis[0].set_title("Standard GrayScale")
        p30 = Thresholding(self)
        p30.threshold(30)
        axis[1].imshow(p30.pixels, cmap='gray')
        axis[1].set_title("p = 30")
        p70 = Thresholding(self)
        p70.threshold(70)
        axis[2].imshow(p70.pixels, cmap='gray')
        axis[2].set_title("p = 70")
        p127 = Thresholding(self)
        p127.threshold(127)
        axis[3].imshow(p127.pixels, cmap='gray')
        axis[3].set_title("p = 127")
        p170 = Thresholding(self)
        p170.threshold(170)
        axis[4].imshow(p170.pixels, cmap='gray')
        axis[4].set_title("p = 170")
        p220 = Thresholding(self)
        p220.threshold(220)
        axis[5].imshow(p220.pixels, cmap='gray')
        axis[5].set_title("p = 220")
        figure.set_figwidth(16)
        figure.set_figheight(3)
        matplotlib.pyplot.show()

    def showAllThresholdedWithHistograms(self) -> None:
        figure, axis = matplotlib.pyplot.subplots(2, 6)
        grayImage = GrayScaleTransform(self.pixels, ColorModel.rgb)
        grayImage.fromRgbToGray()
        axis[0, 0].imshow(grayImage.pixels, cmap='gray')
        axis[0, 0].set_title("Standard GrayScale")
        p30 = Thresholding(self)
        p30.threshold(30)
        axis[0, 1].imshow(p30.pixels, cmap='gray')
        axis[0, 1].set_title("p = 30")
        p70 = Thresholding(self)
        p70.threshold(70)
        axis[0, 2].imshow(p70.pixels, cmap='gray')
        axis[0, 2].set_title("p = 70")
        p127 = Thresholding(self)
        p127.threshold(127)
        axis[0, 3].imshow(p127.pixels, cmap='gray')
        axis[0, 3].set_title("p = 127")
        p170 = Thresholding(self)
        p170.threshold(170)
        axis[0, 4].imshow(p170.pixels, cmap='gray')
        axis[0, 4].set_title("p = 170")
        p220 = Thresholding(self)
        p220.threshold(220)
        axis[0, 5].imshow(p220.pixels, cmap='gray')
        axis[0, 5].set_title("p = 220")
        p30Histogram = Histogram(p30.pixels)
        p30Histogram.plot()
        axis[1, 0].p30Histogram.plot()  # INACZEJ
        axis[1, 0].set_title("p = 220")
        figure.set_figwidth(16)
        figure.set_figheight(3)
        matplotlib.pyplot.show()

        #   TODO dokoncz histogramy pod obrazkami i sprawdz ndim == 1 i ndim == 2
