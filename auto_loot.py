#!/usr/bin/env python3

from pynput.mouse import Button, Controller as mouse_controller
from pynput.keyboard import Key, Controller as keyboard_controller
import random
import time

mouse = mouse_controller()
keyboard = keyboard_controller()

positions = [
    (3179, 488),
    (3299, 502),
    (3287, 605),
    (3296, 684),
    (3186, 704),
    (3081, 693),
    (3082, 583),
    (3082, 475),
    (3195, 588)
]

def pick_loot_around():
    original_position = mouse.position

    for i in positions:
        mouse.position = i
        time.sleep(random.randint(11, 22) / 1000.0)

        with keyboard.pressed(Key.shift):
            mouse.press(Button.right)
            mouse.release(Button.right)
            time.sleep(random.randint(11, 22) / 1000.0)
        
    mouse.position = original_position

if (__name__ == "__main__"):
    pick_loot_around()
