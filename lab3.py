from typing import Any
from lab2 import *
import matplotlib
from matplotlib.pyplot import imshow
import numpy as np
from enum import Enum


# ----------------------------------------- LAB 3 ------------------------------------------


class GrayScaleTransform(BaseImage):
    def __init__(self, pixels: Any, colorModel: ColorModel) -> None:
        super().__init__(pixels, colorModel)

    " metoda zwracajaca obraz w skali szarosci jako obiekt klasy BaseImage "
    def fromRgbToGray(self) -> BaseImage:
        redLayer, greenLayer, blueLayer = np.squeeze(np.dsplit(self.pixels, self.pixels.shape[-1]))
        R, G, B = self.getLayers() / 255
        g = (redLayer + greenLayer + blueLayer) / 3
        print("    R   G   B")
        print(self.pixels)
        self.pixels = g
        print("    G")
        print(self.pixels)
        self.colorModel = ColorModel.gray
        return self

    """ metoda zwracajaca obraz w sepii jako obiekt klasy BaseImage
    sepia tworzona metoda 1 w przypadku przekazania argumentu alpha_beta
    lub metoda 2 w przypadku przekazania argumentu 'w' """
    def to_sepia(self, alpha_beta: tuple = (None, None), w: int = None) -> BaseImage:
        pass

    def showGrayConversions(self) -> None:
        figure, axis = matplotlib.pyplot.subplots(1, 2)
        axis[0].imshow(self.pixels)
        axis[0].set_title("RGB")
        self.fromRgbToGray()
        axis[1].imshow(self.pixels)
        axis[1].set_title("RGB -> GRAY")
        figure.set_figwidth(12)
        figure.set_figheight(4)
        matplotlib.pyplot.show()


    "metoda wyświetlająca warstwę o wskazanym indeksie dla obrazu w szarości"
    def showGrayLayer(self, layer_id: int) -> None:
        layer = self.pixels[:, layer_id]
        imshow(layer)
        matplotlib.pyplot.show()



    """ klasa stanowiaca glowny interfejs biblioteki
    w pozniejszym czasie bedzie dziedziczyla po kolejnych klasach
    realizujacych kolejne metody przetwarzania obrazow """
# class Image(GrayScaleTransform):
#
#     def __init__(self, ...) -> None:
#         pass



    """ DO SAMEJ WARTOŚCI MUSISZ UŻYWAĆ UINT16, DO RESZTY MOZE BYC INT8, BO BEDA ARTEFAKTY """
    " FILTROWANIE DANYCH JESLI PIKSEL MA WARTOSC WIEKSZA NIZ 255, arr[arr > 255] = 255"


# # # --------------------- GRAY ----------------------
image1 = GrayScaleTransform('C:/Users/kompp3/Desktop/lena.jpg', ColorModel.rgb)
image1.fromRgbToGray()
# image1.showGrayLayer(0)
# image1.showGrayLayer(1)
