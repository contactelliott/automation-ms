import threading
from maplestory_telemetry import *
import time
import pyautogui

last_hp_percentage = -1.0
last_mp_percentage = -1.0
last_char_position = -1

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
    global last_hp_percentage
    while True:

        time.sleep(1.5)
def start_bot():


def start_processes():
    telemetry_thread = threading.Thread(target=update_telemetry)
    telemetry_thread.start()

    print_telemetry_thread = threading.Thread(target=print_telemetry)
    print_telemetry_thread.start()

def print_telemetry():
    global last_hp_percentage, last_mp_percentage, last_char_position
    while True:
        print("HP Percentage:", int(last_hp_percentage), " MP Percentage:", int(last_mp_percentage), " Char Position:", int(last_char_position))
        time.sleep(5)

start_processes()