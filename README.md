How I Built It:

 This project was built using Raspberry Pi hardware as well as Python and Processing scripts. No soldering or welding was required. This is a straightforward project to do with the raspberry pi.

Materials

Raspberry Pi 3B+
3 female to female wires
8 LED Neopixel
Power source ( 5V input into the pi)

Hardware

The hardware build was rather simple. The neopixel requires 3 inputs: power, signal, and ground. On the raspberry pi, I connected the GPIO 21 signal pin to the corresponding input pin on the neopixel. This was also done with ground and power pins. Once the neopixel was wired up, it was time to get coding

***Hint: At first I used the GPIO 18 pin for signal, and it did not work well. You may have to troubleshoot with the pins at first.

Software

Now, this was the interesting part. Code was used to create the animation as well as to program the neopixel. Let’s start with the neopixel.

The neopixel has a supported library in python that makes it incredibly easy to interface with. I won’t go into details here, but a great tutorial can be found here. The idea for the neopixel was for the light display to begin in a random manner and progressively become more ordered. This was executed in the following way. I used a web API called “rollthedice”, which is a really good random number generator, to then seed the random number function in python ( yes, two layers of random, was it necessary, I’m not sure?!?!). Using the double random process, I choose a random pixel on which to change the color. The color is also randomly generated. This process is in an infinite loop. However, there is a counter in the loop, and when the counter % 4 == 0, then an order light show is displayed. As the counter grows in value, the chance it is divisible by 4 also increases, and therefore the light display becomes primarily orderly. Check out the script.py file for specifics

Now, the animation. The animation is purely random. I started off with a processing example that generates random coordinate points based on a Brownian motion model and connects each proceeding point resulting in a random figure being drawn. I added upon this by changing the algorithm to create two random Brownian models and the lines move away towards each other in this mesmerizing random dance. In addition, I made the background a random sequence of random colors. So, the animation is totally random in every sense of the word.


Helpful Tutorial:
The project was based off of the following tutorial. 
https://learn.adafruit.com/neopixels-on-raspberry-pi

