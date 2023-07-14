import sys
from time import sleep
from PIL import Image
sys.path.append("")
from utils import pyautoguiUtil
from utils.pyautoguiUtil import resource_path

# pyinstaller -F tansuo.py --path="C:\Users\felix\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2"
class jiejie:
	def __init__(self):
		self.count=0
		self.shibaicount=0
		# 打开窗口在固定位置
		self.attackImg = Image.open(resource_path("img/jiejie/attack.png"))
		self.noattackImg = Image.open(resource_path("img/jiejie/medal.png"))
		self.endImg = Image.open(resource_path("img/jiejie/end.png"))
		self.shibaiImg = Image.open(resource_path("img/jiejie/shibai.png"))

	def dowork(self):
		if pyautoguiUtil.button(self.noattackImg):
			print('点击noattack按钮')
			sleep(1)
			if pyautoguiUtil.button(self.attackImg):
				print('点击attack按钮')
				sleep(5)
		if pyautoguiUtil.button(self.endImg):
			while pyautoguiUtil.button(self.endImg):
				sleep(1)
			print('点击end按钮')
			self.count= self.count + 1
			print("chengong count:{}".format(self.count))
			sleep(1)
		if pyautoguiUtil.button(self.shibaiImg):
			while pyautoguiUtil.button(self.shibaiImg):
				sleep(1)
			print("点击shibai按钮")
			self.shibaicount=self.shibaicount+1
			print("shibai count:{}".format(self.shibaicount))
			sleep(1)
		sleep(1)
		return self.count

	def threadJieJie(self, UI,delayTime):
		sleep(delayTime*60)
		count=0
		while True:
			if UI.event.is_set():
				UI.log.info("tread is stopping")
				break
			count=self.dowork()
			sleep(1)
			UI.log.info("jiejie is running,count:" + str(count))
		UI.log.info("jiejie is end,count:" + str(count))

if __name__ == '__main__':
	jiejie=jiejie()