from machine import Pin
import sys

def lookForTasterPress():
    taster = Pin(0, Pin.IN)
    default_taster_value = taster.value()

    while 1:
        if(not taster.value() == default_taster_value):
            quit()
