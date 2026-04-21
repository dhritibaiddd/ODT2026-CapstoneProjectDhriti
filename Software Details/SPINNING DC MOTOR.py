from machine import Pin, PWM
import time

ena = PWM(Pin(33), freq=100)
in1 = Pin(25, Pin.OUT)
in2 = Pin(26, Pin.OUT)

# Forward
print("Forward")
in1.value(1)
in2.value(0)
ena.duty_u16(65535)
time.sleep(3)

# Stop
in1.value(0)
in2.value(0)
ena.duty_u16(0)
time.sleep(1)

# Backward
print("Backward")
in1.value(0)
in2.value(1)
ena.duty_u16(20000)
time.sleep(3)

# Stop
in1.value(0)
in2.value(0)
ena.duty_u16(0)
print("Done.")