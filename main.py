from lab2.basic_image import *
from lab3.gray_sepia import *
from lab3.image import *
from lab3.gray_sepia import *
from lab4.histogram import *
from lab5.imageAligning import *
from lab7.imageThresholding import Thresholding
from lab8.openCirriculumVitae import *
import matplotlib
import numpy as np
from matplotlib.pyplot import imshow
from PIL import Image

# # ----------------------------- LAB 1 -----------------------------

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
# # # --------------------- HSV ----------------------
image1 = BaseImage(PATH6_500x500_nature, ColorModel.rgb)
image1.showHsvConversions()

# # # --------------------- HSI ----------------------
image2 = BaseImage(PATH, ColorModel.rgb)
image2.showHsiConversions()

# # # --------------------- HSL ----------------------
image3 = BaseImage(PATH6_500x500_nature, ColorModel.rgb)
image3.showHslConversions()


# # # # ------------------------------------------------ Skala Szarości -------------------------------------------------
image1 = GrayScaleTransform('C:/Users/kompp3/Desktop/natura500_1.jpg', ColorModel.rgb)
image1.showGrayConversions()
imageBaseImage = BaseImage('C:/Users/kompp3/Desktop/natura500_1.jpg', ColorModel.rgb)

alpha1 = 1.1
alpha2 = 1.5
alpha3 = 1.9

beta1 = 0.9
beta2 = 0.5
beta3 = 0.1

w1 = 20
w2 = 30
w3 = 40

image3 = GrayScaleTransform(imageBaseImage.pixels, imageBaseImage.colorModel)
image3.showSepiaConversions((alpha1, beta1))

image4 = GrayScaleTransform(PATH6_500x500_nature, ColorModel.rgb)
image4.showSepiaConversions((alpha2, beta2))

image5 = GrayScaleTransform(PATH6_500x500_nature, ColorModel.rgb)
image5.showSepiaConversions((alpha3, beta3))

image5 = GrayScaleTransform(PATH6_500x500_nature, ColorModel.rgb)
image5.showSepiaConversions(w=w1)

image5 = GrayScaleTransform(PATH6_500x500_nature, ColorModel.rgb)
image5.showSepiaConversions(w=w2)

image5 = GrayScaleTransform(PATH6_500x500_nature, ColorModel.rgb)
image5.showSepiaConversions(w=w3)

showAllSepiaConversions(PATH6_500x500_nature)


# # # --------------------------------------------- Histogram i Comparison----------------------------------------------
# # HISTOGRAM
lena = BaseImage(PATH, ColorModel.rgb)
lena.showImg()
lenaRGBHistogram = Histogram(lena.pixels)
lenaRGBHistogram.plotRGBInOne()

lenaGray = GrayScaleTransform(PATH, colorModel=ColorModel.rgb)
lenaGray.fromRgbToGray()
lenaGrayArray = lenaGray.getArray()
lenaGray.showGrayImg()
# imshow(lenaGray.pixels, cmap='gray')  # inny sposob na wyswietlenie graysScale
# matplotlib.pyplot.show()
lenaGrayHistogram = Histogram(lenaGrayArray)
lenaGrayHistogram.plot()
#
# # RMSE I MSE - W SKALI SZAROŚCI
lenaComparison1 = ImageComparison('C://Users/kompp3/Desktop/lena.jpg', colorModel=ColorModel.rgb)
lenaComparison2 = ImageComparison('C://Users/kompp3/Desktop/xdxdxd.jpg', colorModel=ColorModel.rgb)

rmse = lenaComparison1.compareTo(lenaComparison2, ImageDiffMethod.rmse)
mse = lenaComparison1.compareTo(lenaComparison2, ImageDiffMethod.mse)

figure, axis = matplotlib.pyplot.subplots(1, 2)
axis[0].imshow(lenaComparison1.pixels)
axis[0].set_title("LENA JPG")
axis[1].imshow(lenaComparison2.pixels)
axis[1].set_title("LENA JPG PO ZMIANIE")
figure.set_figwidth(14)
figure.set_figheight(14)
matplotlib.pyplot.xlabel("RMSE = {rmse}  |  MSE = {mse}".format(rmse=rmse, mse=mse))
matplotlib.pyplot.show()

# # # # # --------------------------------------------- Image Aligning----------------------------------------------

# # # ALIGN DLA RGB
image = BaseImage(PATH, colorModel=ColorModel.rgb)

imageAligned = ImageAligning(image)
imageAligned.compareStandardToAligned()
# imageAligned.saveImg('C://Users/kompp3/Desktop/hehe.jpg')

