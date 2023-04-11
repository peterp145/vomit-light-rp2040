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

## main loop ##
T_SLEEP_MS = 500
while True:
    # white_led.is_on = not white_led.is_on
    rgb.buffer.set_pixel(0,0xFF0000)
    rgb.buffer.set_pixel(1,0x00FF00)
    rgb.buffer.set_pixel(2,0x0000FF)
    rgb.update()
    sleep_ms(T_SLEEP_MS)

    rgb.buffer.set_pixels(0)
    rgb.update()
    sleep_ms(T_SLEEP_MS)

