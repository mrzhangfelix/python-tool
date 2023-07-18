import sys
from time import sleep
from PIL import Image
from pyautogui import FailSafeException
import constant

sys.path.append("")
from pyautoguiUtil import resource_path, button, autoAlert


# pyinstaller -F tansuo.py --path="C:\Users\felix\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2"
class jiejie:
	def __init__(self):
		self.count=0
		self.shibaicount=0
		# 打开窗口在固定位置
		self.attackImg = Image.open(resource_path(
			constant.resolution_folder+"/jiejie/attack.png"))
		self.noattackImg = Image.open(resource_path(
			constant.resolution_folder+"/jiejie/medal.png"))
		self.endImg = Image.open(resource_path(
			constant.resolution_folder+"/jiejie/end.png"))
		self.shibaiImg = Image.open(resource_path(
			constant.resolution_folder+"/jiejie/shibai.png"))

	def dowork(self):
		if button(self.noattackImg):
			print('点击noattack按钮')
			sleep(1)
			if button(self.attackImg):
				print('点击attack按钮')
				sleep(5)
		if button(self.endImg):
			while button(self.endImg):
				sleep(1)
			print('点击end按钮')
			self.count= self.count + 1
			print("chengong count:{}".format(self.count))
			sleep(1)
		if button(self.shibaiImg):
			while button(self.shibaiImg):
				sleep(1)
			print("点击shibai按钮")
			self.shibaicount=self.shibaicount+1
			print("shibai count:{}".format(self.shibaicount))
			sleep(1)
		sleep(1)
		return self.count

	def threadJieJie(self, UI,delayTime):
		try:
			sleep(delayTime*60)
			count=0
			while True:
				if UI.event.is_set():
					break
				count=self.dowork()
				sleep(1)
				UI.log.info("结界突破运行中,count:" + str(count))
			UI.log.info("结界突破结束,count:" + str(count))
		except FailSafeException:
			UI.log.error("程序安全退出")
			autoAlert("程序安全退出")

if __name__ == '__main__':
	jiejie=jiejie()