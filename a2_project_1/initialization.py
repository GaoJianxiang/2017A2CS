# intialize GPIO on raspberry pi
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
          m=GPIO.input(3)
          n=GPIO.input(16)
          if m==0:
               print("Obstacle detected on Left", m)
               time.sleep(0.1)
          elif n==0:
               print("Obstacle detected on Right", n)
               time.sleep(0.1)
