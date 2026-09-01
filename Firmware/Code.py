print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# 1. Enable media tracking so the mute button can communicate safely
keyboard.extensions.append(MediaKeys())

# 2. Add your 4 switches AND your Encoder Click (D4) directly to the single scanner list
keyboard.matrix = KeysScanner(
    pins=[board.D7, board.D8, board.D9, board.D10, board.D4],
    value_when_pressed=False,
    pull=True,
)

# 3. Simple keymap matching the 5 physical button contacts sequentially
keyboard.keymap = [
    [KC.W, KC.S, KC.A, KC.D, KC.MUTE]
]

if __name__ == '__main__':
    keyboard.go()
