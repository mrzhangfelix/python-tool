import time
from time import sleep
from PIL import Image
from pyautogui import FailSafeException

from pyautoguiUtil import button, find, click, resource_path, autoAlert
import constant
from pymysqlUtil import update_st, update_data


class tansuo:
    def __init__(self):
        self.attackImg = Image.open(resource_path(
            constant.resolution_folder + "/tansuo/attack.png"))
        self.attackLeaderImg = Image.open(resource_path(
            constant.resolution_folder + "/tansuo/attackLeader.png"))
        self.pickUpImg = Image.open(resource_path(
            constant.resolution_folder + "/tansuo/pickUp.png"))
        self.exploreImg = Image.open(resource_path(
            constant.resolution_folder + "/tansuo/explore.png"))
        self.jieshuImg = Image.open(resource_path(
            constant.resolution_folder + "/tansuo/结束探索.png"))
        self.jieshouImg = Image.open(resource_path(
            constant.resolution_folder + "/接受协作邀请.png"))

        self.jingongImg = Image.open(resource_path(
            constant.resolution_folder + "/jiejie/attack.png"))
        self.noattackImg = Image.open(resource_path(
            constant.resolution_folder + "/jiejie/medal.png"))
        self.endImg = Image.open(resource_path(
            constant.resolution_folder + "/jiejie/end.png"))
        self.shibaiImg = Image.open(resource_path(
            constant.resolution_folder + "/jiejie/shibai.png"))
        self.kaishiImg = Image.open(resource_path(
            constant.resolution_folder + "/jiejie/打开结界突破.png"))
        self.guanbiImg = Image.open(resource_path(
            constant.resolution_folder + "/jiejie/关闭结界突破.png"))
        self.shuaxinImg = Image.open(resource_path(
            constant.resolution_folder + "/jiejie/刷新.png"))
        self.quedingImg = Image.open(resource_path(
            constant.resolution_folder + "/jiejie/确定退出.png"))

        self.huijuanxiaoImg = Image.open(resource_path(
            constant.resolution_folder + "/绘卷小.png"))
        self.huijuanzhongImg = Image.open(resource_path(
            constant.resolution_folder + "/绘卷中.png"))
        self.huijuandaImg = Image.open(resource_path(
            constant.resolution_folder + "/绘卷大.png"))

        self.tansuoTotalCount = 0
        self.tansuoLeaderCount = 0
        self.huijuanxiaoCount = 0
        self.huijuanzhongCount = 0
        self.huijuandaCount = 0
        self.tiaozhanTotalCount = 0

        self.UI = None
        update_st(2)

    def print_tansuo_status(self, type):
        msg = "正在{},探索:{},轮:{}，结界:{}，绘卷:{}-{}".format(type,
                                                              self.tansuoTotalCount, self.tansuoLeaderCount,
                                                              self.tiaozhanTotalCount,
                                                      self.huijuanxiaoCount,self.huijuanzhongCount)
        print(msg)
        remark="正在{},结界:{}，绘卷:{}-{}-{}".format(
            type,self.tiaozhanTotalCount, self.huijuanxiaoCount, self.huijuanzhongCount, self.huijuandaCount)
        update_data(2, self.tansuoTotalCount, remark)
        self.UI.log.info(msg)

    def doJiejie(self):
        self.UI.log.info("开始结界")
        button(self.kaishiImg)
        sleep(1)
        while True:
            if self.UI.event.is_set():
                break
            if button(self.noattackImg):
                # logger.info("第{}次选择挑战".format(tiaozhancount))
                sleep(1)
                if button(self.jingongImg):
                    # logger.info("开始第{}次进攻".format(tiaozhancount))
                    sleep(2)
                    if find(self.jingongImg):
                        # logger.info("挑战券数量为0")
                        while button(self.guanbiImg):
                            # logger.info("第{}次，挑战结束关闭".format(tiaozhancount))
                            sleep(1)
                        return
                    sleep(10)
                    while True:
                        if self.UI.event.is_set():
                            break
                        if find(self.huijuanxiaoImg):
                            self.huijuanxiaoCount += 1
                        if find(self.huijuanzhongImg):
                            self.huijuanzhongCount += 1
                        if find(self.huijuandaImg):
                            self.huijuandaCount += 1
                        if button(self.endImg):
                            # logger.info("第{}次，挑战成功".format(tiaozhancount))
                            sleep(1)
                            while button(self.endImg):
                                # logger.info("第{}次，挑战成功".format(tiaozhancount))
                                sleep(1)
                            self.tiaozhanTotalCount += 1
                            self.print_tansuo_status("结界")
                            sleep(1)
                            break
                        if button(self.shibaiImg):
                            sleep(1)
                            while button(self.shibaiImg):
                                sleep(1)
                            self.UI.log.info("突破失败")
                            sleep(1)
                            break
                        sleep(5)
            sleep(3)
            if not find(self.noattackImg) and find(self.shuaxinImg):
                self.UI.log.error("没有可以挑战的结界，存在挑战失败")
                self.buttonshuaxin()

    def doTansou(self, n):
        self.UI.log.info("开始探索")
        attackCount = 0
        while True:
            if self.UI.event.is_set():
                break
            if button(self.attackLeaderImg):
                self.tansuoTotalCount += 1
                self.tansuoLeaderCount += 1
                self.print_tansuo_status("探索")
                attackCount += 1
                time.sleep(5)
                continue
            if button(self.attackImg):
                # logger.info("attack次数:" + str(attackCount))
                self.tansuoTotalCount += 1
                self.print_tansuo_status("探索")
                attackCount += 1
                time.sleep(5)
                continue
            if button(self.pickUpImg):
                click()
                continue
            if find(self.exploreImg) and attackCount > n:
                button(self.jieshuImg)
                time.sleep(2)
                break
            if button(self.exploreImg):
                time.sleep(2)
                continue
            if find(self.huijuanxiaoImg):
                self.huijuanxiaoCount += 1
            if find(self.huijuanzhongImg):
                self.huijuanzhongCount += 1
            if find(self.huijuandaImg):
                self.huijuandaCount += 1
            # X: 2196 , Y:  809
            click()
            time.sleep(2)

    def buttonshuaxin(self):
        if button(self.shuaxinImg):
            print("点击刷新")
            self.UI.log.info("刷新")
            sleep(1)
            if button(self.quedingImg):
                self.UI.log.info("刷新成功")
                sleep(5)
        else:
            self.UI.log.info("刷新冷却中")
            while not button(self.shuaxinImg):
                self.UI.log.info("没有找到刷新按钮")
                sleep(30)
            if button(self.quedingImg):
                self.UI.log.info("刷新成功")
                sleep(2)

    def threadHuijuan(self, UI, tiaozhanCount, jiejie_swith):
        try:
            self.UI = UI
            while True:
                if self.UI.event.is_set():
                    break
                if self.tiaozhanTotalCount > tiaozhanCount:
                    break
                if jiejie_swith.get():
                    self.doJiejie()
                self.doTansou(50)
        except FailSafeException:
            UI.log.error("程序安全退出")
            autoAlert("程序安全退出")


if __name__ == '__main__':
    tansuo = tansuo()
