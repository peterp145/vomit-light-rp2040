## imports ##
from machine import Pin

## helpers ##

## api ##
class WhiteLEDs:
    def __init__(self, pin_id: str = "LED", enable: bool = False):
        self._pin = Pin(pin_id, Pin.OUT)
        self._pin.off()
        self._state = False

    @property
    def is_on(self) -> bool:
        return self._state
    
    @is_on.setter
    def is_on(self, value: bool):
        if(value):
            self._state = True
            self._pin.on()
        else:
            self._state = False
            self._pin.off()
    
