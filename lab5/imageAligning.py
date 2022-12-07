import matplotlib
import numpy as np
from matplotlib.pyplot import imshow

from lab2.basic_image import BaseImage, ColorModel


class ImageAligning(BaseImage):

    def __init__(self, baseImage) -> None:
        super().__init__(baseImage.pixels, baseImage.colorModel)

    def align(self, layer: np.ndarray) -> np.ndarray:
        minPixel = np.min(layer)
        maxPixel = np.max(layer)
        minus = maxPixel - minPixel
        aligned = np.multiply(np.subtract(layer, minPixel), 255 / minus)
        return aligned.astype('uint8')

    def alignImage(self, tailElimination: bool = True) -> 'BaseImage':
        if tailElimination is False:
            if self.pixels.ndim == 2:
                self.align(self.pixels)
                return BaseImage(self.pixels, ColorModel.gray)
            else:
                firstLayer, secondLayer, thirdLayer = self.getLayers()
                firstLayer = self.align(firstLayer)
                secondLayer = self.align(secondLayer)
                thirdLayer = self.align(thirdLayer)
                alignedLayers = np.dstack((firstLayer, secondLayer, thirdLayer))
                return BaseImage(alignedLayers, ColorModel.rgb)
        else:
            pass

    def compareStandardToAligned(self, tailElimination: bool = True):

        if self.pixels.ndim == 2:
            figure, axis = matplotlib.pyplot.subplots(1, 2)
            axis[0].imshow(self.pixels, cmap='gray')
            axis[0].set_title("Standard GrayScale")
            lenaAlign = self.alignImage(tailElimination)
            axis[1].imshow(lenaAlign.pixels, cmap='gray')
            axis[1].set_title("Aligned GrayScale")
            figure.set_figwidth(12)
            figure.set_figheight(4)
            matplotlib.pyplot.show()
        else:
            figure, axis = matplotlib.pyplot.subplots(1, 2)
            axis[0].imshow(self.pixels)
            axis[0].set_title("Standard RGB")
            lenaAlign = self.alignImage(tailElimination)
            axis[1].imshow(lenaAlign.pixels)
            axis[1].set_title("Aligned RGB")
            figure.set_figwidth(12)
            figure.set_figheight(4)
            matplotlib.pyplot.show()
