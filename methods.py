import numpy
import serial
import time
import cv2

def _press(ser: serial.Serial, s: str, duration: float = .1) -> None:
    print(f'{s=} {duration=}')
    ser.write(s.encode())
    time.sleep(duration)
    ser.write(b'0')
    time.sleep(.075)


def _getframe(vid: cv2.VideoCapture) -> numpy.ndarray:
    _, frame = vid.read()
    cv2.imshow('game', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        raise SystemExit(0)
    return frame


def _wait_and_render(vid: cv2.VideoCapture, t: float) -> None:
    end = time.time() + t
    while time.time() < end:
        _getframe(vid)


def _alarm(ser: serial.Serial, vid: cv2.VideoCapture) -> None:
    while True:
        ser.write(b'!')
        _wait_and_render(vid, .5)
        ser.write(b'.')
        _wait_and_render(vid, .5)


def _await_pixel(
        ser: serial.Serial,
        vid: cv2.VideoCapture,
        *,
        x: int,
        y: int,
        pixel,
        timeout: float = 90,
) -> None:
    end = time.time() + timeout
    frame = _getframe(vid)
    while not numpy.array_equal(frame[y][x], pixel):
        frame = _getframe(vid)
        if time.time() > end:
            _alarm(ser, vid)

def _await_channel_value(
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
    frame = _getframe(vid)
    while not frame[y][x][ch]== val:
        frame = _getframe(vid)
        if time.time() > end:
            _alarm(ser, vid)


def _await_not_pixel(
        ser: serial.Serial,
        vid: cv2.VideoCapture,
        *,
        x: int,
        y: int,
        pixel,
        timeout: float = 90,
) -> None:
    end = time.time() + timeout
    frame = _getframe(vid)
    while numpy.array_equal(frame[y][x], pixel):
        frame = _getframe(vid)
        if time.time() > end:
            _alarm(ser, vid)