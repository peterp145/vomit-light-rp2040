## imports ##
from machine import SPI

COLOR_WHEEL_32 = [
    0xff0000,
    0xff3300,
    0xff6200,
    0xff9500,
    0xffc400,
    0xfff700,
    0xd5ff00,
    0xa6ff00,
    0x73ff00,
    0x40ff00,
    0x11ff00,
    0x00ff22,
    0x00ff51,
    0x00ff84,
    0x00ffb7,
    0x00ffe6,
    0x00e6ff,
    0x00b7ff,
    0x0084ff,
    0x0051ff,
    0x0022ff,
    0x1100ff,
    0x4000ff,
    0x7300ff,
    0xa600ff,
    0xd500ff,
    0xff00f7,
    0xff00c4,
    0xff0095,
    0xff0062,
    0xff0033,
    0xff0000,
]

class PixelBuffer():

    def __init__(self, length: int, width: int = 1) -> None:
        # dimensions of LED strip/array
        self.length = length
        self.width  = 1 #width

        self._pixel_buffer    = bytearray(length*width*3)

    def set_pixel(self, x_pos, value: int) -> None:
        self._pixel_buffer[x_pos*3:x_pos*3+3] = value.to_bytes(3, 'little')

    def set_pixels(self, value: int) -> None:
        for idx in range(self.length):
            self.set_pixel(idx, value)

    def rotate_pixels(self, num_pixels) -> None:
        num_pixels = num_pixels % self.length
        pixel_buffer = self._pixel_buffer[-num_pixels*3:] + self._pixel_buffer[:-num_pixels*3]
        self._pixel_buffer = pixel_buffer

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

    def clear(self):
        self.buffer.set_pixels(0)
        self.update()

    def update(self):
        self._spi.write(self.buffer.pixels)

