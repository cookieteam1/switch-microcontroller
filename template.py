import argparse
import sys
from methods import *
import serial
import cv2

SERIAL_DEFAULT = 'COM1' if sys.platform == 'win32' else '/dev/ttyUSB0'

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--serial', default=SERIAL_DEFAULT)
    parser.add_argument('--camera', default=0)
    parser.add_argument('--camAPI', default=0)#opencv videocapture api
    parser.add_argument('--frameW', default=640)#opencv frame width
    parser.add_argument('--frameH', default=480)#opencv frame height
    args = parser.parse_args()

    vid = cv2.VideoCapture(args.camera,args.camAPI)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, args.frameW)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, args.frameH)

    with serial.Serial(args.serial, 9600) as ser:
        while True:
            pass #Here could be your code


if __name__ == '__main__':
    exit(main())