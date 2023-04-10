## imports ##
from machine import SPI

class RgbLeds():
    def __init__(self, spi: SPI, length: int = 32) -> None:
        self._spi = spi
        self._length = length
