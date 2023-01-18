from lab2.basic_image import *
import cv2
import matplotlib.pyplot as plt
import numpy as np

# # # WERSJA OPENCV
# x = cv2.__version__
# print(x)
#
# # # Z RGB NA BGR
# image_rgb = cv2.imread(PATH, cv2.COLOR_RGB2BGR)
# cv2.imwrite('C://Users/kompp3/Desktop/lenaBGR.jpg', image_rgb)
# # # !!! ŚCIEŻKA DO LENY BGR !!!
# PATH_BGR = 'C://Users/kompp3/Desktop/lenaBGR.jpg'
#
# # # WCZYTANIE OBRAZU -- ODWRÓCONE RGB --> BGR
img_color = cv2.imread(PATH, cv2.IMREAD_COLOR)
# plt.imshow(img_color)
# plt.show()
# # typ pikseli
# print(type(img_color))
# # wymiar pikseli
# print(img_color.shape)
#
# # # Skala Szarości
# img_grayscale = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)
# plt.imshow(img_grayscale, cmap='gray')
# plt.show()
# print(img_grayscale.shape)
#
# # # Stała IMREAD_UNCHANGED reprezentuje opcję wczytywania obrazów zawierających kanał alpha.
# img_with_alpha = cv2.imread(PATH, cv2.IMREAD_UNCHANGED)
# plt.imshow(img_grayscale, cmap='gray')
# plt.show()
# print(img_with_alpha.shape)
#
# # # Konwersja między modelami barw
#
# # Z RGB NA BGR
# img_bgr = cv2.cvtColor(img_color, cv2.COLOR_RGB2BGR)
# plt.imshow(img_bgr)
# plt.show()
# # Z BGR NA RGB
# img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
# plt.imshow(img_rgb)
# plt.show()
# # Z BGR NA GRAY
# img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
# plt.imshow(img_gray, cmap='gray')
# plt.show()
# # Z BGR NA XYZ
# img_xyz = cv2.cvtColor(img_color, cv2.COLOR_BGR2XYZ)
# plt.imshow(img_xyz)
# plt.show()
# # Z BGR NA HSV
# img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
# plt.imshow(img_hsv)
# plt.show()
# # Z BGR NA HLS
# img_hls = cv2.cvtColor(img_color, cv2.COLOR_BGR2HLS)
# plt.imshow(img_hls)
# plt.show()
# # Z BGR NA LUV
# img_luv = cv2.cvtColor(img_color, cv2.COLOR_BGR2LUV)
# plt.imshow(img_luv)
# plt.show()
# # Z BGR NA LAB
# img_lab = cv2.cvtColor(img_color, cv2.COLOR_BGR2LAB)
# plt.imshow(img_lab)
# plt.show()

