from typing import Any
import matplotlib
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from matplotlib.image import imsave
import numpy as np
import cv2


class OpenCirriculumVitae:
    imageOpenCV: np.ndarray

    def __init__(self, PATH) -> None:
        self.imageOpenCV = cv2.imread(PATH, cv2.IMREAD_COLOR)

    def otsu(self):
        img_grayscale = cv2.cvtColor(self.imageOpenCV, cv2.COLOR_BGR2GRAY)
        _, thresh_otsu = cv2.threshold(
            img_grayscale,
            thresh=0,
            maxval=255,
            type=cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        matplotlib.pyplot.imshow(thresh_otsu, cmap='gray')
        matplotlib.pyplot.show()

    def claheGray(self):
        lake_gray = cv2.cvtColor(self.imageOpenCV, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(4, 4)
        )
        equalized_lake_gray = clahe.apply(lake_gray)
        matplotlib.pyplot.subplot(221)
        matplotlib.pyplot.imshow(lake_gray, cmap='gray')

        matplotlib.pyplot.subplot(222)
        matplotlib.pyplot.hist(lake_gray.ravel(), bins=256, range=(0, 256), color='gray')

        matplotlib.pyplot.subplot(223)
        matplotlib.pyplot.imshow(equalized_lake_gray, cmap='gray')

        matplotlib.pyplot.subplot(224)
        matplotlib.pyplot.hist(equalized_lake_gray.ravel(), bins=256, range=(0, 256), color='gray')

        matplotlib.pyplot.show()


    def claheRGB(self):
        lake_rgb = cv2.cvtColor(self.imageOpenCV, cv2.COLOR_BGR2RGB)
        lake_lab = cv2.cvtColor(self.imageOpenCV, cv2.COLOR_BGR2LAB)
        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )
        lake_lab[..., 0] = clahe.apply(lake_lab[..., 0])
        lake_color_equalized = cv2.cvtColor(lake_lab, cv2.COLOR_LAB2RGB)
        matplotlib.pyplot.subplot(221)
        matplotlib.pyplot.imshow(lake_rgb)

        matplotlib.pyplot.subplot(222)
        matplotlib.pyplot.hist(lake_rgb[..., 0].ravel(), bins=256, range=(0, 256), color='b')
        matplotlib.pyplot.hist(lake_rgb[..., 1].ravel(), bins=256, range=(0, 256), color='g')
        matplotlib.pyplot.hist(lake_rgb[..., 2].ravel(), bins=256, range=(0, 256), color='r')

        matplotlib.pyplot.subplot(223)
        matplotlib.pyplot.imshow(lake_color_equalized)

        matplotlib.pyplot.subplot(224)
        matplotlib.pyplot.hist(lake_color_equalized[..., 0].ravel(), bins=256, range=(0, 256), color='b')
        matplotlib.pyplot.hist(lake_color_equalized[..., 1].ravel(), bins=256, range=(0, 256), color='g')
        matplotlib.pyplot.hist(lake_color_equalized[..., 2].ravel(), bins=256, range=(0, 256), color='r')

        matplotlib.pyplot.show()

    def canny(self, th0: int, th1: int, kernel_size: int):
        lena_gray = cv2.cvtColor(self.imageOpenCV, cv2.COLOR_BGR2GRAY)
        canny_edges = cv2.Canny(
            lena_gray,
            th0,  # prog histerezy 1
            th1,  # prog histerezy 2
            kernel_size  # wielkoscc filtra sobela
        )
        matplotlib.pyplot.imshow(canny_edges, cmap='gray')
        matplotlib.pyplot.show()
