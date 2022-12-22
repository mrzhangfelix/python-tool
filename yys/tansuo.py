import pyautogui
import time

from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import sys

def main():
	a=1
	b=1
	while True:
		if button("攻击.png",0.7):
			print("小怪次数:"+str(b))
			b=b+1
			time.sleep(5)
			continue
		if button("攻击首领.png",0.7):
			print("首领次数:"+str(a))
			a=a+1
			time.sleep(5)
			continue
		if button("捡东西.png",0.7):
			continue
		if button("探索.png",0.7):
			time.sleep(2)
			continue
		# X: 2196 , Y:  809
		pyautogui.moveTo(2196,809)
		pyautogui.click()
		time.sleep(1)


def button(png,confidence):
	# 事先对按钮截图
	Img = Image.open(png)
	time.sleep(1)
	# 截图当前屏幕并找到之前加载的按钮截图 confidence的值决定精度
	msg = pyautogui.locateOnScreen(Img, confidence=confidence, grayscale=True)
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
