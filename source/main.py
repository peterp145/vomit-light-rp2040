from machine import Pin
from time import sleep_ms

# initialize
print("Hello, Blinky!")

led = Pin("LED", Pin.OUT)

# main loop
while True:
    led.toggle()
    sleep_ms(1000)