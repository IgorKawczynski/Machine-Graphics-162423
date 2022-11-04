from lab2.basic_image import *
import matplotlib
from matplotlib.pyplot import imshow
import numpy as np


# ----------------------------------------- LAB 3 ------------------------------------------

class GrayScaleTransform(BaseImage):
    def __init__(self, pixels: Any, colorModel: ColorModel) -> None:
        super().__init__(pixels, colorModel)

    " metoda zwracajaca obraz w skali szarosci jako obiekt klasy BaseImage "

    def fromRgbToGray(self) -> BaseImage:
        R, G, B = self.getLayers()

        averageR = R * 0.299
        averageG = G * 0.587
        averageB = B * 0.114

        self.pixels = averageR + averageG + averageB
        self.colorModel = ColorModel.gray
        return self

    def showGrayConversions(self) -> None:
        figure, axis = matplotlib.pyplot.subplots(1, 2)
        axis[0].imshow(self.pixels)
        axis[0].set_title("RGB")
        self.fromRgbToGray()
        axis[1].imshow(self.pixels, cmap='gray')
        axis[1].set_title("RGB -> GRAY")
        figure.set_figwidth(12)
        figure.set_figheight(4)
        matplotlib.pyplot.show()

    "metoda wyświetlająca warstwę o wskazanym indeksie dla obrazu w skali szarości"

    def showGrayLayer(self, layer_id: int) -> None:
        layer = self.pixels[:, layer_id]
        imshow(layer)
        matplotlib.pyplot.show()

    "metoda wyswietlajaca obraz znajdujacy sie w atrybucie data"

    def showGrayImg(self) -> None:
        imshow(self.pixels, cmap='gray')
        matplotlib.pyplot.show()

    """metoda zwracajaca obraz w sepii jako obiekt klasy BaseImage
       sepia tworzona metoda 1 w przypadku przekazania argumentu alpha_beta
       lub metoda 2 w przypadku przekazania argumentu 'w' """

    def fromRgbToSepia(self, alpha_beta: tuple = (None, None), w: int = None) -> BaseImage:
        if w is None and alpha_beta is not None and \
                (alpha_beta[0] > 1 and alpha_beta[1] < 1 and alpha_beta[0] + alpha_beta[1] == 2):
            self.fromRgbToGray()
            L0, L1, L2 = self.pixels, self.pixels, self.pixels
            L0 = np.where(L0 * alpha_beta[0] > 255, 255, L0 * alpha_beta[0])
            L2 = np.where(L2 * alpha_beta[1] > 255, 255, L2 * alpha_beta[1])
            self.pixels = np.dstack((L0, L1, L2)).astype('i')
            self.colorModel = ColorModel.sepia
            return self
        elif w is not None and alpha_beta[0] is None and alpha_beta[1] is None:
            self.fromRgbToGray()
            L0, L1, L2 = self.pixels, self.pixels, self.pixels
            L0 = np.where(L0 + 2 * w > 255, 255, L0 + 2 * w)
            L1 = np.where(L1 + w > 255, 255, L1 + w)
            self.pixels = np.dstack((L0, L1, L2)).astype('i')
            self.colorModel = ColorModel.sepia
            return self
        else:
            raise Exception("You must specify either '(α and β where α > 1, β < 1 and α+β = 2)'"
                            "or just 'w' between <20, 40> to run the method!")

    def showSepiaConversions(self, alpha_beta: tuple = (None, None), w: int = None) -> None:
        figure, axis = matplotlib.pyplot.subplots(1, 2)
        axis[0].imshow(self.pixels)
        axis[0].set_title("RGB")
        self.fromRgbToSepia(alpha_beta, w)
        axis[1].imshow(self.pixels, cmap='gray')
        if alpha_beta[0] is not None and alpha_beta[1] is not None and w is None:
            axis[1].set_title("RGB -> SEPIA, α = %f, β = %f" % (alpha_beta[0], alpha_beta[1]))
        elif w is not None and alpha_beta[0] is None and alpha_beta[1] is None:
            axis[1].set_title("RGB -> SEPIA, w = %d" % w)
        else:
            raise Exception("You must specify either '(α and β)' or just 'w' to run the method!")
        figure.set_figwidth(12)
        figure.set_figheight(4)
        matplotlib.pyplot.show()


# # # --------------------- GRAY ----------------------
image1 = GrayScaleTransform('C:/Users/kompp3/Desktop/lena.jpg', ColorModel.rgb)
image1.showGrayConversions()

# # # --------------------- SEPIA ----------------------

alpha1 = 1.1
alpha2 = 1.5
alpha3 = 1.9

beta1 = 0.9
beta2 = 0.5
beta3 = 0.1

w1 = 20
w2 = 30
w3 = 40

image3 = GrayScaleTransform(PATH, ColorModel.rgb)
image3.showSepiaConversions((alpha1, beta1))

image4 = GrayScaleTransform(PATH, ColorModel.rgb)
image4.showSepiaConversions((alpha2, beta2))

image5 = GrayScaleTransform(PATH, ColorModel.rgb)
image5.showSepiaConversions((alpha3, beta3))

image5 = GrayScaleTransform(PATH, ColorModel.rgb)
image5.showSepiaConversions(w=w1)

image5 = GrayScaleTransform(PATH, ColorModel.rgb)
image5.showSepiaConversions(w=w2)

image5 = GrayScaleTransform(PATH, ColorModel.rgb)
image5.showSepiaConversions(w=w3)


# --------------------------- ALL CONVERSIONS -----------------------------

def showAllSepiaConversions(path: str = None):

    image = GrayScaleTransform(path, ColorModel.rgb)
    imageW1 = GrayScaleTransform(path, ColorModel.rgb)
    imageW2 = GrayScaleTransform(path, ColorModel.rgb)
    imageW3 = GrayScaleTransform(path, ColorModel.rgb)

    figure, axis = matplotlib.pyplot.subplots(2, 3)
    sepia0 = image.fromRgbToSepia((alpha1, beta1))
    axis[0, 0].imshow(sepia0.pixels, cmap='gray')
    axis[0, 0].set_title("α = %f, β = %f" % (alpha1, beta1))

    sepia1 = image.fromRgbToSepia((alpha2, beta2))
    axis[0, 1].imshow(sepia1.pixels, cmap='gray')
    axis[0, 1].set_title("α = %f, β = %f" % (alpha2, beta2))

    sepia2 = image.fromRgbToSepia((alpha3, beta3))
    axis[0, 2].imshow(sepia2.pixels, cmap='gray')
    axis[0, 2].set_title("α = %f, β = %f" % (alpha3, beta3))

    sepiaW1 = imageW1.fromRgbToSepia(w=w1)
    axis[1, 0].imshow(sepiaW1.pixels, cmap='gray')
    axis[1, 0].set_title("w = %d" % w1)

    sepiaW2 = imageW2.fromRgbToSepia(w=w2)
    axis[1, 1].imshow(sepiaW2.pixels, cmap='gray')
    axis[1, 1].set_title("w = %d" % w2)

    sepiaW3 = imageW3.fromRgbToSepia(w=w3)
    axis[1, 2].imshow(sepiaW3.pixels, cmap='gray')
    axis[1, 2].set_title("w = %d" % w3)

    figure.set_figwidth(20)
    figure.set_figheight(10)
    matplotlib.pyplot.show()


showAllSepiaConversions(PATH)
