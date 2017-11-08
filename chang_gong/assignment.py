from raspcar import *
import  threading

def linetracing():
    disthread = threading.Thread(target=getDistance())
    dis = 1
    pwm = 50
    dif = 30
    while True:
        disthread.start()
        sensor = getSensor()
        if dis < distance:
            if sum(sensor) == 0:
                move(0, 0, 0)
                break
            elif sensor[1] and not sensor[2] and sensor[3]: # [x 1 0 1 x]
                move(90, 90, 0)
            elif sensor[0] and not sensor[1] and sensor[2]: # [1 0 1 x x]
                move(50, 70, 0)
            elif not sensor[0]: # [0 x x x x]
                move(0, 50, 0)
            elif sensor[2] and not sensor[3] and sensor[4]:  # [x x 1 0 1]
                move(70, 50, 0)
            elif not sensor[4]:  # [x x x x 0]
                move(50, 0, 0)


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
