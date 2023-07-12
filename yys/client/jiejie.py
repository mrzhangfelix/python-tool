from time import sleep
from PIL import ImageGrab, Image
import pyautoguiUtil

# pyinstaller -F tansuo.py --path="C:\Users\felix\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2"
class jiejie:
	def __init__(self):
		self.count=0
		self.shibaicount=0
		# 打开窗口在固定位置
		self.attackImg = Image.open("img/attack.png")
		self.noattackImg = Image.open("img/medal.png")
		self.endImg = Image.open("img/end.png")
		self.shibaiImg = Image.open("img/shibai.png")

	def dowork(self):
		pos=(0,0,1720,968)
		if pyautoguiUtil.button(self.noattackImg,pos):
			print('点击noattack按钮')
			sleep(1)
			if pyautoguiUtil.button(self.attackImg,pos):
				print('点击attack按钮')
				sleep(5)
		if pyautoguiUtil.button(self.endImg,pos):
			while pyautoguiUtil.button(self.endImg,pos):
				sleep(1)
			print('点击end按钮')
			self.count= self.count + 1
			print("chengong count:{}".format(self.count))
			sleep(1)
		if pyautoguiUtil.button(self.shibaiImg,pos):
			while pyautoguiUtil.button(self.shibaiImg,pos):
				sleep(1)
			print("点击shibai按钮")
			self.shibaicount=self.shibaicount+1
			print("shibai count:{}".format(self.shibaicount))
			sleep(1)
		sleep(1)
		return self.count


if __name__ == '__main__':
	jiejie=jiejie()