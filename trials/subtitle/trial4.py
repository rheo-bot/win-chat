import pyautogui
import win32api
import win32con
import time

def show_subtitle(message, duration):
    time.sleep(duration)    
    # Get the screen dimensions
    screen_width, screen_height = win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    # Calculate the position for the subtitle
    subtitle_x = screen_width // 2
    subtitle_y = screen_height - 50

    # Set the font properties
    font = {"family": "Arial", "size": 24, "color": (255, 255, 255)}

    # Display the subtitle message
    pyautogui.moveTo(subtitle_x, subtitle_y, duration=0)
    # pyautogui.typewrite(message, interval=0.1, font=font, center=True)
    pyautogui.typewrite(message, interval=0.1)
    # pyautogui.wait(duration)
    time.sleep(duration)    

    # Clear the subtitle message
    pyautogui.typewrite(['backspace'] * len(message), interval=0.1, center=True)

# Usage example
show_subtitle("Hello, World!", 20)  # Display "Hello, World!" as a subtitle for 20 seconds

