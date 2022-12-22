import pyautogui
import time
currentMouseX, currentMouseY = pyautogui.position()
width, hight = pyautogui.size()
def main():
	# pyautogui.moveTo(width, hight, duration=2)
	# pyautogui.moveTo(width/2, hight/2, duration=2) # 基本移动
	# pyautogui.moveTo(100, 100, duration=2) # 移动过程持续2s完成
	# pyautogui.moveTo(None, 100) # X方向不变，Y方向移动到100
	# for i in range(30):
	while True:
		# pyautogui.moveRel(-10, -10, duration=2) # 相对位置移动
		# pyautogui.moveRel(10, 10, duration=2) # 相对位置移动
		time.sleep(2)
		# pyautogui.press('#')
		pyautogui.click()

if __name__ == '__main__':
	main()
