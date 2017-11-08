from raspcar.py import setup, getDistance, getSensor, move

def linetracing:
    dis = 20
    pwm = 70
    dif = 10
    while True:
        count = 0
        if getDistance() > dis:
            sensor = getSensor()
            arrow = sensor[0] + sensor[1] - sensor[3] - sensor[4]
            if arrow > 0:
                move(pwm, pwm+dif)
            elif arrow < 0:
                move(pwm+dif, pwm)
            else:
                move(pwm, pwm)
        else:
            move(0, 0, 1)
            avoid()
            while getSensor[3] == 0:
                move(pwm, pwm)
            while getSensor[2] == 0:
                move(pwm, 0)


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
        move(0, 0)
        GPIO.cleanup()
