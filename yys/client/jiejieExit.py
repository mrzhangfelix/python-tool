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
		if pyautoguiUtil.button(self.noattackImg):
			sleep(1)
			if pyautoguiUtil.button(self.attackImg):
				sleep(2)
		# 点击退出
		if pyautoguiUtil.button(self.tuichuImg):
			sleep(2)
		# 点击确认
		if pyautoguiUtil.button(self.querenImg):
			sleep(4)
		if pyautoguiUtil.button(self.shibaiImg):
			sleep(1)
			self.shibaicount=self.shibaicount+1
		sleep(1)
		return self.shibaicount

	def threadJieJieExit(self, UI, exitCount):
		shibaiCount=0
		while shibaiCount<exitCount:
			if UI.event.is_set():
				UI.log.info("JieJieExit is stopping,shibaicount:" + str(shibaiCount))
				break
			sleep(1)
			shibaiCount = self.dowork()
			UI.log.info("JieJieExit is running,shibaicount:" + str(shibaiCount))
		UI.log.info("JieJieExit is end,shibaicount:" + str(shibaiCount))

if __name__ == '__main__':
	service=jiejieExit()
	service.dowork()
