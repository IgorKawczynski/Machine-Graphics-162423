from PIL import Image

from lab2.basic_image import *


class ImageFiltering(BaseImage):

    def __init__(self, baseImage) -> None:
        super().__init__(baseImage.pixels, baseImage.colorModel)
    """
    kernel: filtr w postaci tablicy numpy
    prefix: przedrostek filtra, o ile istnieje; Optional - forma poprawna obiektowo, lub domyslna wartosc = 1 - optymalne arytmetycznie
    metoda zwroci obraz po procesie filtrowania
    """
    def convolve2D(self, kernel: np.ndarray, padding=(1, 1)):

        if self.pixels.ndim == 2:
            self.pixels = np.expand_dims(self.pixels, axis=-1)
        if kernel.ndim == 2:
            kernel = np.repeat(np.expand_dims(kernel, axis=-1), self.pixels.shape[-1], axis=-1)
        if kernel.shape[-1] == 1:
            kernel = np.repeat(kernel, self.pixels.shape[-1], axis=-1)

        assert self.pixels.shape[-1] == kernel.shape[-1]
        size_x, size_y = kernel.shape[:2]
        width, height = self.pixels.shape[:2]

        output_array = np.zeros(((width - size_x + 2 * padding[0]) + 1,
                                 (height - size_y + 2 * padding[1]) + 1,
                                 self.pixels.shape[-1]))

        padded_image = np.pad(self.pixels, [
            (padding[0], padding[0]),
            (padding[1], padding[1]),
            (0, 0)
        ])

        for x in range(
                padded_image.shape[0] - size_x + 1):
            for y in range(padded_image.shape[1] - size_y + 1):
                window = padded_image[x:x + size_x, y:y + size_y]
                output_values = np.sum(kernel * window, axis=(0, 1))
                output_array[x, y] = output_values

        return output_array  # DLA SUDOKU WYLACZYC .astype('') :)

    def showFiltered2D(self, kernel):
        convolvedArray = ImageFiltering(self).convolve2D(kernel, padding=(1, 1))  # moze trzeba .astype('i') tu dac
        convolvedImage = Image.fromarray(np.uint8(1 * convolvedArray), 'RGB')
        convolvedImage.show()

    def filter(self, kernel):
        self.pixels = self.convolve2D(kernel).astype('i')

    def showFilters(self):

        identityKernel = np.array([  # Filtr Tożsamościowy
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ], dtype=np.float32)

        highPassKernel = np.array([  # Filtr górnoprzepustowy
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ], dtype=np.float32)

        lowPassKernel = np.array([  # Filtr dolnoprzepustowy
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ], dtype=np.float32) / 9

        gaussThreeKernel = np.array([  # Filtr Gaussa wersja 3x3
            [1, 2, 1],
            [2, 4, 2],
            [1, 2, 1]
        ], dtype=np.float32) / 16

        gaussFiveKernel = np.array([  # Filtr Gaussa wersja 5x5
            [1, 4, 6, 4, 1],
            [4, 16, 24, 16, 4],
            [6, 24, 36, 24, 6],
            [4, 16, 24, 16, 4],
            [1, 4, 6, 4, 1]
        ], dtype=np.float32) / 256

        figure, axis = matplotlib.pyplot.subplots(2, 3)
        axis[0, 0].imshow(self.pixels)
        axis[0, 0].set_title("Standard Image")
        identityArray = self.convolve2D(identityKernel).astype('i')
        axis[0, 1].imshow(identityArray)
        axis[0, 1].set_title("Identity Filter")
        highPassArray = self.convolve2D(highPassKernel).astype('i')
        axis[0, 2].imshow(highPassArray)
        axis[0, 2].set_title("High-Pass Filter")
        lowPassArray = self.convolve2D(lowPassKernel).astype('i')
        axis[1, 0].imshow(lowPassArray)
        axis[1, 0].set_title("Low-Pass Filter")
        gaussThreeArray = self.convolve2D(gaussThreeKernel).astype('i')
        axis[1, 1].imshow(gaussThreeArray)
        axis[1, 1].set_title("Gauss 3x3 Filter")
        gaussFiveArray = self.convolve2D(gaussFiveKernel).astype('i')
        axis[1, 2].imshow(gaussFiveArray)
        axis[1, 2].set_title("Gauss 5x5 Filter")
        figure.set_figwidth(16)
        figure.set_figheight(16)
        matplotlib.pyplot.show()

    def showEdgeDetection(self):

        sobel0 = np.array([  # Operator Sobela - detekcja krawędzi - 0 stopni
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ], dtype=np.float32)

        sobel45 = np.array([  # Operator Sobela - detekcja krawędzi - 45 stopni
            [0, 1, 2],
            [-1, 0, 1],
            [-2, -1, 0]
        ], dtype=np.float32)

        sobel90 = np.array([  # Operator Sobela - detekcja krawędzi - 90 stopni
            [1, 2, 1],
            [0, 0, 0],
            [-1, -2, -1]
        ], dtype=np.float32)

        sobel135 = np.array([  # Operator Sobela - detekcja krawędzi - 135 stopni
            [2, 1, 0],
            [1, 0, -1],
            [0, -1, -2]
        ], dtype=np.float32)

        figure, axis = matplotlib.pyplot.subplots(1, 4)
        sobel0Array = self.convolve2D(sobel0)
        axis[0].imshow(sobel0Array)
        axis[0].set_title("Sobel 0-degree Edge Detection")
        sobel45Array = self.convolve2D(sobel45)
        axis[1].imshow(sobel45Array)
        axis[1].set_title("Sobel 45-degree Edge Detection")
        sobel90Array = self.convolve2D(sobel90)
        axis[2].imshow(sobel90Array)
        axis[2].set_title("Sobel 90-degree Edge Detection")
        sobel135Array = self.convolve2D(sobel135)
        axis[3].imshow(sobel135Array)
        axis[3].set_title("Sobel 135-degree Edge Detection")
        figure.set_figwidth(14)
        figure.set_figheight(6)
        matplotlib.pyplot.show()
