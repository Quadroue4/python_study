from raspcar import *

def linetracing():
    dis = 1
    pwm = 50
    dif = 30
    while True:
        count = 0
        if getDistance() > dis:
            sensor = getSensor()  # 0 : black 1 : white
            if not sensor[0]:
                while sensor[2]:
                    move(pwm - dif, pwm + dif, 0)
            elif not sensor[4]:
                while sensor[2]:
                    move(pwm + dif, pwm - dif, 0)
            else:
                sensor[1] - sensor[3]
        else:
            move(0, 0, 1)
            avoid()
            while getSensor[3] == 0:
                move(pwm, pwm, 1)
            while getSensor[2] == 0:
                move(pwm, 0, 1)


def avoid():
    pwm = 70
    t = 0.5
    move(pwm, -pwm, t)
    move(pwm, pwm, 1)
    move(-pwm, pwm, 2*t)
    #move(pwm, pwm, 1)


if __name__ == '__main__':
    try:
        setup()
        while True:
            linetracing()
    except KeyboardInterrupt:
        move(0, 0, 0)
        GPIO.cleanup()
