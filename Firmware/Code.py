print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# 1. Enable Media Keys for volume control
keyboard.extensions.append(MediaKeys())

# 2. Rotary Encoder setup (Rotation on D1 & D2)
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D1, board.D2),)
encoder_handler.map = [
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN),)
]
keyboard.modules.append(encoder_handler)

# 3. Matrix Scanner: WASD/Arrows (D7, D8, D9, D10) + Encoder Click (D3)
keyboard.matrix = KeysScanner(
    pins=[board.D7, board.D8, board.D9, board.D10, board.D3],
    value_when_pressed=False,
    pull=True,
)

# 4. Keymap: Arrow keys + Mute on encoder click
keyboard.keymap = [
    [KC.UP, KC.DOWN, KC.LEFT, KC.RIGHT, KC.MUTE]
]

if __name__ == '__main__':
    keyboard.go()