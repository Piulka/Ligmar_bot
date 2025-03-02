# utils/image_utils.py
import pyautogui
from PIL import ImageGrab

def locate_image(image_path, confidence=0.9):
    try:
        full_path = f"/Users/piul/Scripts/Ligmar_bot/images/{image_path}.png"
        location = pyautogui.locateOnScreen(full_path, confidence=confidence)
        if location:
            return (
                (location.left + location.width // 2) // 2,
                (location.top + location.height // 2) // 2
            )
        else:
            return None
    except pyautogui.ImageNotFoundException:
        return None

def find_pixel_color(target_color):
    screenshot = ImageGrab.grab()
    pixels = screenshot.load()

    for y in range(screenshot.height):
        for x in range(screenshot.width):
            r, g, b = pixels[x, y][:3] 
            if (r, g, b) == target_color:
                return x, y
    return None