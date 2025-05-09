# main.py
import sys
import os

# Добавляем текущую директорию в sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import time
import threading
from pynput import keyboard
from rich.console import Console
from rich.live import Live
from config_settings import stop_script
from utils.keyboard_utils import on_press
from monitoring.stats_monitor import update_table
from actions.mob_actions import attack_mob
from utils.image_utils import locate_image

def main_loop():
    global stop_script
    targets = ['epic_mob', 'chest', 'altar', '1_mob', '2_mob']
    forbidden_center = None
    
    while not stop_script:
        # Обновляем центр запретной зоны
        if go_to_map_pos := locate_image('go_to_map'):
            forbidden_center = (go_to_map_pos[0], go_to_map_pos[1] - 220)
        
        target_found = False
        for target in targets:
            if mob_pos := locate_image(target):
                x, y = mob_pos
                # Пропускаем если в запретной зоне
                if forbidden_center and (x-forbidden_center[0])**2 + (y-forbidden_center[1])**2 <= 400:  # 20^2
                    continue
                if attack_mob(target):
                    target_found = True
                    break
        
        if not target_found:
            print("Цели не найдены. Повторная проверка...")
            time.sleep(0.5)

if __name__ == "__main__":
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    console = Console()
    with Live(console=console, refresh_per_second=4) as live:
        threading.Thread(target=update_table, args=(live,), daemon=True).start()

        while not stop_script:
            main_loop()
            time.sleep(0.1)

    listener.stop()