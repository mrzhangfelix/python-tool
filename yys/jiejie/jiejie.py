import time
from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import win32api,win32con,win32gui

def main():
	count=1
	pos=(0,0,1720,968)
	# 打开窗口在固定位置
	get_window_pos("MuMu模拟器",pos)

	attackImg = Image.open("attack.png")
	noattackImg = Image.open("medal.png")
	endImg = Image.open("end.png")
	while True:
		if button(noattackImg,pos):
			print("点击noattack按钮")
			sleep(1)
			if button(attackImg,pos):
				print("点击attack按钮")
				sleep(10)
		if button(endImg,pos):
			print("点击end按钮")
			count=count+1
			print("count:{}".format(count))
			sleep(2)
		sleep(3)

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
