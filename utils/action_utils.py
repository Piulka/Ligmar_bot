# utils/action_utils.py
import time
import pyautogui
from config_settings import stop_script, resp_coords
from utils.image_utils import locate_image

def cheme(example, dx=0, dy=0):
    example_image = None
    while not example_image:
        if stop_script:
            return False
        example_image = locate_image(example)
        if example_image:
            x, y = example_image
            pyautogui.click(x + dx, y + dy)
            break

def is_near_resp(x, y, resp_coords, radius=10):
    if resp_coords is None:
        return False
    resp_x, resp_y = resp_coords
    distance_squared = (x - resp_x) ** 2 + (y - resp_y) ** 2
    return distance_squared <= radius ** 2

def cheme2(example, timeout=2):
    start_time = time.time()
    example_image = None  
    while time.time() - start_time < timeout:
        if stop_script:
            return False
        example_image = locate_image(example)
        if example_image:
            pyautogui.click(example_image)
            return True
        time.sleep(0.1)
    return False 