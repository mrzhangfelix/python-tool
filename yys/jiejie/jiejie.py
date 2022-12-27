from time import sleep
import pyautogui
from PIL import ImageGrab, Image

def main():
	a=1
	# 事先对按钮截图
	attackImg = Image.open("attack.png")
	zeroMedalImg = Image.open("medal.png")
	# fullMedalImg = Image.open("fullMedal.png")
	while True:
		if button(zeroMedalImg,"0Medal"):
			print("点击zeroMedal按钮")
			sleep(1)
			if button(attackImg,"attack"):
				print("点击attack按钮")
				sleep(10)
			continue
		# if button(fullMedalImg,"5Medal"):
		# 	print("点击5Medal按钮")
		# 	sleep(1)
		# 	if button(attackImg,"attack"):
		# 		print("点击attack按钮")
		# 		sleep(10)
		# 	continue
		pyautogui.moveTo(2360,776)
		pyautogui.click()
		sleep(2)


def button(Img,imgName):
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
