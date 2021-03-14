import pyautogui
import time
import operator
# 钓鱼标志位id
diaoyuX, diaoyuY = 1910,881

# 获取坐标的颜色
def getcolor(x,y):
	screenshot = pyautogui.screenshot()
	color = screenshot.getpixel((x, y))
	return color

width, hight = pyautogui.size()
def main():
	print("start")
	paogan()
	try:
		while True:
			curcolor = getcolor(diaoyuX,diaoyuY)
			if isdiao(curcolor):
				for i in range(30):
					print("钓鱼--")
					pyautogui.click()
					time.sleep(0.2)
				print('钓了三十次，继续抛竿')
				paogan()
			time.sleep(0.1)
	except KeyboardInterrupt:
		print('Exit')

def isdiao(color):
	if color[0]<130 and color[0]>120:
		if color[1]<180 and color[1]>170:
			if color[2]<180 and color[2]>170:
				return True;
	return False

# 抛竿收杆动作
def paogan():
	print("抛竿。。。")
	pyautogui.press('t');

def shougan():
	pyautogui.click();
	# pyautogui.press('b');

if __name__ == '__main__':
	time.sleep(2)
	main()
