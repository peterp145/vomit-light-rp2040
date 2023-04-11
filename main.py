## imports ##
# builtins
from machine import Pin
from machine import SPI
from time import sleep_ms

# my libs
# import sys
# sys.path.append('source')

# from rgb_leds import RgbLeds
from white_leds import WhiteLEDs

## initialization ##
print("Hello, Darla!")

# peripherals
white_led = WhiteLEDs()
# white_led.is_on = True

# led = Pin("LED", Pin.OUT)
# spi = SPI(0, 400_000)
# rgb = RgbLeds(spi)

## main loop ##
while True:
    # white_led.is_on = not white_led.is_on
    sleep_ms(1000)