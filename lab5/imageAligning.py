import matplotlib
import numpy as np
from matplotlib.pyplot import imshow

from lab2.basic_image import BaseImage, ColorModel
from lab4.histogram import Histogram


class ImageAligning(BaseImage):

    def __init__(self, baseImage) -> None:
        super().__init__(baseImage.pixels, baseImage.colorModel)

    def alignImage(self, tailElimination: bool = True) -> 'BaseImage':

        def alignWithoutTailElimination(layer: np.ndarray) -> np.ndarray:
            minPixel = np.min(layer)
            maxPixel = np.max(layer)
            minus = maxPixel - minPixel
            aligned = np.multiply(np.subtract(layer, minPixel), 255 / minus)
            return aligned.astype('i')

        def alignWithTailElimination(layer: np.ndarray) -> np.ndarray:
            cumulativeValues = Histogram(layer).toCumulative().values
            cumulativeRange = cumulativeValues[-1]
            minValue = 0
            maxValue = 0
            cumulativeSum = 0
            for x in cumulativeValues:
                if cumulativeSum <= 0.05 * cumulativeRange:
                    minValue = minValue + 1
                if cumulativeSum <= 0.95 * cumulativeRange:
                    maxValue = maxValue + 1
                    cumulativeSum = x
            layerCopy = np.float64(np.copy(layer))
            alignment = np.divide(255, (maxValue - minValue))
            layerReturned = ((layerCopy - minValue) * alignment).astype('i')
            layerReturned[layerReturned > 255] = 255
            layerReturned[layerReturned < 0] = 0
            return layerReturned
        if tailElimination is False:
            if self.pixels.ndim == 2:
                grayLayer = alignWithoutTailElimination(self.pixels)
                return BaseImage(grayLayer, self.colorModel)
            else:
                firstLayer, secondLayer, thirdLayer = self.getLayers()
                firstLayer = alignWithoutTailElimination(firstLayer)
                secondLayer = alignWithoutTailElimination(secondLayer)
                thirdLayer = alignWithoutTailElimination(thirdLayer)
                alignedLayers = np.dstack((firstLayer, secondLayer, thirdLayer))
                return BaseImage(alignedLayers, ColorModel.rgb)
        else:
            if self.pixels.ndim == 2:  # lub 1-dim
                grayLayer = alignWithTailElimination(self.pixels)
                return BaseImage(grayLayer, ColorModel.rgb)
            else:
                firstLayer, secondLayer, thirdLayer = self.getLayers()
                firstLayer = alignWithTailElimination(firstLayer)
                secondLayer = alignWithTailElimination(secondLayer)
                thirdLayer = alignWithTailElimination(thirdLayer)
                alignedLayers = np.dstack((firstLayer, secondLayer, thirdLayer))
                return BaseImage(alignedLayers, ColorModel.rgb)

    def compareStandardToAligned(self):
        if self.pixels.ndim == 2:
            figure, axis = matplotlib.pyplot.subplots(1, 3)
            axis[0].imshow(self.pixels, cmap='gray')
            axis[0].set_title("Standard GrayScale")
            lenaAlignWithoutTailElimination = self.alignImage(tailElimination=False)
            axis[1].imshow(lenaAlignWithoutTailElimination.pixels, cmap='gray')
            axis[1].set_title("Aligned GrayScale without tail elimination")
            lenaAlignWithTailElimination = self.alignImage(tailElimination=True)
            axis[2].imshow(lenaAlignWithTailElimination.pixels, cmap='gray')
            axis[2].set_title("Aligned GrayScale with tail elimination")
            figure.set_figwidth(14)
            figure.set_figheight(6)
            matplotlib.pyplot.show()
        else:
            figure, axis = matplotlib.pyplot.subplots(1, 3)
            axis[0].imshow(self.pixels)
            axis[0].set_title("Standard RGB")
            lenaAlignWithoutTailElimination = self.alignImage(tailElimination=False)
            axis[1].imshow(lenaAlignWithoutTailElimination.pixels)
            axis[1].set_title("Aligned RGB without tail elimination")
            lenaAlignWithTailElimination = self.alignImage(tailElimination=True)
            axis[2].imshow(lenaAlignWithTailElimination.pixels)
            axis[2].set_title("Aligned RGB with tail elimination")
            figure.set_figwidth(14)
            figure.set_figheight(6)
            matplotlib.pyplot.show()
