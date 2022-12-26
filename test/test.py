import pyautogui
import time

from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import sys

#刷碎片用
def main():
	a=1
	while True:
		if button("match.png"):
			print("次数:"+str(a))
			a=a+1
			time.sleep(2)
			continue
		time.sleep(1)


def button(png):
	# 事先对按钮截图
	Img = Image.open(png)
	time.sleep(1)
	# 截图当前屏幕并找到之前加载的按钮截图 confidence的值决定精度
	msg = pyautogui.locateOnScreen(Img, confidence=0.6, grayscale=True)
	if msg == None:
		return False
	else:
		x, y, width, height = msg
		print()
		print("点击"+png+"按钮")
		print("X={},Y={}，宽{}像素,高{}像素".format(x, y, width, height))
		center=pyautogui.center((x,y,width,height))
		pyautogui.click(center)
		return True


if __name__ == '__main__':
	main()
