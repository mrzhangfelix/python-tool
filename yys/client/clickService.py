import time
from time import sleep
import pyautogui

from pyautoguiUtil import autoAlert


class clickService:
    def __init__(self):
        self.x=1500
        self.y=720

    def dowork(self):
        pyautogui.moveTo(self.x,self.y)
        pyautogui.click()
        sleep(1)

    def threadclick(self,UI):
        try:
            while True:
                if UI.event.is_set():
                    UI.log.info("tread is stopping")
                    break
                self.dowork()
                time.sleep(1)
                UI.log.info("click is running")
            UI.log.info("click is end")
        except pyautogui.FailSafeException:
            UI.log.error("程序安全退出")
            autoAlert("程序安全退出")


if __name__ == '__main__':
    clickService=clickService()