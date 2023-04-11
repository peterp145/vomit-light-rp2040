## imports ##
# builtins
from machine import Pin
from machine import SPI
from time import sleep_ms

# my libs
from rgb_leds import RgbLeds
from white_leds import WhiteLEDs

## initialization ##
print("Hello, Darla!")

# peripherals
white_led = WhiteLEDs()
white_led.is_on = True

spi = SPI(0, 400_000)
rgb = RgbLeds(spi)

rgb.buffer.set_pixel(0,0xFF0000)
rgb.buffer.set_pixel(1,0x00FF00)
rgb.buffer.set_pixel(2,0x0000FF)

rgb.buffer.set_pixel(8,0xFF0000)
rgb.buffer.set_pixel(9,0x00FF00)
rgb.buffer.set_pixel(10,0x0000FF)

## main loop ##
T_SLEEP_MS = 50
while True:
    # white_led.is_on = not white_led.is_on
    rgb.buffer.rotate_pixels(1)
    rgb.update()
    sleep_ms(T_SLEEP_MS)
