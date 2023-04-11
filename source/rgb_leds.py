## imports ##
from machine import SPI

class PixelBuffer():

    def __init__(self, length: int = 32, width: int = 1) -> None:
        # dimensions of LED strip/array
        self.length = length
        self.width  = 1 #width

        self._buffer    = bytearray(length*width*3)

    def set_pixel(self, x_pos, y_pos, value) -> None:
        pass

    def get_pixel(self, x_pos, y_pos) -> bytearray:
        return bytearray(3)
    
    def shift_pixels(self, x_shift, y_shift) -> bytearray:
        return bytearray(1)

class RgbLeds():
    def __init__(self, spi: SPI, length: int = 32) -> None:
        self._spi = spi
        self._length = length

        self.buffer = PixelBuffer()

