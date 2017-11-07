from raspcar.py import setup, getDistance, getSensor
from raspcar.py import move, leftstop, rightstop, stop

def linetracing:
    print()


if __name__ = '__main__':
    try:
        setup()
        while True:
            linetracing()
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()
