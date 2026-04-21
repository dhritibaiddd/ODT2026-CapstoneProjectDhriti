from machine import Pin
import time

laser = Pin(5, Pin.OUT)
pb = Pin(4, Pin.IN, Pin.PULL_UP)
ldr = Pin(34, Pin.IN)

THRESHOLD = 3000  

while True:
    print(pb.value())
    value1 = pb.value()
    if value1 == 0 :
        print("Laser Activated")
        laser.on()
        time.sleep(2)
        
    value2 = ldr.value()    
    if ldr.value()    == 0 :
        print("Beam Detected   | LDR:", value2)
    else:
        print("NO Beam | LDR:", value2)
    
    time.sleep_ms(200)