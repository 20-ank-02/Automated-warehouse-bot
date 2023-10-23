
import RPi.GPIO as GPIO
import time


class Connection:
    def __init__(self) -> None:

        #------------------ Set up GPIO ------------------
        #Nema23
        GPIO.setmode(GPIO.BCM)
        self.dir_pin23z = 21        # pin 40
        self.pul_pin23z = 20        # pin 38

        GPIO.setup(self.dir_pin23z, GPIO.OUT)
        GPIO.setup(self.pul_pin23z, GPIO.OUT)

        #Nema17 x
        self.dir_pin17x = 23       # pin 16
        self.pul_pin17x = 12       # pin 32
        GPIO.setup(self.dir_pin17x, GPIO.OUT)
        GPIO.setup(self.pul_pin17x, GPIO.OUT)

        #Nema17 y
        self.dir_pin17y =14    #pin8
        self.pul_pin17y =15    #pin10
        GPIO.setup(self.dir_pin17y, GPIO.OUT)
        
                #Ultrasonic sensor
        self.GPIO_TRIGGER = 18  #pin12
        self.GPIO_ECHO = 24     #pin18

        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

        #valve

        #rotateFlip
        self.flip= 16      #pin36
        self.rotate= 7    #pin26
        GPIO.setup(self.flip, GPIO.OUT)
        GPIO.setup(self.rotate, GPIO.OUT)
        pwm_frequency = 50
        pwmF = GPIO.PWM(self.flip, pwm_frequency)
        pwmR = GPIO.PWM(self.rotate, pwm_frequency)

        pwmF.start(0)
        pwmR.start(0)
        #--------------------------------------------------
        
    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance
    def rotateFlip(self, action):
        if action == 'rotate':
            pwmR.ChangeDutyCycle(7.5)
            time.sleep(1)  # Allow time for the servo to move


        if action == 'flip':
            pwmF.ChangeDutyCycle(7.5)
            time.sleep(1)

        if action == 'initial':
            pwmF.start(0)
            pwmR.start(0)
        
        pwmR.stop()
        pwmF.stop()

    # dir = 1 is clockwise
    # dir = 0 is anti-clockwise