# actions/skill_actions.py
import time
import pyautogui
from config_settings import stop_script, death_count, resp_coords
from utils.image_utils import locate_image
from utils.action_utils import cheme

def use_skills_until_enemy_count():
    global stop_script, death_count, resp_coords

    skills = [('skill_kick'), ('skill_punch')]
    enemy_count = None
    skill_stun = locate_image('skill_stun')
    if skill_stun:
        if stop_script:
            return False
        pyautogui.click(skill_stun)

    while not enemy_count and not stop_script:
        if stop_script:
            return False
        for image_name in skills:
            if skill(image_name):
                continue

        enemy_count = locate_image('enemy_count')
        if enemy_count:
            return True
        to_village = locate_image('to_village')
        if to_village:
            if stop_script:
                return False
            pyautogui.click(to_village)
            time.sleep(0.5)
            cheme('go_to_fight')
            pyautogui.scroll(-100, x=1285, y=586)
            cheme('location_oldrud')
            time.sleep(1)
            death_count += 1

            resp_coords = None
            while not resp_coords and not stop_script:
                resp_coords = locate_image('resp')
                if not resp_coords:
                    time.sleep(1)
            return True
        go_to_fight = locate_image('go_to_fight')    
        if go_to_fight:
            if stop_script:
                return False
            cheme('go_to_fight')
            pyautogui.scroll(-100, x=1285, y=586)
            cheme('location_oldrud')
            time.sleep(1)
            death_count += 1

            resp_coords = None
            while not resp_coords and not stop_script:
                resp_coords = locate_image('resp')
                if not resp_coords:
                    time.sleep(1)
            return True
    return False

def skill(image_name):
    global stop_script

    enemy_count = locate_image('enemy_count')
    if enemy_count:
        return True

    image_location = locate_image(image_name, confidence=0.9)
    if image_location:
        if stop_script:
            return False
        pyautogui.click(image_location)
        time.sleep(0.1)

        no_mana_location = locate_image('no_mana', confidence=0.95)
        if no_mana_location:
            use_mana_location = locate_image('use_mana', confidence=0.8)
            if use_mana_location:
                pyautogui.click(use_mana_location)
                time.sleep(0.1)
            else:
                return True

        my_hp = locate_image('my_hp', confidence=0.95)

        if my_hp:
            return True
        else:
            use_hp_location = locate_image('use_hp', confidence=0.8)
            skill_heal = locate_image('skill_heal')

            if use_hp_location:
                pyautogui.click(use_hp_location)
                time.sleep(0.1)

            if skill_heal:
                pyautogui.click(skill_heal)
    else:
        return False