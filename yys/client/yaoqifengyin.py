import time

from pyautogui import FailSafeException

from pyautoguiUtil import resource_path, button, click, find, autoAlert
from PIL import Image

import constant
from pymysqlUtil import update_st,update_data


class yaoqi:
    def __init__(self):
        self.count = 0
        self.teamUpImg = Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\teamUp.png"))
        self.jieshouImg = Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\接受邀请.png"))
        self.jujueImg = Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\拒绝邀请.png"))
        self.quxiaoImg = Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\是否邀请.png"))
        self.yaoqiImg = Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\yaoqi.png"))
        self.jiaruImg = Image.open \
            (resource_path(constant.resolution_folder + "\\yaoqi\\jiaru.png"))
        self.tianzhanImg = Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\tiaozhan.png"))
        self.endImg = Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\end.png"))
        self.yaoguaiImg_list = []
        self.yaoguaiImg_list.append(Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\yaoguai\\二口女.png")))
        self.yaoguaiImg_list.append(Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\yaoguai\\小松丸.png")))
        self.yaoguaiImg_list.append(Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\yaoguai\\日和坊.png")))
        self.yaoguaiImg_list.append(Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\yaoguai\\椒图.png")))
        self.yaoguaiImg_list.append(Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\yaoguai\\海坊主.png")))
        self.yaoguaiImg_list.append(Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\yaoguai\\跳跳哥哥.png")))
        self.yaoguaiImg_list.append(Image.open(
            resource_path(constant.resolution_folder + "\\yaoqi\\yaoguai\\鬼使黑.png")))
        update_st(3)

        self.jieshouyaoqingzuobiao = (250, 350)
        self.jujueyaoqingzuobiao = (130, 350)

    def is_yaoguai(self):
        for img in self.yaoguaiImg_list:
            if find(img):
                return True
        return False

    # 刷碎片用
    def dowork(self):
        # 组队
        if button(self.teamUpImg):
            time.sleep(0.5)
        # 如果是妖气妖怪就接受邀请
        if find(self.jieshouImg):
            if self.is_yaoguai():
                button(self.jieshouImg)
            else:
                button(self.jujueImg)
            time.sleep(1)
        # 自己当房主取消邀请其他人
        if button(self.quxiaoImg):
            time.sleep(1)
        # 自己当房主挑战
        if button(self.tianzhanImg):
            time.sleep(1)
        # 妖气加入
        if button(self.yaoqiImg):
            time.sleep(0.5)
            while button(self.jiaruImg):
                time.sleep(0.5)
        if button(self.endImg):
            while button(self.endImg):
                time.sleep(1)
            self.count += 1
            update_data(3,self.count,'running')
            print("次数:{}".format(self.count))
            time.sleep(1)
            return self.count
        click()
        time.sleep(2)
        return self.count

    def threadSuipian(self, UI):
        try:
            count = 0
            while True:
                if UI.event.is_set():
                    UI.log.info("suipianService is stopping")
                    break
                count = self.dowork()
                time.sleep(1)
                UI.log.info("suipianService is running,count:" + str(count))
            UI.log.info("suipianService is end,count:" + str(count))
        except FailSafeException:
            UI.log.error("程序安全退出")
            autoAlert("程序安全退出")
        finally:
            update_data(3,self.count,'ended')


if __name__ == '__main__':
    yaoqiservice = yaoqi()
    while True:
        yaoqiservice.dowork()
