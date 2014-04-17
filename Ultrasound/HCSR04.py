#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_TRIG = 17
GPIO_ECHO = 18
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIG, GPIO.LOW)

if __name__ == '__main__':
    try:
        while True:
            time.sleep(3)
            GPIO.output(GPIO_TRIG, True)
            time.sleep(0.00001)
            GPIO.output(GPIO_TRIG, False)
            while GPIO.input(GPIO_ECHO) == 0:
                SIGNALOFF = time.time()
            while GPIO.input(GPIO_ECHO) == 1:
                SIGNALON = time.time()

            D = (SIGNALON - SIGNALOFF) * 17000
            print D

    except KeyboardInterrupt:
        GPIO.cleanup()