# # # THRESHOLDING - PROGOWANIE
#
# # # METODA OTSU
# lena_gray = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)
# _, thresh_otsu = cv2.threshold(
#     lena_gray,
#     thresh=0,
#     maxval=255,
#     type=cv2.THRESH_BINARY + cv2.THRESH_OTSU
# )
# plt.imshow(thresh_otsu, cmap='gray')
# plt.show()
#
# # Metoda Adaptacyjna
# # adaptiveMethod - parametr stałej określającej metodę wyznaczania lokalnych progów
# # ADAPTIVE_THRESH_MEAN_C - wyznaczanie progu na podstawie średniej wartości sąsiednich pikseli
# # ADAPTIVE_THRESH_GAUSSIAN_C - wyznaczanie progu na podstawie sumy ważonej sąsiednich pikseli, gdzie wagi pochodzą z rozkładu gaussowskiego
# # thresholdType - metoda binaryzacji
# # blockSize - wielkośc obszaru sąsiedztwa
# # C - stała odejmowana od obliczonej średniej arytmetycznej lub ważonej
# th_adaptive = cv2.adaptiveThreshold(
#     lena_gray,
#     maxValue=255,
#     adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
#     thresholdType=cv2.THRESH_BINARY,
#     blockSize=13,
#     C=8
# )
# plt.imshow(th_adaptive, cmap='gray')
# plt.show()
#
#
# # DETEKCJA KRAWĘDZI (metodą Canny'ego)
# # Metoda Canny'ego jest rozwinięciem operatora Sobela. Działanie jej polega na wykonaniu nastepujących kroków:
# # wygładzanie obrazu filtrem gaussowskim
# # wyznaczanie gradientów operatorem Sobela
# # zachowanie gradientów które mają odpowiednio dużą wartość w stosunku do otoczenia
# # łączenie i progowanie krawędzi
# # Do wykrycia krawędzi metodą Canny'ego w bibliotece OpenCV służy funkcja Canny, która przyjmuje dwa argumenty numeryczne stanowiące progi histerezy oraz jeden argument stanowiący wielkośc filtra gaussowskiego
# canny_edges = cv2.Canny(
#       lena_gray,
#       16,  # prog histerezy 1
#       40,  # prog histerezy 2
#       3  # wielkoscc filtra sobela
# )
# plt.imshow(canny_edges, cmap='gray')
# plt.show()
#
# # Wyrównanie histogramu metodą CLAHE
# # Metoda CLAHE polega adaptywnym na ograniczaniu wysokich wartości na histogramie. Po dokonaniu operacji wyrównana zostaje redystrybucja krańcowych wartości pikseli po całym obszarze obrazu. Metoda CLAHE znacząco obniża również liczebnośc pikseli o wartościach granicznych.
# # W celu zastosowania implementacji metody CLAHE należy użyć funkcji createCLAHE będącej konstruktorem zwracającym obiekt dokonujący adaptacji histogramu. Następnie, na zwróconym obiekcie należy wywołać metodę apply, do której zostanie przekazany obraz wejściowy.
# # Funkcja createCLAHE przyjmuje dwa parametry:
# # clipLimit - wartość progu do limitowania kontrastu (wielkość odstawania barwy do zredukowania)
# # tileGridSize - wielkość pojedynczych fragmentów, w ktorych wyrownywany jest histogram (wielkosc sasiedztwa ekstremów na histogramie)
# lake_color = cv2.imread(PATH6_500x500_nature, cv2.IMREAD_COLOR)
# lake_gray = cv2.cvtColor(lake_color, cv2.COLOR_BGR2GRAY)
# clahe = cv2.createCLAHE(
#     clipLimit=2.0,
#     tileGridSize=(4, 4)
# )
# equalized_lake_gray = clahe.apply(lake_gray)
# plt.subplot(221)
# plt.imshow(lake_gray, cmap='gray')
#
# plt.subplot(222)
# plt.hist(lake_gray.ravel(), bins=256, range=(0, 256), color='gray')
#
# plt.subplot(223)
# plt.imshow(equalized_lake_gray, cmap='gray')
#
# plt.subplot(224)
# plt.hist(equalized_lake_gray.ravel(), bins=256, range=(0, 256), color='gray')
#
# plt.show()
#
#
# # Korekcja histogramu w obrazach kolorowych
# # Jednym z najczęstszych podejść w korekcji histogramu obrazu kolorowego jest konwersja do przestrzeni Lab, a nastepnie dokonanie metody CLAHE jedynie na warstwie L reprezentującej jasność
# lake_rgb = cv2.cvtColor(lake_color, cv2.COLOR_BGR2RGB)
# lake_lab = cv2.cvtColor(lake_color, cv2.COLOR_BGR2LAB)
#
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# lake_lab[..., 0] = clahe.apply(lake_lab[..., 0])
# lake_color_equalized = cv2.cvtColor(lake_lab, cv2.COLOR_LAB2RGB)
# plt.subplot(221)
# plt.imshow(lake_rgb)
#
# plt.subplot(222)
# plt.hist(lake_rgb[..., 0].ravel(), bins=256, range=(0, 256), color='b')
# plt.hist(lake_rgb[..., 1].ravel(), bins=256, range=(0, 256), color='g')
# plt.hist(lake_rgb[..., 2].ravel(), bins=256, range=(0, 256), color='r')
#
# plt.subplot(223)
# plt.imshow(lake_color_equalized)
#
# plt.subplot(224)
# plt.hist(lake_color_equalized[..., 0].ravel(), bins=256, range=(0, 256), color='b')
# plt.hist(lake_color_equalized[..., 1].ravel(), bins=256, range=(0, 256), color='g')
# plt.hist(lake_color_equalized[..., 2].ravel(), bins=256, range=(0, 256), color='r')
#
# plt.show()


