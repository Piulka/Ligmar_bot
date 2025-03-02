import time
import pyautogui
import cv2
import numpy as np

# Определяем пути к изображениям
IMAGE_PATHS = {
    'image': "/Users/piul/Scripts/Ligmar/images/epic_item.png"
}

def check_screen_resolution():
    screen_width, screen_height = pyautogui.size()
    print(f"Текущее разрешение экрана: {screen_width}x{screen_height}")
    
    
def locate_image_on_screen(image_path, confidence=0.8):
    """
    Находит изображение на экране и возвращает его координаты и точность совпадения.
    """
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Загружаем шаблон
    template = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if template is None:
        print(f"Ошибка: не удалось загрузить изображение {image_path}")
        return None, 0

    # Убедимся, что у шаблона и скриншота одинаковые каналы (RGB или RGBA)
    if template.shape[2] == 4:  # Если изображение имеет 4 канала (RGBA), преобразуем в RGB
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
    
    if screenshot.shape[2] == 4:  # Если скриншот имеет 4 канала (RGBA), преобразуем в RGB
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

    # Преобразуем изображения в тип CV_8U
    screenshot = cv2.convertScaleAbs(screenshot)
    template = cv2.convertScaleAbs(template)

    # Получаем размеры шаблона
    w, h = template.shape[:2]

    # Выполняем сопоставление
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= confidence:
        return (max_loc[0] + w // 2, max_loc[1] + h // 2), max_val
    return None, 0

def main():
    screen_width, screen_height = pyautogui.size()
    print(f"Текущее разрешение экрана: {screen_width}x{screen_height}")
    print("Ищу изображения на экране...")
    for image_name, image_path in IMAGE_PATHS.items():
        position, confidence = locate_image_on_screen(image_path)
        if position:
            print(f"Изображение '{image_name}' найдено на координатах {position} с точностью {confidence:.2f}")
        else:
            print(f"Изображение '{image_name}' не найдено на экране")

if __name__ == "__main__":
    main()
