## imports ##
from machine import Pin
from time import sleep_ms

from button import TimedButton
from white_leds import WhiteLEDs

## types and constants ##
T_SLEEP_MS = 100

## initialization ##
print("Hello, Darla!")

white_led = WhiteLEDs()
white_led.is_on = True

button = TimedButton(16)

## main loop ##
while True:
    # print(mode_button.value())
    press_ms = button.press_time_ms
    if press_ms > 0 and press_ms < 1000:
        white_led.is_on = not white_led.is_on

    sleep_ms(T_SLEEP_MS)