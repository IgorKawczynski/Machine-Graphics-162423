from lab2.basic_image import *
from lab3.gray_sepia import *
from lab3.image import *
from lab3.gray_sepia import *
from lab4.histogram import *
from lab5.imageAligning import *

import matplotlib
import numpy as np
from matplotlib.pyplot import imshow

# # ----------------------------- LAB 1 -----------------------------
# # img_arr = imread(PATH)
# img_arr = imread(PATH)
#
# print(type(img_arr))
# print(img_arr)
#
# imshow(img_arr)
# matplotlib.pyplot.show()
#
# imsave('image.jpg', img_arr)
#
# # mozna rozbic obraz na wszystkie warstwy R G B
# r_layer, g_layer, b_layer = np.squeeze(np.dsplit(img_arr, img_arr.shape[-1]))
# img_stacked_layers = np.dstack((r_layer, g_layer, b_layer))
# imshow(img_stacked_layers)
#
# matplotlib.pyplot.show()
#
# f, ax_arr = matplotlib.pyplot.subplots(1, 3)
# ax_arr[0].imshow(r_layer, cmap='gray')
# ax_arr[1].imshow(g_layer, cmap='gray')
# ax_arr[2].imshow(b_layer, cmap='gray')
#
# matplotlib.pyplot.show()
#
# # Osobne warstwy można z powodzeniem złożyć do postaci obrazu kolorowego.
# # Należy jednak pamiętać o kolejności warstw: RGB:
#
# img_stacked_layers = np.dstack((r_layer, g_layer, b_layer))
# imshow(img_stacked_layers)
#
# matplotlib.pyplot.show()


# # # # -------------------------------------------------- Konwersja ---------------------------------------------------
#
# # # # --------------------- HSV ----------------------
# image1 = BaseImage(PATH, ColorModel.rgb)
# image1.showHsvConversions()
#
# # # # --------------------- HSI ----------------------
# image2 = BaseImage(PATH, ColorModel.rgb)
# image2.showHsiConversions()
#
# # # # --------------------- HSL ----------------------
# image3 = BaseImage(PATH, ColorModel.rgb)
# image3.showHslConversions()


# # # # ------------------------------------------------ Skala Szarości -------------------------------------------------
# image1 = GrayScaleTransform('C:/Users/kompp3/Desktop/lena.jpg', ColorModel.rgb)
# image1.showGrayConversions()
#
# alpha1 = 1.1
# alpha2 = 1.5
# alpha3 = 1.9
#
# beta1 = 0.9
# beta2 = 0.5
# beta3 = 0.1
#
# w1 = 20
# w2 = 30
# w3 = 40
#
# image3 = GrayScaleTransform(PATH, ColorModel.rgb)
# image3.showSepiaConversions((alpha1, beta1))
#
# image4 = GrayScaleTransform(PATH, ColorModel.rgb)
# image4.showSepiaConversions((alpha2, beta2))
#
# image5 = GrayScaleTransform(PATH, ColorModel.rgb)
# image5.showSepiaConversions((alpha3, beta3))
#
# image5 = GrayScaleTransform(PATH, ColorModel.rgb)
# image5.showSepiaConversions(w=w1)
#
# image5 = GrayScaleTransform(PATH, ColorModel.rgb)
# image5.showSepiaConversions(w=w2)
#
# image5 = GrayScaleTransform(PATH, ColorModel.rgb)
# image5.showSepiaConversions(w=w3)
#
# showAllSepiaConversions(PATH)


# # # --------------------------------------------- Histogram i Comparison----------------------------------------------
# # HISTOGRAM
# lena = BaseImage(PATH, ColorModel.rgb)
# lena.showImg()
# lenaRGBHistogram = Histogram(lena.pixels)
# lenaRGBHistogram.plotRGBInOne()
#
# lenaGray = GrayScaleTransform(PATH, colorModel=ColorModel.rgb)
# lenaGray.fromRgbToGray()
# lenaGrayArray = lenaGray.getArray()
# imshow(lenaGray.pixels, cmap='gray')
# matplotlib.pyplot.show()
# lenaGrayHistogram = Histogram(lenaGrayArray)
# lenaGrayHistogram.plot()

