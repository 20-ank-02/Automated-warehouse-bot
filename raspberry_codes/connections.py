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
        self.dir_pin17y = 
        self.pul_pin17y = 
        GPIO.setup(self.dir_pin17y, GPIO.OUT)
        GPIO.setup(self.pul_pin17y, GPIO.OUT)
        
        
        #Ultrasonic sensor
        self.GPIO_TRIGGER = 18
        self.GPIO_ECHO = 24
        
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        
        #valve
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
 


    # dir = 1 is clockwise
    # dir = 0 is anti-clockwise
    def moveZ(self,dir,units):   
        try:
            GPIO.output(self.dir_pin23z, dir) 
            while units :
                # starting pulse with 1
                GPIO.output(self.pul_pin23z,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(self.pul_pin23z,GPIO.LOW)
                time.sleep(0.5)
            
        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C) or other exceptions
            GPIO.cleanup()


    def moveX(self,dir,units):
        try:
            GPIO.output(self.dir_pin17x, dir) 
            while units :
                # starting pulse with 1
                GPIO.output(self.pul_pin17x,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(self.pul_pin17x,GPIO.LOW)
                time.sleep(0.5)
            
        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C) or other exceptions
            GPIO.cleanup()
            
            
    def moveY(self,dir,units):
        try:
            GPIO.output(self.dir_pin17y, dir) 
            while units :
                # starting pulse with 1
                GPIO.output(self.pul_pin17y,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(self.pul_pin17y,GPIO.LOW)
                time.sleep(0.5)

        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C) or other exceptions
            GPIO.cleanup()
           
    def valve(self,condition):
        if condition == 1:
            print('opening valve')
            
        if condition == 0:
            print('closing valve')

    def exitGPIO():
    # Clean up GPIO on program exit
        GPIO.cleanup()
