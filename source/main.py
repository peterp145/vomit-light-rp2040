## imports ##
# builtins
from machine import Pin
from machine import SPI
from time import sleep_ms

# my libs
from rgb_leds import RgbLeds, COLOR_WHEEL_32
from white_leds import WhiteLEDs

## initialization ##
print("Hello, Darla!")

# peripherals
white_led = WhiteLEDs()
white_led.is_on = True

spi = SPI(0, 400_000)
rgb = RgbLeds(spi)

for idx, color in enumerate(COLOR_WHEEL_32):
    rgb.buffer.set_pixel(idx, color)
rgb.update()

## main loop ##
T_SLEEP_MS = 100
while True:
    # white_led.is_on = not white_led.is_on
    rgb.buffer.rotate_pixels(1)
    rgb.update()
    sleep_ms(T_SLEEP_MS)
