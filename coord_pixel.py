import pyautogui
from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.Key.enter:
            print(f"Текущие координаты курсора: {pyautogui.position()}")
        elif key == keyboard.Key.esc:
            print("Выход из программы.")
            return False  # Останавливаем слушатель
    except AttributeError:
        pass

print("Нажмите Enter, чтобы вывести координаты курсора. Для выхода нажмите Esc.")

# Запуск слушателя клавиатуры
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    