## imports ##
from machine import SPI

class PixelBuffer():

    def __init__(self, length: int = 32, width: int = 1) -> None:
        # dimensions of LED strip/array
        self.length = length
        self.width  = 1 #width

        self._pixel_buffer    = bytearray(length*width*3)

    def set_pixel(self, x_pos, value: int) -> None:
        self._pixel_buffer[x_pos*3:x_pos*3+3] = value.to_bytes(6, 'little')

    def set_pixels(self, value: int) -> None:
        for idx in range(self.length):
            self.set_pixel(idx, value)

    def get_pixel(self, x_pos) -> int:
        return int(self._pixel_buffer[x_pos*3:x_pos*3+3])
    
    # def shift_pixels(self, x_shift) -> bytearray:
    #     return bytearray(1)
    
    @property
    def pixels(self) -> bytearray:
        return self._pixel_buffer

class RgbLeds():
    def __init__(self, spi: SPI, length: int = 32) -> None:
        self._spi = spi
        self._length = length

        self.buffer = PixelBuffer(length)
        self.update()

    def update(self):
        self._spi.write(self.buffer.pixels)

