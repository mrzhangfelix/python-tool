import pyautogui
import time

from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import sys

def main():
	a=1
	while True:
		if button("进攻.png"):
			time.sleep(2)
			continue
		if button("空勋章.png"):
			time.sleep(1)
			if button("进攻.png"):
				time.sleep(15)
			continue
		if button("满勋章.png"):
			time.sleep(1)
			if button("进攻.png"):
				time.sleep(15)
			continue
		# if button("准备.png"):
		# 	print("次数:"+str(a))
		# 	a=a+1
		# 	time.sleep(20)
		# 	continue
		pyautogui.moveTo(2360,776)
		pyautogui.click()
		time.sleep(1)


def button(png):
	# 事先对按钮截图
	Img = Image.open(png)
	time.sleep(1)
	# 截图当前屏幕并找到之前加载的按钮截图 confidence的值决定精度
	msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True)
	if msg == None:
		return False
	else:
		x, y, width, height = msg
		print()
		print("点击"+png+"按钮")
		# print("X={},Y={}，宽{}像素,高{}像素".format(x, y, width, height))
		center=pyautogui.center((x,y,width,height))
		pyautogui.click(center)
		return True


if __name__ == '__main__':
	main()
