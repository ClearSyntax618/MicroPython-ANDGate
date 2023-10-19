import machine
from machine import Pin

ledRojo = Pin(14, Pin.OUT)

SliderA = Pin(2, Pin.IN, Pin.PULL_UP)
SliderB = Pin(15, Pin.IN, Pin.PULL_UP)
SliderC = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    A = SliderA.value()
    B = SliderB.value()
    C = SliderC.value()

    AND = (A and B and C)
    ledRojo.value(AND)