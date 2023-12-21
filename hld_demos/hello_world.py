#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a simple animation that moves 10 LEDs from left to right
# pip3 install tinkerforge


from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip
import time
import config

HOST = config.HOST
PORT = config.PORT
UID_LED_STRIP_BRICKLET = config.UID_LED_STRIP_BRICKLET
NUM_LEDS = config.NUM_LEDS

# deactivate all LEDs
def clear_screen():
    r = [0]*NUM_LEDS
    g = [0]*NUM_LEDS
    b = [0]*NUM_LEDS
    for i in range(200):        
        ls.set_rgb_values(i, 10, r, g, b)    

if __name__ == "__main__":
    led_ipcon = IPConnection() # Create IP connection
    ls = BrickletLEDStrip(UID_LED_STRIP_BRICKLET, led_ipcon) # Create device object
    led_ipcon.connect(HOST, PORT) # Connect to brickd
        
    clear_screen()
    
    # set 3 LEDs to white, 4 to a bright blue, 3 to white  
    r = [255, 255, 255, 168, 168, 168, 168, 255, 255, 255, 0, 0, 0, 0, 0, 0]
    g = [255, 255, 255, 110, 110, 110, 160, 255, 255, 255, 0, 0, 0, 0, 0, 0]
    b = [255, 255, 255, 50, 50, 50, 50, 255, 255, 255, 0, 0, 0, 0, 0, 0]

    # 0 is the first LED, 200 the last 
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