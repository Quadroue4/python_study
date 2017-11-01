######################################################################
### Date: 2017/10/5
### file name: go_any.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to go forward or backward without time limit
######################################################################

# import GPIO library
import RPi.GPIO as GPIO

from time import sleep

# set GPIO warnings as flase
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)


# =======================================================================
# REVERSE function to control the direction of motor in reverse
# =======================================================================
def REVERSE(x):
    return not x

# =======================================================================
# Set the motor's true / false value to go forward.
# =======================================================================
forward = True
backward = REVERSE(forward)

# =======================================================================
# Set the pin
#  =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


def leftmotor(direction, speed):
    if direction:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    else:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)


def rightmotor(direction, speed):
    if direction:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    else:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    RightPwm.ChangeDutyCycle(speed)


# =======================================================================
# because the connetions between motors (left motor) and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

# =======================================================================
# because the connetions between motors (right motor) and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
# =======================================================================
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)

# =======================================================================
# create right pwm object to control the speed of right motor
# =======================================================================
RightPwm = GPIO.PWM(MotorRight_PWM, 100)

def move(key, status):
    if key == 'w':
        leftmotor(forward, 30)
        rightmotor(forward, 30)
        status = 1
    elif key == 's':
        leftmotor(backward, 30)
        rightmotor(backward, 30)
        status = -1
    elif key == 'a':
        leftmotor(backward, 70)
        rightmotor(forward, 70)
        sleep(0.2)
        if status == 1:
            move('w', status)
        elif status == -1:
            move('s', status)
        else:
            stop()
    elif key == 'd':
        leftmotor(forward, 70)
        rightmotor(backward, 70)
        sleep(0.2)
        if status == 1:
            move('w', status)
        elif status == -1:
            move('s', status)
        else:
            stop()
    elif key == 'f':
        stop()
        status = 0
    return status


# =======================================================================
# define the stop module
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
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()


pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
dis = 17  # ??
obstacle = 1

# when obstacle=1, the power and
# running time of the first turn
spd = 0

try:
    key = ''
    status = 0
    while key != 'exit':
        key = raw_input("move key : ")
        status = move(key, status)
    stop()


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
