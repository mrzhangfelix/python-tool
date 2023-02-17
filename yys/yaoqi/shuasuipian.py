import time
import pyautogui
from PIL import ImageGrab, Image
import win32api,win32con,win32gui

#刷碎片用
def main():
	# 状态 0：初始 1：组队界面 2：匹配中 3：战斗中 4：战斗结束
	a=1
	pos=(0,0,1720,968)
	# 打开窗口在固定位置
	get_window_pos("阴阳师 - MuMu模拟器",pos)

	teamUpImg = Image.open("teamUp.png")
	jieshouImg = Image.open("接受邀请.png")
	quxiaoImg = Image.open("是否邀请.png")
	prepareImg = Image.open("prepare.png")
	yaoqiImg = Image.open("yaoqi.png")
	jiaruImg = Image.open("jiaru.png")
	tianzhanImg = Image.open("tiaozhan.png")
	while True:
		if button(teamUpImg):
			time.sleep(0.5)
		if button(jieshouImg):
			time.sleep(1)
		if button(quxiaoImg):
			time.sleep(1)
		if button(tianzhanImg):
			time.sleep(1)
		if button(yaoqiImg):
			time.sleep(0.5)
			while button(jiaruImg):
				time.sleep(0.5)
			continue
		# if button(matchImg):
		# 	time.sleep(1)
		if button(prepareImg):
			# 确保战斗开始
			while button(prepareImg):
				time.sleep(1)
			print("开始次数:{}".format(a))
			a=a+1
			time.sleep(10)
		# if button(endImg):
		# 	time.sleep(1)
		# 	continue
		# 680,300 quanbu
		# 1400,300 jiaru
		# pyautogui.moveTo(1500,720)
		pyautogui.click(1500,720)
		time.sleep(1)

def button(Img):
	msg = pyautogui.locateOnScreen(Img, confidence=0.9)
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
