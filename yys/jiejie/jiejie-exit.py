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

	attackImg = Image.open("img/attack.png")
	noattackImg = Image.open("img/medal.png")
	shibaiImg = Image.open("img/shibai.png")
	tuichuImg = Image.open("img/退出.png")
	querenImg = Image.open("img/确认.png")
	while shibaicount<9:
		if button(noattackImg,pos):
			sleep(1)
			if button(attackImg,pos):
				sleep(2)
		# 点击退出
		if button(tuichuImg,pos):
			sleep(2)
		# 点击确认
		if button(querenImg,pos):
			sleep(4)
		if button(shibaiImg,pos):
			sleep(1)
			shibaicount=shibaicount+1
			print("shibai count:{}".format(shibaicount))
		sleep(1)

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
