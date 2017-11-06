import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

def REVERSE(x):
    return not x

forward = True
backward = REVERSE(forward)

# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37

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
        sleep(time)
        stop()


# =======================================================================
GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)
GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# =======================================================================
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


# =======================================================================
def leftstop():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)


def rightstop():
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    RightPwm.ChangeDutyCycle(0)


def stop():
    leftstop()
    rightstop()


def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)


def pwm_low():
    stop()
    GPIO.cleanup()