# # # Transformaty Hougha
# # Transformata Hougha - metoda wykrywania obiektów w wizji komputerowej. Jest szczególnym przypadkiem transformaty Radona znanej od 1917 roku. Oryginalna metoda Hougha służy do wykrywania prostych, natomiast jej modyfikacje umozliwiają detekcję również innych kształtów.


# # # Detekcja prostych
# # W OpenCV istnieją dwie funkcje przeznaczone do detekcji prostych za pomocą transformaty Hougha:
# HoughLines - wersja deterministyczna
# HoughLinesP - wersja stochastyczna, zoptymalizowana pod kątem wydajności obliczeń
# # Obie funkcje mają bardzo podobne interfejsy i przyjmują następujące parametry:
# rho - 1 rozdzielczość kontenerów na linie
# theta - kąt stanowiący odstęp przy badaniu prostych
# threshold - próg liczby głosów poniżej którego wykryte linie są odrzucane

# # WCZYTANIE OBRAZU DO DETEKCJI PROSTYCH
# lines_img = cv2.imread('lines.jpg', cv2.IMREAD_GRAYSCALE)
# plt.imshow(lines_img, cmap='gray')
# plt.show()
#
# # THRESHOLD NAJPIERW
# _, lines_thresh = cv2.threshold(
#     lines_img,
#     thresh=0,
#     maxval=255,
#     type=cv2.THRESH_BINARY + cv2.THRESH_OTSU
# )
# plt.imshow(lines_thresh, cmap='gray')
# plt.show()
#
# # I DETEKCJA
# lines_edges = cv2.Canny(lines_thresh, 20, 50, 3)
# plt.imshow(lines_edges, cmap='gray')
# plt.show()
# lines = cv2.HoughLinesP(lines_edges, 2, np.pi / 180, 30)
# print(len(lines))
#
# result_lines_img = cv2.cvtColor(lines_img, cv2.COLOR_GRAY2RGB)
# for line in lines:
#   x0, y0, x1, y1 = line[0]
#   cv2.line(result_lines_img, (x0, y0), (x1, y1), (0, 255, 0), 5)
# plt.imshow(result_lines_img)
# plt.show()

# # # # Detekcja okręgów
# # # Do detekcji okręgów za pomocą modyfikacji transformaty Hougha przeznaczona jest funkcja HoughCircles, która przyjmuje następujące parametry:
# # method - placeholder dla kolejnych modyfikacji (w tym momencie dostępna jest tylko jedna)
# # dp - odwrotny współczynik rozdzielczości kontenera na głosy
# # minDist - minimalna odległość między środkami okręgów, przy małej wartości może występować wiele fałszywych detekcji
# # minRadius - minimalny promień wykrytego okręgu
# # maxRadius - maksymalny promień wykrytego okręgu
# checkers_img = cv2.imread('checkers.png')
# checkers_gray = cv2.cvtColor(checkers_img, cv2.COLOR_BGR2GRAY)
# checkers_color = cv2.cvtColor(checkers_img, cv2.COLOR_BGR2RGB)
# circles = cv2.HoughCircles(
#     checkers_gray,
#     method=cv2.HOUGH_GRADIENT,
#     dp=2,
#     minDist=60,
#     minRadius=20,
#     maxRadius=100
# )
# print(len(circles[0]))
# for (x, y, r) in circles.astype(int)[0]:
#   cv2.circle(checkers_color, (x, y), r, (0, 255, 0), 4)
#
# plt.imshow(checkers_color)
# plt.show()