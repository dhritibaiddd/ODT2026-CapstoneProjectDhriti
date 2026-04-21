from machine import Pin
import time

# Motor control pins
in1 = Pin(25, Pin.OUT)
in2 = Pin(26, Pin.OUT)

def clockwise():
    in1.value(1)
    in2.value(0)

def anticlockwise():
    in1.value(0)
    in2.value(1)

def stop():
    in1.value(0)
    in2.value(0)

while True:
    print("Clockwise")
    clockwise()
    time.sleep(1)

    print("Anticlockwise")
    anticlockwise()
    time.sleep(1)