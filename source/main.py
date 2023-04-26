## imports ##
from machine import Pin
from time import sleep_ms

from white_leds import WhiteLEDs

## types and constants ##
T_SLEEP_MS = 100

## initialization ##
print("Hello, Darla!")

was_pressed = False
mode_button = Pin(16, Pin.IN, Pin.PULL_UP)
def callback(pin):
    global was_pressed
    was_pressed = True

mode_button.irq(trigger=Pin.IRQ_FALLING, handler=callback)

white_led = WhiteLEDs()
white_led.is_on = True


## main loop ##
while True:
    # print(mode_button.value())
    if was_pressed:
        white_led.is_on = not white_led.is_on
        was_pressed = False

    sleep_ms(T_SLEEP_MS)