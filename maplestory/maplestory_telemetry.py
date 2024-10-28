from eds_config import *
import pyautogui
import numpy as np

def get_hp_percentage():
    hp_bar = pyautogui.screenshot(region=(hp_top_left_x, hp_top_left_y, hp_width, hp_height))
    # Convert the screenshot to RGB (just in case)
    hp_bar.convert("RGB")

    # Define the range for colors
    threshold = 175

    # Count the red pixels
    red_pixels = 0
    total_pixels = hp_width

    # Iterate through pixels to count red pixels
    for x in range(hp_width):
         r, g, b = hp_bar.getpixel((x, hp_height/2))
         if r >= threshold >= b:
            red_pixels += 1

    # Calculate the percentage of red pixels
    red_percentage = (red_pixels / total_pixels) * 100
    return red_percentage

def get_mp_percentage():
    mp_bar = pyautogui.screenshot(region=(mp_top_left_x, mp_top_left_y, mp_width, mp_height))
    # Convert the screenshot to RGB (just in case)
    mp_bar.convert("RGB")

    # Define the range for colors
    threshold = 175

    # Count the red pixels
    blue_pixels = 0
    total_pixels = mp_width

    # Iterate through pixels to count red pixels
    for x in range(mp_width):
         r, g, b = mp_bar.getpixel((x, mp_height/2))
         if b >= threshold >= r:
            blue_pixels += 1


    # Calculate the percentage of red pixels
    blue_percentage = (blue_pixels / total_pixels) * 100
    return blue_percentage

def get_char_x_map_position():
    map = pyautogui.screenshot(region=(map_top_left_x, map_top_left_y, map_width, map_height))
    pixels = np.array(map)

    yellow_threshold = (200, 200, 50)
    min_cluster_size = 10

    # Define the yellow color range for filtering
    yellow_min = np.array([yellow_threshold[0], yellow_threshold[1], 0])  # Min RGB for yellow
    yellow_max = np.array([255, 255, yellow_threshold[2]])  # Max RGB for yellow

    # Create a binary mask where yellow pixels are marked as True
    yellow_mask = np.all((pixels >= yellow_min) & (pixels <= yellow_max), axis=-1)

    # Get the coordinates of yellow pixels
    yellow_coordinates = np.argwhere(yellow_mask)

    # If there are no yellow pixels, return None
    if len(yellow_coordinates) == 0:
        return -1
    center_y, center_x = np.mean(yellow_coordinates, axis=0)
    return center_x