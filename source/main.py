from machine import Pin
from machine import SPI
from time import sleep_ms
from rgb_leds import RgbLeds

# initialize
print("Hello, Darla!")

led = Pin("LED", Pin.OUT)
# spi = SPI(0, 400_000)
# rgb = RgbLeds(spi)

# main loop
while True:
    led.toggle()
    sleep_ms(1000)