# # RMSE I MSE - W SKALI SZAROŚCI
# lenaComparison1 = ImageComparison('C://Users/kompp3/Desktop/lena.jpg', colorModel=ColorModel.rgb)
# lenaComparison2 = ImageComparison('C://Users/kompp3/Desktop/xdxdxd.jpg', colorModel=ColorModel.rgb)
#
# rmse = lenaComparison1.compareTo(lenaComparison2, ImageDiffMethod.rmse)
# mse = lenaComparison1.compareTo(lenaComparison2, ImageDiffMethod.mse)
#
# figure, axis = matplotlib.pyplot.subplots(1, 2)
# axis[0].imshow(lenaComparison1.pixels)
# axis[0].set_title("LENA JPG")
# axis[1].imshow(lenaComparison2.pixels)
# axis[1].set_title("LENA JPG PO ZMIANIE")
# figure.set_figwidth(14)
# figure.set_figheight(14)
# matplotlib.pyplot.xlabel("RMSE = {rmse}  |  MSE = {mse}".format(rmse=rmse, mse=mse))
# matplotlib.pyplot.show()
#
# lenaComparison3 = ImageComparison('C://Users/kompp3/Desktop/lena.jpg', colorModel=ColorModel.rgb)
# lenaComparison4 = Image('C://Users/kompp3/Desktop/lena.jpg', colorModel=ColorModel.rgb)
#
# rmse = lenaComparison3.compareTo(lenaComparison4, ImageDiffMethod.rmse)
# mse = lenaComparison3.compareTo(lenaComparison4, ImageDiffMethod.mse)
#
# figure, axis = matplotlib.pyplot.subplots(1, 2)
# axis[0].imshow(lenaComparison3.pixels)
# axis[0].set_title("LENA JPG")
# axis[1].imshow(lenaComparison4.pixels)
# axis[1].set_title("LENA JPG 2")
# figure.set_figwidth(14)
# figure.set_figheight(14)
# matplotlib.pyplot.xlabel("RMSE = {rmse}  |  MSE = {mse}".format(rmse=rmse, mse=mse))
# matplotlib.pyplot.show()

# # # # --------------------------------------------- Image Aligning----------------------------------------------
# ALIGN DLA RGB
lena = BaseImage(PATH, colorModel=ColorModel.rgb)
imshow(lena.pixels)
matplotlib.pyplot.show()

lenaAlign = ImageAligning(lena).alignImage(tailElimination=False)
imshow(lenaAlign.pixels)
matplotlib.pyplot.show()

image = ImageAligning(lena)
image.compareStandardToAligned(tailElimination=False)

lenaHistogram = Histogram(lena.pixels)
lenaHistogram.plot()

lenaAlignedHistogram = Histogram(ImageAligning(lena).alignImage(tailElimination=False).pixels)
lenaAlignedHistogram.plot()


# # ALIGN + CUMULATIVE DLA Skali szarości
lenaGray = GrayScaleTransform(PATH, colorModel=ColorModel.rgb)
lenaGray.fromRgbToGray()

lenaGrayAlign = ImageAligning(lenaGray).alignImage(tailElimination=False)

imageGray = ImageAligning(lenaGray)
imageGray.compareStandardToAligned(tailElimination=False)


lenaGrayHistogram = Histogram(lenaGray.pixels)
lenaGrayHistogram.plot()

lenaGrayHistogramCumulative = Histogram(lenaGray.pixels).toCumulative()
lenaGrayHistogramCumulative.plotCumulative()

lenaAlignedHistogram = Histogram(lenaGrayAlign.pixels)
lenaAlignedHistogram.plot()





