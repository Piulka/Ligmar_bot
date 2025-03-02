import pyautogui
from pynput import keyboard
from PIL import ImageGrab

def on_press(key):
    try:
        if key == keyboard.Key.enter:
            # Получаем текущие координаты курсора
            x, y = pyautogui.position()
            
            # Делаем скриншот экрана
            screenshot = ImageGrab.grab()
            
            # Получаем цвет пикселя по координатам курсора
            pixel_color = screenshot.getpixel((x, y))
            
            # Выводим координаты и цвет пикселя
            print(f"Координаты курсора: ({x}, {y})")
            print(f"Цвет пикселя (RGBA): {pixel_color}")
        elif key == keyboard.Key.esc:
            print("Выход из программы.")
            return False  # Останавливаем слушатель
    except AttributeError:
        pass

print("Нажмите Enter, чтобы вывести цвет пикселя под курсором. Для выхода нажмите Esc.")

# Запуск слушателя клавиатуры
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()