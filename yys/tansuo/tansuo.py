import pyautogui
import time

from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import sys

def main():
	a=1
	b=1
	# 事先对按钮截图
	attackImg = Image.open("attack.png")
	attackLeaderImg = Image.open("attackLeader.png")
	pickUpImg = Image.open("pickUp.png")
	exploreImg = Image.open("explore.png")
	while True:
		if button(attackImg,"attack"):
			print("attack次数:"+str(b))
			b=b+1
			time.sleep(5)
			continue
		if button(attackLeaderImg,"attackLeader"):
			print("attackLeader次数:"+str(a))
			a=a+1
			time.sleep(5)
			continue
		if button(pickUpImg,"pickUp"):
			pyautogui.moveTo(2196,809)
			pyautogui.click()
			continue
		if button(exploreImg,"explore.png"):
			time.sleep(2)
			continue
		# X: 2196 , Y:  809
		pyautogui.moveTo(2360,776)
		pyautogui.click()
		time.sleep(1)


def button(Img,imgName):
	msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True)
	if msg == None:
		return False
	else:
		x, y, width, height = msg
		print("点击"+imgName+"按钮")
		# print("X={},Y={}，宽{}像素,高{}像素".format(x, y, width, height))
		center=pyautogui.center((x,y,width,height))
		pyautogui.click(center)
		return True

if __name__ == '__main__':
	main()
