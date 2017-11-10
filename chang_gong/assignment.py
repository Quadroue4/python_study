from raspcar import move, getDistance_start, getDistance_end, getSensor, setup
import RPI.GPIO as GPIO
import time

32
def linetracing():
    spd = 50
    dif = 20
    current_dis = 100
    standard_dis = 30
    while True:
        sensor = getSensor()
        if current_dis <= standard_dis:
            avoid()
            current_dis = 100
        # =============== getDistance ===============
        if start_time == 0:
            start_time = time.time()
            getDistance_start()
        if time.time() - start_time > 0.5:
            current_dis = getDistance_end()
            start_time = 0
        # =============== getDistance ===============

        # Move (0 : black, 1 : white)
        if sensor == [0, 0, 0, 0, 0]:  # detect finish line
            move(0, 0)
            break
        elif not sensor[2] and sensor[0] and sensor[4]:  # [1 x 0 x 1]
            move(spd, spd)
        elif not sensor[1]:  # [x 0 x x x]
            move(spd, spd + dif)
        elif not sensor[3]:  # [x x x 0 x]
            move(spd + dif, spd)
        elif not sensor[0]:  # [0 x x x x]
            move(10, spd + dif)
        elif not sensor[4]:  # [x x x x 0]
            move(spd + dif, 10)
        else:
            move(-spd, -spd, 1)
            move(spd, 0)


def avoid():
    spd = 70
    turn_time = 0.5
    move(0, 0, 1)
    move(spd, 0, turn_time)
    move(spd, spd, 1)
    move(40, spd)
    while getSensor()[2] == 1:
        continue


if __name__ == '__main__':
    try:
        setup()
        linetracing()
    except KeyboardInterrupt:
        move(0, 0, 0)
        GPIO.cleanup()
