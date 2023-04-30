## imports ##
from micropython import const
from machine import Pin
from machine import SPI
from time import sleep_ms

from button import TimedButton
from white_leds import WhiteLEDs
# from states import States
from rgb_leds import RgbLeds

## types and constants ##
T_SLEEP_MS = 100

STATE_HOUSE_ON   = const(0)
STATE_HOUSE_OFF  = const(1)
STATE_SEQUENCE   = const(2)

class StateMachine():
    def __init__(self, white_leds, rgb_led0, button):
        self._white_leds = white_leds
        self._rgb_led0 = rgb_led0
        self._button = button

        self._state = STATE_HOUSE_ON

    def state(self):
        if self._state == STATE_HOUSE_ON:
            next_state = self._house_on()
        elif self._state == STATE_HOUSE_OFF:
            next_state = self._house_off()
        else:
            next_state = self._house_on()

        self._state = next_state

    def _house_on(self) -> int:
        # action
        self._white_leds.is_on = True

        # next state
        press_ms = self._button.press_time_ms
        next_state = STATE_HOUSE_OFF if press_ms > 0 else STATE_HOUSE_ON
        return next_state

    def _house_off(self) -> int:
        # action
        self._white_leds.is_on = False

        # next state
        press_ms = self._button.press_time_ms
        next_state = STATE_HOUSE_ON if press_ms > 0 else STATE_HOUSE_OFF
        return next_state

## initialization ##
print("Hello, Darla!")

white_led = WhiteLEDs()
white_led.is_on = True

rgb = RgbLeds(SPI(0, 400_00))

button = TimedButton(16)

state_machine = StateMachine(white_led, rgb, button)

## main loop ##
while True:
    state_machine.state()
    # print(mode_button.value())
    # press_ms = button.press_time_ms

    # if state == States.IDLE:
    #     if press_ms > 0 and press_ms <= 1000:
    #         white_led.is_on = not white_led.is_on
    #     elif press_ms > 1000 and press_ms <= 3000:
    #         state = States.SEQUENCE1
    #         print("starting seq 1")
    # elif press_ms > 0:
    #     print("returning to idle")
    #     state = States.IDLE
    #     white_led.is_on = True

    sleep_ms(T_SLEEP_MS)