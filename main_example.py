import time
from machine import Pin
from morse_code import translate_to_morse_code
led = Pin(5, Pin.OUT)

while True:
    translate_to_morse_code("Gday Luke", led)
    time.sleep(5)
