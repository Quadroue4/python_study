import RPi.GPIO as GPIO
import time

# =======================================================================
# Setup
# =======================================================================

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    global MotorLeft_A, MotorLeft_B, MotorLeft_PWM
    global MotorRight_A, MotorRight_B, MotorRight_PWM 
    MotorLeft_A = 12
    MotorLeft_B = 11
    MotorLeft_PWM = 35
    MotorRight_A = 15
    MotorRight_B = 13
    MotorRight_PWM = 37

    global trig, echo
    trig = 33
    echo = 31

    global otd, otb, ota, otc, ote
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

    global LeftPwm, RightPwm
    LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
    RightPwm = GPIO.PWM(MotorRight_PWM, 100)

    LeftPwm.start(0)
    RightPwm.start(0)


# ===========================================================================
# Move / left(right)motor(spd), move(lspd, rspd, t), (left/right)stop()
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


def move(leftspd, rightspd, t=-1):
    leftmotor(leftspd)
    rightmotor(rightspd)

    if t > 0:
        time.sleep(t)
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
# Get Data / getDistance(), getSensor()
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


def getSensor():
    res = [GPIO.input(otd),
           GPIO.input(otb),
           GPIO.input(ota),
           GPIO.input(otc),
           GPIO.input(ote)]
    return res


# ===========================================================================
# Main
# ===========================================================================

if __name__ == '__main__':
    try:
        setup()
        while True:
            ot_list = getSensor()
            dis = getDistance()
            print(ot_list)
            print(dis)
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()
