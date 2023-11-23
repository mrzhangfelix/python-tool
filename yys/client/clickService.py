import time
from time import sleep
from PIL import Image

import pyautogui

from pyautoguiUtil import autoAlert, click, resource_path, button, find, clickPos
import constant


class clickService:
    def __init__(self):
        self.jieshouImg = Image.open(resource_path(
            constant.resolution_folder + "/接受协作邀请.png"))

    def jieshouyaoqing(self, UI):
        while True:
            if UI.event.is_set():
                UI.log.info("接受邀请现场停止")
                break
            if button(self.jieshouImg):
                UI.log.error("接受悬赏邀请")
            sleep(5)

    def threadclick(self, UI, x, y):
        try:
            while True:
                if UI.event.is_set():
                    break
                clickPos(x, y)
                time.sleep(1)
                UI.log.info("连续点击线程运行中")
            UI.log.info("连续点击线程停止")
        except pyautogui.FailSafeException:
            UI.log.error("程序安全退出")
            autoAlert("程序安全退出")

    def threadMouseClick(self, UI):
        try:
            while True:
                if UI.event.is_set():
                    break
                pyautogui.click()
                time.sleep(1)
                UI.log.info("连续点击线程运行中")
            UI.log.info("连续点击线程停止")
        except pyautogui.FailSafeException:
            UI.log.error("程序安全退出")
            autoAlert("程序安全退出")

    def threadqiling(self):
        qilingCount = 0
        qilingShibaiCount = 0
        zhenhunshouImg = Image.open(resource_path(
            constant.resolution_folder + "/qiling/zhenhunshou.png"))
        tiaozhanImg = Image.open(resource_path(
            constant.resolution_folder + "/qiling/tiaozhan.png"))
        endImg = Image.open(resource_path(
            constant.resolution_folder + "/end.png"))
        shibaiImg = Image.open(resource_path(
            constant.resolution_folder + "/shibai.png"))
        try:
            while True:
                if find(zhenhunshouImg):
                    button(tiaozhanImg)
                if button(endImg):
                    qilingCount += 1
                    print("chenggong:{}".format(qilingCount))
                if button(shibaiImg):
                    qilingShibaiCount += 1
                    print("shibai:{}".format(qilingShibaiCount))
                time.sleep(1)
        except pyautogui.FailSafeException:
            autoAlert("程序安全退出")


if __name__ == '__main__':
    clickService = clickService()
    clickService.threadqiling()
