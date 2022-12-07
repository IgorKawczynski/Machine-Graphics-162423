import matplotlib
import numpy as np
from matplotlib.pyplot import imshow

from lab2.basic_image import BaseImage, ColorModel, PATH
from lab3.gray_sepia import GrayScaleTransform


class ImageAligning(BaseImage):

    def __init__(self, baseImage) -> None:
        super().__init__(baseImage.pixels, baseImage.colorModel)

    def alignImage(self, tail_elimination: bool = True) -> 'BaseImage':
        self.pixels = np.where(self.pixels >= 0.0,
                               (self.pixels - np.min(self.pixels)) * (
                                       255 / (np.max(self.pixels) - np.min(self.pixels))),
                               0.0)
        self.pixels = np.where(self.pixels > 255, 255, self.pixels)
        self.colorModel = ColorModel.gray
        return self

    def compareStandardToAligned(self):
        figure, axis = matplotlib.pyplot.subplots(1, 2)
        axis[0].imshow(self.pixels, cmap='gray')
        axis[0].set_title("Standard GrayScale")
        self.alignImage()
        axis[1].imshow(self.pixels, cmap='gray')
        axis[1].set_title("Aligned GrayScale")
        figure.set_figwidth(12)
        figure.set_figheight(4)
        matplotlib.pyplot.show()


#  TODO -> ulozyc schemat ładnie, imageAlign clasa zeby miala metody do skali szarosci i rob dalej lab5

# lenaGray = GrayScaleTransform(PATH, colorModel=ColorModel.rgb)
# lenaGray.fromRgbToGray()
#
# imshow(lenaGray.pixels, cmap='gray')
# matplotlib.pyplot.show()
#
# img1 = ImageAligning(lenaGray)
# img1.alignImage()
#
# imshow(img1.pixels, cmap='gray')
# matplotlib.pyplot.show()
#
# img1.compareStandardToAligned()




