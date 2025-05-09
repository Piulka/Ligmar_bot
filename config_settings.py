# config.py
from datetime import datetime

# Глобальные переменные
stop_script = False
cmd_pressed = False
shift_pressed = False
resp_coords = None

# Счетчики активности
activity_count = {
    "altar": 0,
    "chest": 0,
    "1_mob": 0,
    "2_mob": 0,
    "epic_mob": 0,
    "epic_items": 0,
    "total_mobs": 0,
    "shop_visits": 0
}
death_count = 0
start_time = datetime.now()