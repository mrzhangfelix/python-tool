import time
import pyautogui
from PIL import ImageGrab, Image

#刷碎片用
def main():
	# 状态 0：初始 1：组队界面 2：匹配中 3：战斗中 4：战斗结束
	status=1
	a=1
	teamUpImg = Image.open("teamUp.png")
	matchImg = Image.open("match.png")
	prepareImg = Image.open("prepare.png")
	endImg = Image.open("end.png")
	while True:
		if status==4 and button(teamUpImg):
			print("点击teamUp按钮")
			status=1
			time.sleep(1)
		if status==1 and button(matchImg):
			print("点击match按钮")
			status=2
			time.sleep(1)
		if status==2 and button(prepareImg):
			# 确保战斗开始
			while button(prepareImg):
				time.sleep(2)
			print("点击prepare按钮")
			status=3
			print("开始次数:{}".format(a))
			a=a+1
			time.sleep(20)
		if status==3 and button(endImg):
			status=4
			time.sleep(1)
			continue
		time.sleep(3)

def button(Img):
	msg = pyautogui.locateOnScreen(Img, confidence=0.9)
	if msg == None:
		return False
	else:
		x, y, width, height = msg
		# print("X={},Y={}，宽{}像素,高{}像素".format(x, y, width, height))
		center=pyautogui.center((x,y,width,height))
		pyautogui.click(center)
		return True


if __name__ == '__main__':
	main()
