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

def main_loop():
    global stop_script
    if not attack_mob('1_mob'):
        if not attack_mob('2_mob'):
            if not attack_mob('epic_mob'):
                time.sleep(0.1)
    return True

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