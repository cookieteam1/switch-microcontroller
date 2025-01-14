from __future__ import annotations
import argparse
import sys
from methods import *
import serial
import cv2

SERIAL_DEFAULT = 'COM1' if sys.platform == 'win32' else '/dev/ttyUSB0'

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--serial', default=SERIAL_DEFAULT, type=str)
    parser.add_argument('--baud', default=9600, type=int)#opencv frame height
    parser.add_argument('--camera', default=0, type=int)
    parser.add_argument('--camAPI', default=0, type=int)#opencv videocapture api
    parser.add_argument('--frameW', default=640, type=int)#opencv frame width
    parser.add_argument('--frameH', default=480, type=int)#opencv frame height
    args = parser.parse_args()

    vid = cv2.VideoCapture(args.camera,args.camAPI)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, args.frameW)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, args.frameH)

    with serial.Serial(args.serial, args.baud) as ser, shh(ser):
        while True:
            pass #Here could be your code
    
    vid.release()
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    exit(main())