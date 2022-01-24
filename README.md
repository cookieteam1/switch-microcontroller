# nintendo switch controller arduino

control your Nintendo Switch using a pro micro

## requirements

- [pro micro] (or compatible)
- [ftdi usb to uart] (or other uart device)
- usb cables (both use [micro usb])
- wires

[pro micro]: https://amzn.to/3rpb36r
[ftdi usb to uart]: https://amzn.to/3dRWML0
[micro usb]: https://amzn.to/2NVK4ll

## installation

```bash
sudo apt install avrdude gcc-avr avr-libc dfu-programmer
```

## assembly

the assembly is fairly straightforward, here is a rough diagram of the parts
and how they will be hooked up when operating

```
                        [your computer]
                            |
          +===========+     |
          | (ftdi)    |-----+ (usb cable)
          | gnd tx rx |
          +==-===-==-=+
             |   |  |
 +======+    |   |  |
 |buzzer|    |   |  |
 +======+    |   |  |  wires (note: tx matches with rx (crossed))
     |  |    |   |  |
    +-==-====-===-==-==+
    |9  gnd  gnd rx tx |-------------+  (usb cable)
    |     (pro micro)  |             |
    +==================+        [nintendo switch]

```

my assembly (I have a button from rst to gnd to help flashing)

![](https://user-images.githubusercontent.com/1810591/114293095-2ab8a980-9a48-11eb-9b35-290d58786701.jpg)

## building

```bash
make MCU=atmega32u4
```

use the appropriate `MCU` for your board, the pro micro uses `atmega32u4`

## flashing

you have to be quick with this!

- connect the pro micro to your computer
- short `rst` to `gnd` twice in quick succession

```bash
sudo avrdude -v -patmega32u4 -cavr109 -P/dev/ttyACM0 -Uflash:w:output.hex
```

use the appropriate `MCU` and serial port for your board, the pro micro uses
`atmega32u4` and `/dev/ttyACM0`

## usage

to use the controller:
- start the game you want to play
- press home
- navigate to controllers
- change order/grip
- at this point, connect the controller (it should register itself and start
  the game)

at this point, you can control the controller using uart

commands are single-byte ascii characters sent over 9600 baud serial.

this is the current list of commands:

```
V: enable verbose mode (microcontroller will reply with `revc: _`)
v: disable verbose mode

!: enable output on pin 9 (buzzer)
.: disable output on pin 9

0: empty state (no buttons pressed)
A: A is pressed
B: B is pressed
X: X is pressed
Y: Y is pressed
H: Home is pressed
+: + is pressed
-: - is pressed
L: left trigger is pressed
R: right trigger is pressed
l: ZL is pressed
r: ZR is pressed

directions:
left stick

      w
   q     e
      ║
a  ═══╬═══  d
      ║
   z     c
      s

left stick

      u
   y     i
      ║
h  ═══╬═══  k
      ║
   n     m
      j

```

## thanks

Thanks to Shiny Quagsire for his [Splatoon post printer](https://github.com/shinyquagsire23/Switch-Fightstick) and progmem for his [original discovery](https://github.com/progmem/Switch-Fightstick).
Also thanks to bertrandom for his [snowball thrower](https://github.com/bertrandom/snowball-thrower) and all the modifications.
Also thanks to asottile for his [switchcontoller](https://github.com/asottile/switch-microcontroller) for the base code and example scripts.