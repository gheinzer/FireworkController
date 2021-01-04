from machine import Pin
from lib.nextion import nextion
import time

display = nextion(12, 13, 9600)

def LAUNCH(channel):
    if(channel==1 or channel=="1"):
        relay = Pin(22, Pin.OUT)
        relay.on()
        time.sleep(3)
        relay.off()
    if(channel==2 or channel=="2"):
        relay = Pin(23, Pin.OUT)
        relay.on()
        time.sleep(3)
        relay.off()
        
def man_launch():
    print("MANUAL LAUNCH (WITHOUT WARNINGS)")
    response = None
    while response is None:
        response = display.read()
    output = bytearray(response).decode("ASCII")
    output = str(output).replace("b'", "")
    output = str(output).replace("'", "")
    print("Received output data. Output: " + output)
    LAUNCH(int(output))