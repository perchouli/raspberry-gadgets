#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_CHANNEL = 27
GPIO.setup(GPIO_CHANNEL, GPIO.IN)

if __name__ == '__main__':
    try:
        while True:
            if GPIO.input(GPIO_CHANNEL) == 1:
                print "DETECTED!"
                time.sleep(5)
            else:
                time.sleep(0.2)

    except KeyboardInterrupt:
        GPIO.cleanup()

