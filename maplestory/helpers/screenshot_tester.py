import pyautogui
from pynput import mouse

# Initialize variables to store the coordinates
coords = []

# Mouse click event handler
def on_click(x, y, button, pressed):
    if pressed:
        # Store coordinates of each click
        coords.append((x, y))
        print(f"Mouse clicked at ({x}, {y})")

        # When we have two clicks, capture the region
        if len(coords) == 2:
            # Calculate the region based on the two clicks
            x1, y1 = coords[0]
            x2, y2 = coords[1]

            # Calculate width and height from the two corners
            top_left_x = min(x1, x2)
            top_left_y = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)

            # Take the screenshot of the specified region
            screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, width, height))
            print("Screenshot taken. Top Left X:" + str(top_left_x) + " Top Left Y:" + str(top_left_y) + " Width:" + str(width) + " Height:" + str(height))
            screenshot.show()
            # Stop the listener after taking the screenshot
            return False

# Set up the listener for mouse clicks
with mouse.Listener(on_click=on_click) as listener:
    listener.join()