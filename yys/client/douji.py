import time

from pyautogui import FailSafeException

from pyautoguiUtil import resource_path, button, click, find, autoAlert, clickPos
from PIL import Image

import constant
from pymysqlUtil import update_st,update_data


class douji:
    def __init__(self):
        self.chenggongcount = 0
        self.shibaicount = 0
        self.totalcount=0
        self.zhanImg = Image.open(
            resource_path(constant.resolution_folder + "\\douji\\zhan.png"))
        self.zidongshangzhenImg = Image.open(
            resource_path(constant.resolution_folder + "\\douji\\zidongshangzhen.png"))
        self.shoudongImg = Image.open(
            resource_path(constant.resolution_folder + "\\douji\\shoudong.png"))
        self.chenggongImg = Image.open(
            resource_path(constant.resolution_folder + "\\douji\\chenggong.png"))
        self.shibaiImg = Image.open(
            resource_path(constant.resolution_folder + "\\douji\\shibai.png"))
        self.biaojiImg = Image.open(
            resource_path(constant.resolution_folder + "\\douji\\biaoji.png"))

    # 刷碎片用
    def dowork(self):
        # 开始
        if button(self.zhanImg):
            self.totalcount+=1
            time.sleep(2)
        # 自动上阵
        if button(self.zidongshangzhenImg):
            time.sleep(2)
        # 手动
        if button(self.shoudongImg):
            time.sleep(2)
            if not find(self.biaojiImg):
                clickPos(1000,500)
            time.sleep(10)
        # 成功
        if button(self.chenggongImg):
            self.chenggongcount+=1
            time.sleep(2)
        # 失败
        if button(self.shibaiImg):
            self.shibaicount+=1
            time.sleep(2)
        time.sleep(5)
        return self.chenggongcount,self.shibaicount,self.totalcount

    def threaddouji(self, UI):
        try:
            count = 0
            while True:
                if UI.event.is_set():
                    UI.log.info("斗鸡 is stopping")
                    break
                count = self.dowork()
                time.sleep(1)
                UI.log.info("斗鸡 is running,成功:" + str(self.chenggongcount)
                            +"失败："+str(self.shibaicount)
                            +"总次数："+str(self.totalcount))

            UI.log.info("斗鸡 is end")
        except FailSafeException:
            UI.log.error("程序安全退出")
            autoAlert("程序安全退出")


if __name__ == '__main__':
    doujiservice = douji()
    while True:
        doujiservice.dowork()
