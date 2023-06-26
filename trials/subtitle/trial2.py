import win32gui
import win32con
import win32api

def show_subtitle(message, duration):
    hwnd = win32gui.GetDesktopWindow()
    hdc = win32gui.GetDC(hwnd)

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

    # Calculate the subtitle position
    monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromWindow(hwnd))
    subtitle_x = monitor_info['Monitor'][0]
    subtitle_y = monitor_info['Monitor'][1] + monitor_info['Monitor'][3] - 100

    # Draw the subtitle text
    win32gui.DrawText(hdc, message, -1, (subtitle_x, subtitle_y, 0, 0),
                      win32con.DT_LEFT | win32con.DT_NOCLIP | win32con.DT_SINGLELINE)

    # Update the display
    win32gui.UpdateWindow(hwnd)

    # Wait for the specified duration
    import time
    time.sleep(duration)

    # # Clean up resources
    # win32gui.DeleteObject(subtitle_font)
    # win32gui.ReleaseDC(hwnd, hdc)

# Usage example
show_subtitle("Hello, World!", 100)  # Display "Hello, World!" as a subtitle for 5 seconds