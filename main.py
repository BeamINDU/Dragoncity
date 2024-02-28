import win32api
import win32con
import cv2
import numpy as np
import pyautogui
import time
import keyboard

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# หยุดเป็นเวลา 2 วินาที
time.sleep(2)

# โหลดภาพที่ต้องการหา
template = cv2.imread('gold2.png')
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

while keyboard.is_pressed('q') == False:
    # จับภาพหน้าจอในบริเวณที่กำหนด
    screenshot = pyautogui.screenshot(region=(700, 500, 751, 700))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # ทำ grayscale สำหรับทั้งภาพหน้าจอและภาพที่ต้องการหา
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # ค้นหาภาพที่ต้องการในภาพหน้าจอ
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.7

    if max_val >= threshold:
        # หากพบภาพที่ต้องการในภาพหน้าจอ
        click(max_loc[0] + 584, max_loc[1] + 422)
        time.sleep(0.05)
