from time import sleep
import pyautogui
from PIL import ImageGrab, Image

def main():
	a=1
	# 事先对按钮截图
	attackImg = Image.open("attack.png")
	noattackImg = Image.open("medal.png")
	while True:
		if button(noattackImg):
			print("点击zeroMedal按钮")
			sleep(1)
			if button(attackImg):
				print("点击attack按钮")
				sleep(10)
			continue
		pyautogui.moveTo(2360,776)
		pyautogui.click()
		sleep(3)


def button(Img):
	msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True)
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
