# utils/action_utils.py
import time
import pyautogui
from config_settings import stop_script, resp_coords
from utils.image_utils import locate_image

def cheme(example):
    example_image = None
    while not example_image:
        if stop_script:
            return False
        example_image = locate_image(example)
        if example_image:
            pyautogui.click(example_image)
            break

def is_near_resp(x, y, resp_coords, radius=10):
    if resp_coords is None:
        return False
    resp_x, resp_y = resp_coords
    distance_squared = (x - resp_x) ** 2 + (y - resp_y) ** 2
    return distance_squared <= radius ** 2