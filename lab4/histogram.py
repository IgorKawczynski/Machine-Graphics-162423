from matplotlib.pyplot import imshow
from lab3.gray_sepia import *
import numpy as np


class Histogram:
    values: np.ndarray  # przechowuje wartosci histogramu danego obrazu

    def __init__(self, values: np.ndarray) -> None:
        if values.ndim == 2:
            self.values = np.histogram(values, bins=256, range=(0, 255))[0]
        # else:
        #     firstLayer = values[:, :, 0]
        #     secondLayer = values[:, :, 1]
        #     thirdLayer = values[:, :, 2]
        #     firstLayerHistogram = np.histogram(firstLayer, bins=256, range=(0, 255))[0]
        #     secondLayerHistogram = np.histogram(secondLayer, bins=256, range=(0, 255))[0]
        #     thirdLayerHistogram = np.histogram(thirdLayer, bins=256, range=(0, 255))[0]
        #     self.values = np.dstack((firstLayerHistogram, secondLayerHistogram, thirdLayerHistogram))
        # DLA METODY plotRGBInOne()  :
        else:
            self.values = values

    def plot(self) -> None:
        if self.values.ndim == 1:
            matplotlib.pyplot.figure()
            matplotlib.pyplot.title("Gray Scale Histogram")
            matplotlib.pyplot.xlabel("Gray Scale value")
            matplotlib.pyplot.ylabel("Number of pixels")
            matplotlib.pyplot.xlim([0, 255])
            bin_edges = np.linspace(0, 254.9, 256)
            matplotlib.pyplot.plot(bin_edges, self.values, color="gray")
            matplotlib.pyplot.show()
        else:
            matplotlib.pyplot.figure(figsize=(14, 8))
            bin_edges = np.linspace(0, 254.9, 256)
            matplotlib.pyplot.subplot(131)
            matplotlib.pyplot.title("red layer")
            matplotlib.pyplot.xlim([0, 255])
            matplotlib.pyplot.ylabel("Number of pixels")
            matplotlib.pyplot.xlabel("Red Scale value")
            matplotlib.pyplot.plot(bin_edges, self.values[:, :, 0].flatten(), color="red")
            matplotlib.pyplot.subplot(132)
            matplotlib.pyplot.title("green layer")
            matplotlib.pyplot.xlabel("Green Scale value")
            matplotlib.pyplot.xlim([0, 255])
            matplotlib.pyplot.plot(bin_edges, self.values[:, :, 1].flatten(), color="green")
            matplotlib.pyplot.subplot(133)
            matplotlib.pyplot.title("blue layer")
            matplotlib.pyplot.xlabel("Blue Scale value")
            matplotlib.pyplot.xlim([0, 255])
            matplotlib.pyplot.plot(bin_edges, self.values[:, :, 2].flatten(), color="blue")
            matplotlib.pyplot.show()

    def plotRGBInOne(self) -> None:
        matplotlib.pyplot.figure()
        matplotlib.pyplot.title("Layer saturation histogram")
        matplotlib.pyplot.xlim([0, 256])
        matplotlib.pyplot.xlabel("Layer saturation")
        matplotlib.pyplot.ylabel("Number of pixels")
        for layer, color in enumerate(("red", "green", "blue")):
            histogram, binEdges = np.histogram(self.values[:, :, layer], bins=256, range=(0, 256))
            matplotlib.pyplot.plot(binEdges[0: -1], histogram, color=color, label=color + " layer")
            matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

    def plotCumulative(self) -> None:
        if self.values.ndim == 1:
            matplotlib.pyplot.title("Gray Scale Cumulative Histogram")
            matplotlib.pyplot.xlim([0, 255])
            binEdgesC = np.linspace(0, 254.9, 256)
            matplotlib.pyplot.plot(binEdgesC, self.values, color="gray")
            matplotlib.pyplot.show()
        else:
            raise Exception("MUST BE 1 DIMENSIONAL !!!")

    def toCumulative(self) -> 'Histogram':
        self.values = np.cumsum(self.values)
        return self


class ImageDiffMethod(Enum):
    mse = 0
    rmse = 1


class Image(GrayScaleTransform):
    def __init__(self, pixels: Any, colorModel: ColorModel) -> None:
        super().__init__(pixels, colorModel)


class ImageComparison(BaseImage):
    def __init__(self, pixels: Any, colorModel: ColorModel) -> None:
        super().__init__(pixels, colorModel)

    """
    metoda zwracajaca obiekt zawierajacy histogram biezacego obrazu (1- lub wielowarstwowy)
    """
    def histogram(self) -> Histogram:
        return Histogram(self.pixels)

    """
    metoda zwracajaca mse lub rmse dla dwoch obrazow
    """
    def compareTo(self, other: Image, method: ImageDiffMethod) -> float:
        grayImage1 = GrayScaleTransform(self.pixels, colorModel=ColorModel.rgb).fromRgbToGray()
        grayImage2 = GrayScaleTransform(other.pixels, colorModel=ColorModel.rgb).fromRgbToGray()
        grayImage1HistogramValues = Histogram(grayImage1.pixels).values
        grayImage2HistogramValues = Histogram(grayImage2.pixels).values
        # TODO --> do zmiany(?)
        n = len(grayImage1HistogramValues)
        sumHistogram = 0
        for x in range(n):
            sumHistogram = sumHistogram + ((grayImage1HistogramValues[x] - grayImage2HistogramValues[x]) ** 2)
        sumHistogram = np.sum(sumHistogram) * 1/n

        if method == ImageDiffMethod.rmse:
            sumHistogram = np.sqrt(sumHistogram)
        print("Coefficient of Determination {method} = {result}".format(method=method.name.upper(),
                                                                        result=sumHistogram))
        return sumHistogram


# Przykladowy tensor dla obrazu :
# 240 50 30
# 110 180 35
# 10 25 64
#
# min = 10
# max = 240
# dla pierwszej wartosci zrobmy sobie wlasnie wyrównanie (wyrównanie histogramu to wyrownanie wszystkich pikseli w obrazie w skali szarosci)
# f(1, 1) = (f(1, 1) - min) * ( 255 / (max - min) )
# tensor po wyrownaniu histogramu :
# 255 x x    <--- dla x'ow analogicznie robimy jak dla 240...
# x x x
# x x x