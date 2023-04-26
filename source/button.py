from machine import Pin

class TimedButton:
    def __init__(self, pin_id) -> None:
        self._was_pressed = False
        
        self._pin = Pin(pin_id, Pin.IN, Pin.PULL_UP)
        self._pin.irq(self.press_handler, Pin.IRQ_FALLING)

    def press_handler(self, pin):
        self._was_pressed = True

    @property
    def was_pressed(self):
        pressed = self._was_pressed
        self._was_pressed = False
        return pressed