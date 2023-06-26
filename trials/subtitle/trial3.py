import pyautogui
import time

def show_subtitle(message, duration):
    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Calculate the position for the subtitle
    subtitle_x = screen_width // 2
    subtitle_y = screen_height - 100

    # Display the subtitle message
    pyautogui.alert(text=message, title='', button='OK', timeout=duration, region=(subtitle_x, subtitle_y))

# Usage example
show_subtitle("Hello, World!", 5)  # Display "Hello, World!" as a subtitle for 5 seconds