#from gpiozero import LED
import RPi.GPIO as GPIO
import time

#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

num = 0

try:
    time.sleep(2)
    while True:
        if GPIO.input(23):
            #GPIO.output(24, True)
            time.sleep(0.5)
            #GPIO.output(24, False)
            num += 1
            print(num)
            time.sleep(5)
        time.sleep(0.1)
except:
    GPIO.cleanup()
    print("No")

#while True:
#    GPIO.output(24, True)
#    time.sleep(0.5)
#    GPIO.output(24, False)
#    print("BLah")
#    time.sleep(5)
