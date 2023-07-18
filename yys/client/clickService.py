import time
from time import sleep
from PIL import Image

import pyautogui

from pyautoguiUtil import autoAlert, click, resource_path, button
import constant


class clickService:
    def __init__(self):
        self.jieshouImg = Image.open(resource_path(
            constant.resolution_folder + "/接受协作邀请.png"))


    def jieshouyaoqing(self,UI):
        while True:
            if UI.event.is_set():
                UI.log.info("接受邀请现场停止")
                break
            if button(self.jieshouImg):
                UI.log.error("接受悬赏邀请")
            sleep(5)

    def threadclick(self,UI):
        try:
            while True:
                if UI.event.is_set():
                    break
                click()
                time.sleep(1)
                UI.log.info("连续点击线程运行中")
            UI.log.info("连续点击线程停止")
        except pyautogui.FailSafeException:
            UI.log.error("程序安全退出")
            autoAlert("程序安全退出")


if __name__ == '__main__':
    clickService=clickService()