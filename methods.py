from __future__ import annotations
import numpy
import serial
import time
import cv2
import contextlib
from typing import Generator

def press(ser: serial.Serial, s: str, duration: float = .1, d: bool = False) -> None:
    if d:
        print(f'{s=} {duration=}')
    ser.write(s.encode())
    time.sleep(duration)
    ser.write(b'0')
    time.sleep(.075)


def getframe(vid: cv2.VideoCapture) -> numpy.ndarray:
    _, frame = vid.read()
    cv2.imshow('game', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        raise SystemExit(0)
    return frame


def wait_and_render(vid: cv2.VideoCapture, t: float) -> None:
    end = time.time() + t
    while time.time() < end:
        getframe(vid)


def alarm(ser: serial.Serial, vid: cv2.VideoCapture) -> None:
    while True:
        ser.write(b'!')
        wait_and_render(vid, .5)
        ser.write(b'.')
        wait_and_render(vid, .5)


def await_pixel(
        ser: serial.Serial,
        vid: cv2.VideoCapture,
        *,
        x: int,
        y: int,
        pixel: tuple[ int, int, int],
        timeout: float = 90,
) -> None:
    end = time.time() + timeout
    frame = getframe(vid)
    while not numpy.array_equal(frame[y][x], pixel):
        frame = getframe(vid)
        if time.time() > end:
            alarm(ser, vid)

def await_channel_value(
        ser: serial.Serial,
        vid: cv2.VideoCapture,
        *,
        x: int,
        y: int,
        val: int,
        ch: int,
        timeout: float = 90,
) -> None:
    end = time.time() + timeout
    frame = getframe(vid)
    while not frame[y][x][ch]== val:
        frame = getframe(vid)
        if time.time() > end:
            alarm(ser, vid)


def await_not_pixel(
        ser: serial.Serial,
        vid: cv2.VideoCapture,
        *,
        x: int,
        y: int,
        pixel: tuple[ int, int, int],
        timeout: float = 90,
) -> None:
    end = time.time() + timeout
    frame = getframe(vid)
    while numpy.array_equal(frame[y][x], pixel):
        frame = getframe(vid)
        if time.time() > end:
            alarm(ser, vid)

@contextlib.contextmanager
def shh(ser: serial.Serial) -> Generator[None, None, None]:
    try:
        yield
    finally:
        ser.write(b'.')