import time
from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import win32api,win32con,win32gui

class clickService:
    def __init__(self):
        self.x=1500
        self.y=720

    def dowork(self):
        pyautogui.moveTo(self.x,self.y)
        pyautogui.click()
        sleep(1)


if __name__ == '__main__':
    clickService=clickService()