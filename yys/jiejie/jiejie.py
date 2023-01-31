import time
from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import win32api,win32con,win32gui

# pyinstaller -F tansuo.py --path="C:\Users\felix\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2"

def main():
	count=0
	shibaicount=0
	pos=(0,0,1720,968)
	# 打开窗口在固定位置
	get_window_pos("阴阳师 - MuMu模拟器",pos)

	attackImg = Image.open("attack.png")
	noattackImg = Image.open("medal.png")
	endImg = Image.open("end.png")
	shibaiImg = Image.open("shibai.png")
	while True:
		if button(noattackImg,pos):
			print("点击noattack按钮")
			sleep(1)
			if button(attackImg,pos):
				print("点击attack按钮")
				sleep(5)
				# if button(attackImg,pos):
				# 	# 如果进攻按钮还在就说明没有挑战机会了，可以去做点别的事情
				# 	print("挑战测试用光，退出")
				# 	pyautogui.moveTo(1500,720)
				# 	pyautogui.click()
				# 	sleep(1800)
				# 	continue
		# else:
		# 	print("当前已经挑战完毕，可以刷新")
		# 	exit()
		if button(endImg,pos):
			while button(endImg,pos):
				sleep(1)
			print("点击end按钮")
			count=count+1
			print("chengong count:{}".format(count))
			sleep(1)
		if button(shibaiImg,pos):
			while button(shibaiImg,pos):
				sleep(1)
			print("点击shibai按钮")
			shibaicount=shibaicount+1
			print("shibai count:{}".format(shibaicount))
			sleep(1)
		sleep(2)

def button(Img,pos):
	msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True,region=pos)
	if msg == None:
		return False
	else:
		x, y, width, height = msg
		# print("X={},Y={}，宽{}像素,高{}像素".format(x, y, width, height))
		center=pyautogui.center((x,y,width,height))
		pyautogui.click(center)
		return True

def get_window_pos(name,pos):
	handle = win32gui.FindWindow(0, name)
	# 获取窗口句柄
	if handle == 0:
		print("not found windows")
		exit()
	else:
		# win32gui.SendMessage(handle,win32con.WM_SYSCOMMAND,win32con.SC_RESTORE,0)
		#发送还原最小化窗口的信息
		win32gui.ShowWindow(handle, win32con.SW_SHOWMINIMIZED)
		win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)
		win32gui.ShowWindow(handle, win32con.SW_SHOW)
		win32gui.SetWindowPos(handle, win32con.HWND_TOP, pos[0], pos[1], pos[2], pos[3], win32con.SWP_SHOWWINDOW)
		win32gui.SetForegroundWindow(handle)  # 获取控制
		time.sleep(1)
		# 窗口的标题
		tit = win32gui.GetWindowText(handle)
		# 窗口的坐标
		(x1, y1, x2, y2)=win32gui.GetWindowRect(handle)
		print('已启动【'+str(tit)+'】窗口')
		print('-----------------')


if __name__ == '__main__':
	main()
