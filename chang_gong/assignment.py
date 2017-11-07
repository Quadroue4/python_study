import RPi.GPIO as GPIO
import time

# =======================================================================
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    MotorLeft_A = 12
    MotorLeft_B = 11
    MotorLeft_PWM = 35
    MotorRight_A = 15
    MotorRight_B = 13
    MotorRight_PWM = 37

    trig = 33
    echo = 31

    otd = 16
    otb = 18
    ota = 22
    otc = 40
    ote = 32


    GPIO.setup(MotorLeft_A, GPIO.OUT)
    GPIO.setup(MotorLeft_B, GPIO.OUT)
    GPIO.setup(MotorLeft_PWM, GPIO.OUT)
    GPIO.setup(MotorRight_A, GPIO.OUT)
    GPIO.setup(MotorRight_B, GPIO.OUT)
    GPIO.setup(MotorRight_PWM, GPIO.OUT)

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.setup(otd, GPIO.IN)
    GPIO.setup(otb, GPIO.IN)
    GPIO.setup(ota, GPIO.IN)
    GPIO.setup(otc, GPIO.IN)
    GPIO.setup(ote, GPIO.IN)


    LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
    RightPwm = GPIO.PWM(MotorRight_PWM, 100)

    LeftPwm.start(0)
    RightPwm.start(0)


# ===========================================================================
# Move
# ===========================================================================

def leftmotor(speed):
    if speed > 0:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
        GPIO.output(MotorLeft_PWM, GPIO.HIGH)
        LeftPwm.ChangeDutyCycle(speed)
    elif speed < 0:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
        GPIO.output(MotorLeft_PWM, GPIO.HIGH)
        LeftPwm.ChangeDutyCycle(-speed)
    else: # speed == 0
        leftstop()


def rightmotor(speed):
    if speed > 0:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
        GPIO.output(MotorRight_PWM, GPIO.HIGH)
        RightPwm.ChangeDutyCycle(speed)
    elif speed < 0:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
        GPIO.output(MotorRight_PWM, GPIO.HIGH)
        RightPwm.ChangeDutyCycle(-speed)
    else: # speed == 0
        rightstop()


def move(leftspd, rightspd, time = -1):
    leftmotor(leftspd)
    rightmotor(rightspd)

    if time > 0:
        time.sleep(time)
        stop()


def leftstop():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)


def rightstop():
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    RightPwm.ChangeDutyCycle(0)


def stop():
    leftstop()
    rightstop()

# ===========================================================================
# Get Data
# ===========================================================================

def getDistance():
    GPIO.output(trig, False)
    time.sleep(0.5)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        pulse_start = time.time()
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    dis = pulse_duration * 17000
    dis = round(dis, 2)
    return dis



# ===========================================================================
# Main
# ===========================================================================

if __name__ == '__main__':
    try:
        setup()
        while True:
            ot_list = [otd, otb, ota, otc, ote]
            dis = getDistance()
            print(ot_list)
            print(dis)
            #linetracing()
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()
