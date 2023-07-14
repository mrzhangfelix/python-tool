import time
from pyautoguiUtil import button,click
from PIL import ImageGrab, Image


class yaoqi:
	def __init__(self):
		self.count=0
		self.teamUpImg = Image.open("img/yaoqi/teamUp.png")
		self.jieshouImg = Image.open("img/yaoqi/接受邀请.png")
		self.quxiaoImg = Image.open("img/yaoqi/是否邀请.png")
		self.yaoqiImg = Image.open("img/yaoqi/yaoqi.png")
		self.jiaruImg = Image.open("img/yaoqi/jiaru.png")
		self.tianzhanImg = Image.open("img/yaoqi/tiaozhan.png")
		self.endImg = Image.open("img/yaoqi/end.png")

	#刷碎片用
	def dowork(self):
		# 组队
		if button(self.teamUpImg):
			time.sleep(0.5)
		# 接受邀请,总有人御魂邀请，取消这个接受邀请功能
		# if button(self.jieshouImg,pos):
		# 	time.sleep(1)
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
			self.count+=1
			print("次数:{}".format(self.count))
			time.sleep(1)
		click()
		time.sleep(2)
		return self.count

	def threadSuipian(self, UI):
		count=0
		while True:
			if UI.event.is_set():
				UI.log.info("suipianService is stopping")
				break
			count=self.dowork()
			time.sleep(1)
			UI.log.info("suipianService is running,count:"+str(count))
		UI.log.info("suipianService is end,count:"+str(count))


if __name__ == '__main__':
	yaoqi()
