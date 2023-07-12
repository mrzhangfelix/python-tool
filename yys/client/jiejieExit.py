from time import sleep
from PIL import ImageGrab, Image
import pyautoguiUtil

# pyinstaller -F tansuo.py --path="C:\Users\felix\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2"
class jiejieExit:
	def __init__(self):
		self.attackImg = Image.open("img/jiejie/attack.png")
		self.noattackImg = Image.open("img/jiejie/medal.png")
		self.shibaiImg = Image.open("img/jiejie/shibai.png")
		self.tuichuImg = Image.open("img/jiejie/退出.png")
		self.querenImg = Image.open("img/jiejie/确认.png")
		self.shibaicount=0

	def dowork(self):
		pos=(0,0,1720,968)
		if pyautoguiUtil.button(self.noattackImg,pos):
			sleep(1)
			if pyautoguiUtil.button(self.attackImg,pos):
				sleep(2)
		# 点击退出
		if pyautoguiUtil.button(self.tuichuImg,pos):
			sleep(2)
		# 点击确认
		if pyautoguiUtil.button(self.querenImg,pos):
			sleep(4)
		if pyautoguiUtil.button(self.shibaiImg,pos):
			sleep(1)
			self.shibaicount=self.shibaicount+1
		sleep(1)
		return self.shibaicount

if __name__ == '__main__':
	service=jiejieExit()
	service.dowork()
