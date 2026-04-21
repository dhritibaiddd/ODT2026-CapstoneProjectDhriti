from machine import Pin, PWM
import neopixel
import time

NEO_PIN  = 15
NUM_LEDS = 24
BUZZER_PIN = 23

np = neopixel.NeoPixel(Pin(NEO_PIN), NUM_LEDS)
buzzer = PWM(Pin(BUZZER_PIN))

# ---------- HELPERS ----------

def set_all(r, g, b):
    for i in range(NUM_LEDS):
        np[i] = (r, g, b)
    np.write()

def tone(freq, duration_ms):
    buzzer.freq(freq)
    buzzer.duty(512)   # sound ON
    time.sleep_ms(duration_ms)
    buzzer.duty(0)     # sound OFF

# ---------- NEW: BLUE FADE IN ----------

print("Starting fade-in")

for b in range(0, 255, 5):
    set_all(0, 0, b)
    buzzer.freq(300 + b*2)   # rising tone with brightness
    buzzer.duty(300)
    time.sleep_ms(25)

buzzer.duty(0)

# ---------- ORIGINAL PORTAL PATTERN ----------

print("Portal pattern")

for pulse in range(3):

    # Fade blue → purple
    for step in range(0, 50, 2):
        set_all(step * 2, 0, 255 - step)
        buzzer.freq(500 + step*10)   # rising eerie tone
        buzzer.duty(200)
        time.sleep_ms(18)

    # Fade purple → blue
    for step in range(50, 0, -2):
        set_all(step * 2, 0, 255 - step)
        buzzer.freq(500 + step*10)
        buzzer.duty(200)
        time.sleep_ms(18)

buzzer.duty(0)

# ---------- FLASHES ----------

print("Flashes")

for flash in range(2):
    set_all(255, 255, 255)

    tone(2000, 120)   # sharp high-pitch flash sound

    set_all(0, 0, 0)
    time.sleep_ms(80)

set_all(0, 0, 0)

# ---------- READY BEEPS ----------

tone(1000, 100)
time.sleep_ms(100)
tone(1200, 100)

print("Pattern and buzzer test done.")