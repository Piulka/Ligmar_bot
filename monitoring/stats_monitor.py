# monitoring/stats_monitor.py
import time
from rich.live import Live
from config_settings import stop_script
from utils.table_utils import generate_table

def update_table(live):
    while not stop_script:
        live.update(generate_table())
        time.sleep(1)