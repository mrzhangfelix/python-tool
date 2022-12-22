import pyautogui
import time
import operator
import ctypes, sys
import os

width, hight = pyautogui.size()
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def main():
	try:
		while True:
			print("start")
			# pyautogui.keyDown('t')
			pyautogui.press('t')
			time.sleep(1)
			# pyautogui.keyUp('t')
	except KeyboardInterrupt:
		print('Exit')

if __name__ == '__main__':
	time.sleep(2)
	main()
