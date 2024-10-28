import threading
from maplestory_telemetry import *
import time
import pyautogui
import numpy as np


last_hp_percentage = -1.0
last_mp_percentage = -1.0
last_char_position = -1
curr_direction = 'right'

def pressKey(key, duration=0.0):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def update_hp_percentage():
    global last_hp_percentage
    while True:
        last_hp_percentage = get_hp_percentage()
        time.sleep(1.5)

def update_mp_percentage():
    global last_mp_percentage
    while True:
        last_mp_percentage = get_mp_percentage()
        time.sleep(1.5)

def update_char_position():
    global last_char_position
    while True:
        last_char_position = get_char_x_map_position()
        time.sleep(1.5)

def update_telemetry():
    update_hp_thread = threading.Thread(target=update_hp_percentage)
    update_hp_thread.start()

    update_mp_thread = threading.Thread(target=update_mp_percentage)
    update_mp_thread.start()

    update_char_position_thread = threading.Thread(target=update_char_position)
    update_char_position_thread.start()

def hp_pot_bot():
    global last_hp_percentage, hp_threshold, hp_key
    while True:
        if last_hp_percentage <= hp_threshold:
            pressKey(hp_key)
        time.sleep(1.5)

def mp_pot_bot():
    global last_mp_percentage, mp_threshold, mp_key
    while True:
        if last_mp_percentage <= mp_threshold:
            pressKey(mp_key)
        time.sleep(1.5)

def navigate():
    global curr_direction
    if curr_direction == 'right' and last_char_position > right_boundary:
        curr_direction = 'left'
        return
    elif curr_direction == 'left' and last_char_position < left_boundary:
        curr_direction = 'right'
        return
    pressKey(curr_direction, movement_duration)

def attack():
    global attack_key
    sample = np.random.binomial(num_trials, prob_success)
    for i in range (0, min_attacks + sample):
        pressKey(attack_key,.25)


def navigate_attack():
    global last_char_position
    while True:
        for i in range(0, interval_per_cycle):
            attack()
            navigate()
            attack()



def start_bot():
    hp_pot_bot_thread = threading.Thread(target=hp_pot_bot)
    hp_pot_bot_thread.start()

    mp_pot_bot_thread = threading.Thread(target=mp_pot_bot)
    mp_pot_bot_thread.start()

    navigate_attack_thread = threading.Thread(target=navigate_attack)
    navigate_attack_thread.start()


def start_processes():
    telemetry_thread = threading.Thread(target=update_telemetry)
    telemetry_thread.start()

    start_bot_thread = threading.Thread(target=start_bot)
    start_bot_thread.start()

    print_telemetry_thread = threading.Thread(target=print_telemetry)
    print_telemetry_thread.start()

def print_telemetry():
    global last_hp_percentage, last_mp_percentage, last_char_position
    while True:
        print("HP Percentage:", int(last_hp_percentage), " MP Percentage:", int(last_mp_percentage), " Char Position:", int(last_char_position))
        time.sleep(5)

start_processes()