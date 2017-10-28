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
forward = False

# =======================================================================
# Set the motor's true / false value to go opposite.
# =======================================================================
backward = REVERSE(forward)

# =======================================================================
# declare the pins of 12, 11, 35 in the Rapberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Rapberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled
# =======================================================================
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# ===========================================================================

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


# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  objec to go forward without any limitation of running_time
# =======================================================================

def go_forward_any(speed):
    leftmotor(forward, speed)
    rightmotor(forward, speed)


# =======================================================================
#  go_backward_any method has been generated for the three-wheeled moving
#  object to go backward without any limitation of running_time
# =======================================================================

def go_backward_any(speed):
    leftmotor(backward, speed)
    rightmotor(backward, speed)


# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  object to go forward with the limitation of running_time
# =======================================================================

def go_forward(speed, running_time):
    leftmotor(forward, speed)
    rightmotor(forward, speed)
    if running_time > 0:
        sleep(running_time)
        stop()

# student assignment (6)

# =======================================================================
#  go_backward_any method has been generated for the three-wheeled moving
#  object to go backward with the limitation of running_time
# =======================================================================


def go_backward(speed, running_time):
    leftmotor(forward, speed)
    rightmotor(forward, speed)
    if running_time > 0:
        sleep(running_time)
        stop()


def leftSwingTurn(speed, running_time):
    leftstop()
    rightmotor(forward, speed)
    sleep(running_time)
    stop()


def rightSwingTurn(speed, running_time):
    leftmotor(forward, speed)
    rightstop()
    sleep(running_time)
    stop()


def leftPointTurn(speed, running_time):  # student assignment (1)
    leftmotor(backward, speed)
    rightmotor(forward, speed)
    sleep(running_time)
    stop()


def rightPointTurn(speed, running_time):  # student assignment (1)
    leftmotor(forward, speed)
    rightmotor(backward, speed)
    sleep(running_time)
    stop()


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
