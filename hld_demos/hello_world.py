#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Eine einfache Animation bei der 10 LEDs von links nach rechts über die Wand bewegen

HOST = "192.168.178.230"
PORT = 4223
LED_UID = "yph" # Change XYZ to the UID of your LED Strip Bricklet
NUM_LEDS = 16

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip
import time

def clear_screen():
    r = [0]*NUM_LEDS
    g = [0]*NUM_LEDS
    b = [0]*NUM_LEDS
    for i in range(200):        
        ls.set_rgb_values(i, 10, r, g, b)    

if __name__ == "__main__":
    led_ipcon = IPConnection() # Create IP connection
    ls = BrickletLEDStrip(LED_UID, led_ipcon) # Create device object
    led_ipcon.connect(HOST, PORT) # Connect to brickd
        
    # deaktiviere alle LEDs
    clear_screen()
    
    # setze 3 LEDs auf die Werte r,g,b, 4 LEDs und 3 weitere LEDs    
    r = [255, 255, 255, 168, 168, 168, 168, 255, 255, 255, 0, 0, 0, 0, 0, 0]
    g = [255, 255, 255, 110, 110, 110, 160, 255, 255, 255, 0, 0, 0, 0, 0, 0]
    b = [255, 255, 255, 50, 50, 50, 50, 255, 255, 255, 0, 0, 0, 0, 0, 0]

    # 0 ist die erste LED, 200 die letzte
    for x in range(3):        
        ls.set_rgb_values(0, 10, r,g,b)
        i = 0
        while i < 200:                    
            time.sleep(0.1)
            ls.set_rgb_values(i, 10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            i = i + 10        
            ls.set_rgb_values(i, 10, r,g,b)
        while i > 0:        
            time.sleep(0.1)
            ls.set_rgb_values(i, 10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            i = i - 10        
            ls.set_rgb_values(i, 10, r,g,b)
    
    led_ipcon.disconnect()