print("Starting")

import board

from kmk.extensions.RGB import RGB
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.pins = (board.D7,board.D8,board.D9,board.D10)

rgb = RGB(pixel_pin=board.D0, num_pixels=2)
keyboard.extensions.append(rgb)

keyboard.keymap = [
    [KC.UP, KC.DOWN, KC.LEFT, KC.RIGHT]
]

if __name__ == '__main__':
    keyboard.go()