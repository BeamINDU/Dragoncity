import time
import keyboard
import pyautogui
import win32api
import win32con

time.sleep(2)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)


while not keyboard.is_pressed('q'):
    start = pyautogui.locateCenterOnScreen('gold.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    if start is not None:
        pyautogui.moveTo(start) 
        click()