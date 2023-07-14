import time
from time import sleep
from PIL import Image

from utils.pyautoguiUtil import button,find,click,resource_path

class tansuo:
    def __init__(self):
        self.attackImg = Image.open(resource_path("img/tansuo/attack.png"))
        self.attackLeaderImg = Image.open(resource_path("img/tansuo/attackLeader.png"))
        self.pickUpImg = Image.open(resource_path("img/tansuo/pickUp.png"))
        self.exploreImg = Image.open(resource_path("img/tansuo/explore.png"))
        self.jieshuImg = Image.open(resource_path("img/tansuo/结束探索.png"))
        self.jieshouImg = Image.open(resource_path("img/接受.png"))
        self.huijuanzhongImg = Image.open(resource_path("img/绘卷中.png"))

        self.attackImg = Image.open(resource_path("img/jiejie/attack.png"))
        self.noattackImg = Image.open(resource_path("img/jiejie/medal.png"))
        self.endImg = Image.open(resource_path("img/jiejie/end.png"))
        self.shibaiImg = Image.open(resource_path("img/jiejie/shibai.png"))
        self.kaishiImg = Image.open(resource_path("img/jiejie/打开结界突破.png"))
        self.guanbiImg = Image.open(resource_path("img/jiejie/关闭结界突破.png"))
        self.shuaxinImg = Image.open(resource_path("img/jiejie/刷新.png"))
        self.quedingImg = Image.open(resource_path("img/jiejie/确定退出.png"))
        self.huijuanzhongImg = Image.open(resource_path("img/绘卷中.png"))

        self.tansuoTotalCount=0
        self.tansuoLeaderCount=0
        self.huijuanzhongCount=0
        self.tiaozhanTotalCount=0

        self.UI=None

    def print_tansuo_status(self):
        msg = "探索总数：{},探索轮数：{}，结界数：{}，绘卷中数：{}".format(
            self.tansuoTotalCount, self.tansuoLeaderCount,self.tiaozhanTotalCount, self.huijuanzhongCount)
        print(msg)
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
                if button(self.attackImg):
                    # logger.info("开始第{}次进攻".format(tiaozhancount))
                    sleep(2)
                    if find(self.attackImg):
                        # logger.info("挑战券数量为0")
                        while button(self.guanbiImg):
                            # logger.info("第{}次，挑战结束关闭".format(tiaozhancount))
                            sleep(1)
                        return
                    sleep(10)
                    while True:
                        if self.UI.event.is_set():
                            break
                        if find(self.huijuanzhongImg):
                            self.huijuanzhongCount+=1
                            self.print_tansuo_status()
                        if button(self.endImg):
                            # logger.info("第{}次，挑战成功".format(tiaozhancount))
                            sleep(1)
                            while button(self.endImg):
                                # logger.info("第{}次，挑战成功".format(tiaozhancount))
                                sleep(1)
                            self.tiaozhanTotalCount+=1
                            self.print_tansuo_status()
                            sleep(1)
                            break
                        if button(self.shibaiImg):
                            sleep(1)
                            while button(self.shibaiImg):
                                sleep(1)
                            self.UI.log.info("失败突破次数")
                            sleep(1)
                            break
                        sleep(5)
            sleep(3)
            if not find(self.noattackImg) and find(self.shuaxinImg):
                self.UI.log.error("没有可以挑战的结界，存在挑战失败")
                self.buttonshuaxin()

    def doTansou(self,n):
        self.UI.log.info("开始探索")
        attackCount=0
        while True:
            if self.UI.event.is_set():
                break
            if button(self.attackLeaderImg):
                self.tansuoTotalCount+=1
                self.tansuoLeaderCount+=1
                self.print_tansuo_status()
                attackCount+=1
                time.sleep(5)
                continue
            if button(self.attackImg):
                # logger.info("attack次数:" + str(attackCount))
                self.tansuoTotalCount+=1
                self.print_tansuo_status()
                attackCount+=1
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
            if find(self.huijuanzhongImg):
                self.huijuanzhongCount+=1
                self.print_tansuo_status()
            # X: 2196 , Y:  809
            click()
            time.sleep(2)

    def buttonshuaxin(self):
        if button(self.shuaxinImg):
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


    def threadHuijuan(self, UI):
        self.UI=UI
        while True:
            if self.UI.event.is_set():
                break
            self.doJiejie()
            self.doTansou(50)


if __name__ == '__main__':
    tansuo=tansuo()