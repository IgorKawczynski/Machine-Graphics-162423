from matplotlib.pyplot import imshow
from lab3.gray_sepia import *
import numpy as np


class Histogram:
    values: np.ndarray  # przechowuje wartosci histogramu danego obrazu

    def __init__(self, values: np.ndarray) -> None:
        self.values = values

    """
    metoda wyswietlajaca histogram na podstawie atrybutu values
    """
    def plot(self) -> None:
        if self.values.ndim == 2:
            self.plotGrayScale()
        else:
            self.plotRGBInOne()

    def plotRGB(self) -> None:
        rLayer, gLayer, bLayer = np.squeeze(np.dsplit(self.values, self.values.shape[-1]))
        matplotlib.pyplot.figure()
        matplotlib.pyplot.title("RED LAYER")
        matplotlib.pyplot.xlim([0, 256])
        matplotlib.pyplot.xlabel("Layer saturation")
        matplotlib.pyplot.ylabel("Number of pixels")
        histogramR, binEdgesR = np.histogram(rLayer, bins=256, range=(0, 256))
        matplotlib.pyplot.plot(binEdgesR[0: -1], histogramR, color="red")

        matplotlib.pyplot.figure()
        matplotlib.pyplot.title("GREEN LAYER")
        matplotlib.pyplot.xlim([0, 256])
        matplotlib.pyplot.xlabel("Layer saturation")
        matplotlib.pyplot.ylabel("Number of pixels")
        histogramG, binEdgesG = np.histogram(gLayer, bins=256, range=(0, 256))
        matplotlib.pyplot.plot(binEdgesG[0: -1], histogramG, color="green")

        matplotlib.pyplot.figure()
        matplotlib.pyplot.title("BLUE LAYER")
        matplotlib.pyplot.xlim([0, 256])
        matplotlib.pyplot.xlabel("Layer saturation")
        matplotlib.pyplot.ylabel("Number of pixels")
        histogramB, binEdgesB = np.histogram(bLayer, bins=256, range=(0, 256))
        matplotlib.pyplot.plot(binEdgesB[0: -1], histogramB, color="blue")
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

    def plotGrayScale(self) -> None:
        matplotlib.pyplot.title("Gray Scale Histogram")
        matplotlib.pyplot.xlim([0, 256])
        matplotlib.pyplot.xlabel("Gray Scale Layer saturation")
        matplotlib.pyplot.ylabel("Number of pixels")
        matplotlib.pyplot.ylim([0, 3000])
        histogramG, binEdgesG = np.histogram(self.values, bins=256, range=(0, 256))
        matplotlib.pyplot.plot(binEdgesG[0: -1], histogramG, color="gray")
        matplotlib.pyplot.show()

    """
    metoda zwracajaca histogram skumulowany na podstawie stanu wewnetrznego obiektu
    """
    def to_cumulated(self) -> 'Histogram':

        pass


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
        grayImage1 = GrayScaleTransform(self.pixels, colorModel=ColorModel.rgb)
        grayImage2 = GrayScaleTransform(other.pixels, colorModel=ColorModel.rgb)
        grayImage1HistogramValues = Histogram(grayImage1.pixels).values
        grayImage2HistogramValues = Histogram(grayImage2.pixels).values

        # TODO --> do zmiany
        n = int(len(grayImage1HistogramValues) / 2)
        sumHistogram = 0
        for x in range(n):
            sumHistogram = sumHistogram + ((grayImage1HistogramValues[x] - grayImage2HistogramValues[x]) ** 2)
        sumHistogram = np.sum(sumHistogram) * 1/n

        if method == ImageDiffMethod.rmse:
            sumHistogram = np.sqrt(sumHistogram)
        print("Coefficient of Determination {method} = {result}".format(method=method.name.upper(),
                                                                        result=sumHistogram))
        return sumHistogram

# TODO - poprawic takze histogram w skali szarosci ( a moze cala skale szarosci ? )

# TODO wyznaczamy sobie min i max wartosc pixela wystepujacego na CAAALYM obrazie w SKALI szerosci,
#  f to jest caly obraz, dokonujemy pozniej transformacji takiej jaka jest na wzorze, i we wzorze mamy tak :
#  dla kazdego pixela odejmuje minimalna wartosc piksela na obrazie i mnozymy przez 255 i dzielimy przez max(f) i min(f)

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