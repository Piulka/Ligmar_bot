# actions/mob_actions.py
import time
import pyautogui
from config_settings import stop_script, activity_count, resp_coords
from utils.image_utils import locate_image, find_pixel_color
from utils.action_utils import cheme, is_near_resp 
from actions.skill_actions import use_skills_until_enemy_count

def attack_mob(mob_name):
    global stop_script, activity_count, resp_coords

    mob_image = locate_image(mob_name, confidence=0.99)
    if mob_image:
        if stop_script:
            return False
        x, y = mob_image

        if is_near_resp(x, y, resp_coords):
            return False

        pyautogui.click(mob_image)
        activity_count[mob_name] += 1
        if mob_name == "1_mob":
            activity_count["total_mobs"] += 1
        elif mob_name == "2_mob":
            activity_count["total_mobs"] += 2
        cheme('go_to')
        time.sleep(4)
        cheme('close_2')
        use_skills_until_enemy_count()
        cheme('go_to_map')
        cheme('go_to_map')

        full_bp = locate_image('full_bp')
        if full_bp:
            if stop_script:
                return False
            portal = locate_image('portal')
            pyautogui.click(portal)
            cheme('persona')
            cheme('bp')
            cheme('skip_eq')
            while True:
                item = None
                time.sleep(1)
                pixel_coords = find_pixel_color((44, 12, 92))
                if pixel_coords:
                    item = pixel_coords
                if item:
                    x, y = item
                    x //= 2
                    y //= 2
                    pyautogui.click(x, y)
                    time.sleep(0.2)
                    cheme('to_chest')
                    cheme('skip_window')
                    activity_count["epic_items"] += 1
                else:
                    print("Пиксель цвета (44, 12, 92) не найден.")
                    break
            cheme('village')
            cheme('builds')
            cheme('shop')
            cheme('sell_all')
            cheme('sell')
            activity_count["shop_visits"] += 1
            cheme('village')
            time.sleep(0.5)
            cheme('go_to_fight')
            pyautogui.scroll(-100, x=1285, y=586)
            cheme('location_oldrud')
            time.sleep(1)

        return True
    else:
        return False