import win32gui
import win32api
import win32con


def show_subtitle(message, duration):
    hwnd = win32gui.GetDesktopWindow()
    hdc = win32gui.GetDC(hwnd)

    # Get the screen dimensions
    screen_width, screen_height = win32api.GetSystemMetrics(
        win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    # Calculate the position for the subtitle
    subtitle_x = screen_width // 2
    subtitle_y = screen_height - 50

    # Set the font properties
    font = win32gui.LOGFONT()
    font.lfHeight = 36
    font.lfWeight = win32con.FW_BOLD
    font.lfQuality = win32con.NONANTIALIASED_QUALITY
    font.lfFaceName = "Arial"

    # Create the font and set it in the device context
    subtitle_font = win32gui.CreateFontIndirect(font)
    win32gui.SelectObject(hdc, subtitle_font)

    # Set the text color and background mode
    win32gui.SetTextColor(hdc, win32api.RGB(255, 255, 255))
    win32gui.SetBkMode(hdc, win32con.TRANSPARENT)

    # Draw the subtitle text
    win32gui.DrawText(hdc, message, -1, (subtitle_x, subtitle_y, 0, 0),
                      win32con.DT_LEFT | win32con.DT_NOCLIP | win32con.DT_SINGLELINE)

    # Update the display
    win32gui.UpdateWindow(hwnd)

    # Wait for the specified duration
    import time
    time.sleep(duration)


# Usage example
# Display "Hello, World!" as a subtitle for 5 seconds
show_subtitle("Hello, World!", 5)
show_subtitle("Bye Bye!", 2)
