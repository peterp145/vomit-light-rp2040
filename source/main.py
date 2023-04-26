## imports ##
from machine import Pin
from time import sleep_ms

from button import TimedButton
from white_leds import WhiteLEDs
from states import States

## types and constants ##
T_SLEEP_MS = 100

## initialization ##
print("Hello, Darla!")

white_led = WhiteLEDs()
white_led.is_on = True

button = TimedButton(16)

state = States.IDLE

## main loop ##
while True:
    # print(mode_button.value())
    press_ms = button.press_time_ms

    if state == States.IDLE:
        if press_ms > 0 and press_ms <= 1000:
            white_led.is_on = not white_led.is_on
        elif press_ms > 1000 and press_ms <= 3000:
            state = States.SEQUENCE1
            print("starting seq 1")
    elif press_ms > 0:
        print("returning to idle")
        state = States.IDLE
        white_led.is_on = True

    sleep_ms(T_SLEEP_MS)