imageHistogram = Histogram(image.pixels)
imageHistogram.plotRGBInOne()

imageAlignWithoutTailElimination = ImageAligning(image).alignImage(tailElimination=False)
imageAlignedWithoutTailEliminationHistogram = Histogram(imageAlignWithoutTailElimination.pixels)
imageAlignedWithoutTailEliminationHistogram.plotRGBInOne()

imageAlignWithTailElimination = ImageAligning(image).alignImage(tailElimination=True)
imageAlignedWithTailEliminationHistogram = Histogram(imageAlignWithTailElimination.pixels)
imageAlignedWithTailEliminationHistogram.plotRGBInOne()
#
# # # ALIGN + CUMULATIVE DLA Skali szarości
imageGray = GrayScaleTransform(PATH, colorModel=ColorModel.rgb)
imageGray.fromRgbToGray()

imageGray = ImageAligning(imageGray)
imageGray.compareStandardToAligned()

imageGrayHistogram = Histogram(imageGray.pixels)
imageGrayHistogram.plot()

imageGrayHistogramCumulative = Histogram(imageGray.pixels).toCumulative()
imageGrayHistogramCumulative.plotCumulative()

imageGrayAlignWithoutTailElimination = ImageAligning(imageGray).alignImage(tailElimination=False)
imageAlignedHistogram = Histogram(imageGrayAlignWithoutTailElimination.pixels)
imageAlignedHistogram.plot()

imageGrayAlignWithTailElimination = ImageAligning(imageGray).alignImage(tailElimination=True)
imageAlignedHistogram = Histogram(imageGrayAlignWithTailElimination.pixels)
imageAlignedHistogram.plot()


# # # # # --------------------------------------------- Image Filtering----------------------------------------------
# # # Kernele W LAB6 SĄ:
# #
# # # FILTRY
#
from lab6.imageFiltering import *

imageToFilter = BaseImage('./lab6/img/lena.jpg', ColorModel.rgb)
imageToFilter.showImg()

filteredTOPImage = ImageFiltering(imageToFilter)
filteredTOPImage.showFilters()
#
# # # DETEKCJA KRAWEDZI
imageToEdgeDetect = BaseImage('./lab6/img/sudoku2.jpg', ColorModel.rgb)
imageToEdgeDetect.showImg()

edgeDetectionTOPImage = ImageFiltering(imageToEdgeDetect)
edgeDetectionTOPImage.showEdgeDetection()

# # # PO KOLEI KAZDY KERNEL
# # # 1-wersja
# image = BaseImage('./lab6/img/nieLena.jpg', ColorModel.rgb)
# filteredImage = ImageFiltering(image)
# filteredImage.showFiltered2D(sobel45)
# # # 2-wersja
# image = BaseImage('./lab6/img/nieLena.jpg', ColorModel.rgb)
# filteredImage = ImageFiltering(image)
# filteredImage.filter(highPassKernel)
# filteredImage.showImg()

# # # # # -------------------------------------------- Image Thresholding ---------------------------------------------
# # Przykład pojedynczy
image = BaseImage(PATH, colorModel=ColorModel.rgb)
imageGray = GrayScaleTransform(PATH, colorModel=ColorModel.rgb)
imageGray.fromRgbToGray()
imageT = Thresholding(image)
imageT.threshold(127)
imshow(imageT.pixels, cmap='gray')
matplotlib.pyplot.show()
# # Wyświetlenie po kolei lub wszystkich na raz
image = BaseImage(PATH, colorModel=ColorModel.rgb)
imageT = Thresholding(image)
imageT.showThresholded(30)
imageT.showThresholded(70)
imageT.showThresholded(127)
imageT.showThresholded(170)
imageT.showThresholded(220)
image2 = BaseImage(PATH6_500x500_nature, colorModel=ColorModel.rgb)
imageT2 = Thresholding(image2)
imageT2.showAllThresholded()


# # # # # ---------------------------------------------- OPEN CV 2 -----------------------------------------------


# # # # --------------------- OTSU ----------------------
image = OpenCirriculumVitae('C://Users/kompp3/Desktop/lena.jpg')
image.otsu()

image2 = OpenCirriculumVitae('C://Users/kompp3/Desktop/lena.jpg')
image2.claheGray()

image3 = OpenCirriculumVitae('C://Users/kompp3/Desktop/lena.jpg')
image3.claheRGB()

image4 = OpenCirriculumVitae('C://Users/kompp3/Desktop/lena.jpg')
image4.canny(16, 40, 3)

