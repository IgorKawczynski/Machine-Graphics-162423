from typing import Any
import matplotlib
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from matplotlib.image import imsave
import numpy as np
from enum import Enum

PATH = 'C://Users/kompp3/Desktop/lena.jpg'
PATH2 = 'C://Users/kompp3/Desktop/nieLena.jpg'

# ------------------------------------------------------------------------------------------------------------


class ColorModel(Enum):
    rgb = 0
    hsv = 1
    hsi = 2
    hsl = 3
    gray = 4  # obraz 2d
    sepia = 5  # 3d


class BaseImage:
    pixels: np.ndarray  # tensor przechowujacy piksele obrazu
    colorModel: ColorModel  # atrybut przechowujacy biezacy model barw obrazu

    "inicjalizator wczytujacy obraz do atrybutu data na podstawie sciezki - wtedy zczytujemy piksele ze sciezki(imread)"
    "ewentualnie na podstawie tablicy pikseli, wtedy po prostu przepisujemy wartości"
    def __init__(self, pixels: Any, colorModel: ColorModel) -> None:
        if isinstance(pixels, str):
            self.pixels = imread(pixels)
        else:
            self.pixels = pixels
        self.colorModel = colorModel

    "metoda zapisujaca obraz znajdujacy sie w atrybucie data do pliku"
    def saveImg(self, path: str) -> None:
        imsave(path, self.pixels)

    "metoda wyswietlajaca obraz znajdujacy sie w atrybucie data"
    def showImg(self) -> None:
        imshow(self.pixels)
        matplotlib.pyplot.show()

    "metoda zwracająca warstwe jako tensor o wskazanym indeksie"
    def getLayer(self, layer_id: int) -> 'np.ndarray':
        return self.pixels[:, :, layer_id]

    "metoda zwracajaca warstwy z obrazu"
    def getLayers(self) -> []:
        return np.squeeze(np.dsplit(self.pixels, self.pixels.shape[-1]))

    "metoda zwracająca kształt obrazu"
    def getShape(self) -> '[]':
        return self.pixels.shape

    "metoda zwracająca tensor pikseli obrazu"
    def getArray(self) -> '[]':
        return self.pixels

    "metoda wyświetlająca warstwę o wskazanym indeksie"
    def showLayer(self, layer_id: int) -> None:
        layer = self.pixels[:, :, layer_id]
        imshow(layer)
        matplotlib.pyplot.show()

    "metoda wyswietlajaca obraz RGB dzieląc go na 3 warstwy R | G | B"
    def showAsRgbLayers(self) -> None:
        redLayer, greenLayer, blueLayer = np.squeeze(np.dsplit(self.pixels, self.pixels.shape[-1]))
        fun, axisArr = matplotlib.pyplot.subplots(1, 3)
        axisArr[0].imshow(redLayer, cmap='gray')
        axisArr[1].imshow(greenLayer, cmap='gray')
        axisArr[2].imshow(blueLayer, cmap='gray')
        matplotlib.pyplot.show()

    def showHsvConversions(self) -> None:
        figure, axis = matplotlib.pyplot.subplots(1, 3)
        axis[0].imshow(self.pixels)
        axis[0].set_title("RGB")
        self.fromRgbToHsv()
        axis[1].imshow(self.pixels)
        axis[1].set_title("RGB -> HSV")
        self.fromHsvToRgb()
        axis[2].imshow(self.pixels)
        axis[2].set_title("HSV -> RGB")
        figure.set_figwidth(12)
        figure.set_figheight(4)
        matplotlib.pyplot.show()

    def showHsiConversions(self) -> None:
        figure, axis = matplotlib.pyplot.subplots(1, 3)
        axis[0].imshow(self.pixels)
        axis[0].set_title("RGB")
        self.fromRgbToHsi()
        axis[1].imshow(self.pixels)
        axis[1].set_title("RGB -> HSI")
        self.fromHsiToRgb()
        axis[2].imshow(self.pixels)
        axis[2].set_title("HSI -> RGB")
        figure.set_figwidth(12)
        figure.set_figheight(4)
        matplotlib.pyplot.show()

    def showHslConversions(self) -> None:
        figure, axis = matplotlib.pyplot.subplots(1, 3)
        axis[0].imshow(self.pixels)
        axis[0].set_title("RGB")
        self.fromRgbToHsl()
        axis[1].imshow(self.pixels)
        axis[1].set_title("RGB -> HSL")
        self.fromHslToRgb()
        axis[2].imshow(self.pixels)
        axis[2].set_title("HSL -> RGB")
        figure.set_figwidth(12)
        figure.set_figheight(4)
        matplotlib.pyplot.show()

    "metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsv"
    "metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw"
    def fromRgbToHsv(self) -> 'BaseImage':

        R, G, B = self.getLayers() / 255
        M = np.max([R, G, B], axis=0)
        m = np.min([R, G, B], axis=0)
        V = M / 255

        S = np.where(M > 0, 1 - (m / M), 0)

        H = np.where(G >= B,
                     np.cos((R - (G / 2.0) - (B / 2.0)) /
                            np.sqrt(np.power(R, 2.0) + np.power(G, 2.0), np.power(B, 2.0)
                                    - np.multiply(R, G) - np.multiply(R, B) - np.multiply(G, B))
                            ) ** (-1),
                     360 - np.cos((R - (G / 2.0) - (B / 2.0)) /
                                  np.sqrt(np.power(R, 2.0) + np.power(G, 2.0), np.power(B, 2.0)
                                          - np.multiply(R, G) - np.multiply(R, B) - np.multiply(G, B))
                                  ) ** (-1),
                     )

        self.pixels = np.dstack((H, S, V))
        self.colorModel = ColorModel.hsv
        return self

    def fromHsvToRgb(self) -> 'BaseImage':

        if self.colorModel != ColorModel.hsv:
            raise TypeError("This method is only eligible to HSV schema color!")

        H, S, V = self.getLayers()
        M = 255 * V
        m = M * (1 - S)
        z = (M - m) * (1 - np.absolute(((H / 60) % 2) - 1))

        R = np.where(H < 60, M,
            np.where(H < 120, z + m,
            np.where(H < 240, m,
            np.where(H < 300, z + m, M))))

        G = np.where(H < 60, z + m,
            np.where(H < 240, M, m))

        B = np.where(H < 120, m,
            np.where(H < 240, z + m,
            np.where(H < 300, M, z + m)))

        self.pixels = np.dstack((R, G, B))
        self.colorModel = ColorModel.rgb
        return self

    "metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsi metoda"
    "zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw"

    def fromRgbToHsi(self) -> 'BaseImage':

        R, G, B = self.getLayers() / 255
        M = np.max([R, G, B], axis=0)
        m = np.min([R, G, B], axis=0)
        I = (R + G + B) / 3
        S = np.where(M > 0, 1 - (m / M), 0)

        H = np.where(G >= B,
                     np.cos((R - (G / 2.0) - (B / 2.0)) /
                            np.sqrt(np.power(R, 2.0) + np.power(G, 2.0), np.power(B, 2.0)
                                    - np.multiply(R, G) - np.multiply(R, B) - np.multiply(G, B))
                            ) ** (-1),
                     360 - (np.cos((R - (G / 2.0) - (B / 2.0)) /
                                  np.sqrt(np.power(R, 2.0) + np.power(G, 2.0), np.power(B, 2.0)
                                          - np.multiply(R, G) - np.multiply(R, B) - np.multiply(G, B))
                                  )) ** (-1),
                     )

        self.pixels = np.dstack((H, S, I))
        self.colorModel = ColorModel.hsi
        return self

    def fromHsiToRgb(self) -> 'BaseImage':

        if self.colorModel != ColorModel.hsi:
            raise TypeError("This method is only eligible to HSI schema color!")

        for layer in self.pixels:
            for pixel in layer:
                H, S, I = pixel[0], pixel[1], pixel[2]
                S = S * 0.5
                if 0 <= H <= 120:
                    pixel[2] = I * (1 - S)
                    pixel[0] = I * (1 + (S * np.cos(np.radians(H)) / np.cos(np.radians(60) - np.radians(H))))
                    pixel[1] = I * 3 - (pixel[0] + pixel[2])
                elif 120 < H <= 240:
                    H = H - 120
                    pixel[0] = I * (1 - S)
                    pixel[1] = I * (1 + (S * np.cos(np.radians(H)) / np.cos(np.radians(60) - np.radians(H))))
                    pixel[2] = 3 * I - (pixel[0] + pixel[1])
                elif 0 < H <= 360:
                    H = H - 240
                    pixel[1] = I * (1 - S)
                    pixel[2] = I * (1 + (S * np.cos(np.radians(H)) / np.cos(np.radians(60) - np.radians(H))))
                    pixel[0] = I * 3 - (pixel[1] + pixel[2])

        # ALGORYTM PROSTO Z LABORATORIUM
        # R = np.where(H == 0, I + (2 * I * S),
        #     np.where(H < 120, I + (I * S) * (np.cos(H) / np.cos(60 - H)),
        #     np.where(H <= 240, I - (I * S), I + (I * S) * (1 - np.cos(H - 240) / np.cos(300 - H)))))
        #
        # G = np.where(H == 0, I - (I * S),
        #     np.where(H < 120, I + (I * S) * (1 - (np.cos(H) / np.cos(60 - H))),
        #     np.where(H == 120, I + (2 * I * S),
        #     np.where(H < 240, I + (I * S) * (np.cos(H - 180) / np.cos(180 - H)), I - (I * S)))))
        #
        # B = np.where(H <= 120, I - (I * S),
        #     np.where(H < 240, I + (I * S) * (1 - (np.cos(H - 120) / np.cos(180 - H))),
        #     np.where(H == 240, I + (2 * I * S), I + (I * S) * (np.cos(H - 240) / np.cos(300 - H)))))

        # self.__pixels = np.dstack((pixel[2], pixel[1], pixel[0]))
        self.colorModel = ColorModel.rgb
        return self

    "metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsl, metoda"
    "zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw"

    def fromRgbToHsl(self) -> 'BaseImage':

        R, G, B = self.getLayers() / 255
        M = np.max([R, G, B], axis=0)
        m = np.min([R, G, B], axis=0)
        d = (M - m) / 255
        L = ((M + m) / 2) / 255
        S = np.where(L > 0, (1 * d) / (1 - np.absolute((2 * L) - 1)), 0)

        H = np.where(G >= B,
                     np.cos((R - (G / 2.0) - (B / 2.0)) /
                            np.sqrt(np.power(R, 2.0) + np.power(G, 2.0), np.power(B, 2.0)
                                    - np.multiply(R, G) - np.multiply(R, B) - np.multiply(G, B))
                            ) ** (-1),
                     360 - np.cos((R - (G / 2.0) - (B / 2.0)) /
                                  np.sqrt(np.power(R, 2.0) + np.power(G, 2.0), np.power(B, 2.0)
                                          - np.multiply(R, G) - np.multiply(R, B) - np.multiply(G, B))
                                  ) ** (-1),
                     )

        self.pixels = np.dstack((H, S, L))
        self.colorModel = ColorModel.hsl
        return self

    def fromHslToRgb(self) -> 'BaseImage':

        if self.colorModel != ColorModel.hsl:
            raise TypeError("This method is only eligible to HSL schema color!")

        H, S, L = self.getLayers()
        d = S * (1 - np.absolute((2 * L) - 1))
        m = 255 * (L - (d / 2))
        x = d * (1 - np.absolute(((H / 60) % 2) - 1))

        R = np.where(H < 60, (255 * d) + m,
            np.where(H < 120, (255 * x) + m,
            np.where(H < 240, m,
            np.where(H < 300, (255 * x) + m, (255 * d) + m))))

        G = np.where(H < 60, (255 * x) + m,
            np.where(H < 180, (255 * d) + m,
            np.where(H < 240, (255 * x) + m, m)))

        B = np.where(H < 120, m,
            np.where(H < 180, (255 * x) + m,
            np.where(H < 300, (255 * d) + m, (255 * x) + m)))

        self.pixels = np.dstack((R, G, B))
        self.colorModel = ColorModel.rgb
        return self

    "metoda dokonujaca konwersji obrazu w atrybucie data do modelu rgb "
    "metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw"

    def toRgb(self) -> 'BaseImage':
        if self.colorModel == ColorModel.hsv:
            return self.fromHsvToRgb()
        elif self.colorModel == ColorModel.hsi:
            return self.fromHsiToRgb()
        elif self.colorModel == ColorModel.hsl:
            return self.fromHslToRgb()
        else:
            raise TypeError("This method is only eligible to HSV, HSI, HSL schema colors!")
