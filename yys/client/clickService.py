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

    def threadclick(self,UI):
        while True:
            if UI.event.is_set():
                UI.log.info("tread is stopping")
                break
            self.dowork()
            time.sleep(1)
            UI.log.info("click is running")
        UI.log.info("click is end")


if __name__ == '__main__':
    clickService=clickService()