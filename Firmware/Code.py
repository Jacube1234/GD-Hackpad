print("Starting")

import board

from kmk.extensions.RGB import RGB
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.pins = (board.GP8,board.GP9,board.GP10,board.GP11)

rgb = RGB(pixel_pin=board.GP1, num_pixels=2)
keyboard.extensions.append(rgb)

keyboard.keymap = [
    [KC.UP, KC.DOWN, KC.LEFT, KC.RIGHT]
]

if __name__ == '__main__':
    keyboard.go()