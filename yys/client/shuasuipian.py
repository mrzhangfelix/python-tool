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
		pos=(0,0,1720,968)
		# 组队
		if button(self.teamUpImg,pos):
			time.sleep(0.5)
		# 接受邀请
		if button(self.jieshouImg,pos):
			time.sleep(1)
		# 自己当房主取消邀请其他人
		if button(self.quxiaoImg,pos):
			time.sleep(1)
		# 自己当房主挑战
		if button(self.tianzhanImg,pos):
			time.sleep(1)
		# 妖气加入
		if button(self.yaoqiImg,pos):
			time.sleep(0.5)
			while button(self.jiaruImg,pos):
				print("jiaruImg")
				time.sleep(0.5)
		if button(self.endImg,pos):
			while button(self.endImg,pos):
				print("endImg")
				time.sleep(1)
			self.count+=1
			print("次数:{}".format(self.count))
			time.sleep(1)
		click()
		print("click")
		time.sleep(2)
		return self.count


if __name__ == '__main__':
	yaoqi()
