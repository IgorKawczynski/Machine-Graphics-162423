""" klasa stanowiaca glowny interfejs biblioteki
w pozniejszym czasie bedzie dziedziczyla po kolejnych klasach
realizujacych kolejne metody przetwarzania obrazow """
from lab3.gray_sepia import GrayScaleTransform
from lab4.histogram import ImageComparison
from lab5.imageAligning import ImageAligning


class Image(GrayScaleTransform, ImageComparison, ImageAligning):
    """
    interfejs glownej klasy biblioteki c.d.
    """
    pass