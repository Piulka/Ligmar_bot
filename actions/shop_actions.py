# actions/shop_actions.py
import time
from config_settings import activity_count
from utils.action_utils import cheme

def sell_items():
    cheme('village')
    cheme('builds')
    cheme('shop')
    cheme('sell_all')
    cheme('sell')
    activity_count["shop_visits"] += 1
    cheme('village')
    time.sleep(0.5)