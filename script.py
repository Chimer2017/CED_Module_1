# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import requests
import json
from random import seed
from random import randint
from random import random


def getNewDiceValue():
    try:
        res = requests.get("http://roll.diceapi.com/json/d8/d6")
        if res.status_code == 200:
            data = res.json()
            index = data['dice'][0]['value']
            col = data['dice'][1]['value']
            return [index,col]
        else:
            print("error")
    except:
        return [1,1]
    

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 8

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER
)



pixels.fill((0, 0, 0))
pixels.show()
time.sleep(0.5)
pixels.fill((0, 255, 0))
pixels.show()

timeCount = 0.90



    
    
def orderLightUp():
    for i in range(0,10):
        color = (randint(0,255),randint(0,255),randint(0,255))
        for i in range(0,8):
            pixels[i] = color
            pixels.show()
            time.sleep(0.1)
    
    

count = 0
while True:
    print("loop")
    randVals = getNewDiceValue()
    seed(randVals[1])
    pixels[randVals[0]-1] = (randint(0,255),randint(0,255),randint(0,255))
    pixels.show()
    time.sleep(timeCount)
    if timeCount >= 0.04:
        timeCount = timeCount - 0.02
        
    count += 1
    if ( count % 4 == 0):
        orderLightUp()


  
