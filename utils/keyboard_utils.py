# utils/keyboard_utils.py
from pynput import keyboard
from config_settings import stop_script, cmd_pressed, shift_pressed

def on_press(key):
    global stop_script, cmd_pressed, shift_pressed

    if key == keyboard.Key.cmd:
        cmd_pressed = True
    elif key == keyboard.Key.shift:
        shift_pressed = True
    if cmd_pressed and shift_pressed:
        stop_script = True
        print("Скрипт прерван по нажатию на cmd+shift")
        return False