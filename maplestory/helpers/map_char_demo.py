from PIL import Image
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from eds_config import *
import pyautogui
import time

def find_yellow_dot_center(yellow_threshold=(200, 200, 50), min_cluster_size=10):
    # Load the image
    image = pyautogui.screenshot(region=(map_top_left_x, map_top_left_y, map_width, map_height))
    # Convert image to numpy array
    pixels = np.array(image)

    # Define the yellow color range for filtering
    yellow_min = np.array([yellow_threshold[0], yellow_threshold[1], 0])  # Min RGB for yellow
    yellow_max = np.array([255, 255, yellow_threshold[2]])  # Max RGB for yellow

    # Create a binary mask where yellow pixels are marked as True
    yellow_mask = np.all((pixels >= yellow_min) & (pixels <= yellow_max), axis=-1)

    # Get the coordinates of yellow pixels
    yellow_coordinates = np.argwhere(yellow_mask)

    # If there are no yellow pixels, return None
    if len(yellow_coordinates) == 0:
        return None

    # Calculate the center of the yellow cluster
    center_y, center_x = np.mean(yellow_coordinates, axis=0)
    center_coordinates = (int(center_x), int(center_y))

    print(f"Center of yellow cluster: {center_coordinates}")
    return center_coordinates


# Example usage:
while True:
    center = find_yellow_dot_center()
    if center:
        print(f"Yellow dot center coordinates: {center}")
    else:
        print("No yellow pixels found.")
    time.sleep(1)