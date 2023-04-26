from machine import Pin
from time import ticks_ms, ticks_diff

class TimedButton:

    def __init__(self, pin_id) -> None:        
        self._pin = Pin(pin_id, Pin.IN, Pin.PULL_UP)
        self._pin.irq(self._pin_handler, Pin.IRQ_RISING | Pin.IRQ_FALLING)
        self._press_tick = ticks_ms()
        self._press_time_ms = 0

    def _pin_handler(self, pin):
        flags = pin.irq().flags()

        if flags == Pin.IRQ_FALLING:
            self._press_tick = ticks_ms()
            print("press")
        else:
            self._press_time_ms = ticks_diff(ticks_ms(), self._press_tick)
            print(f"held for {self._press_time_ms} ms")
        
    @property
    def press_time_ms(self):
        press_ms = self._press_time_ms
        self._press_time_ms = 0
        return press_ms