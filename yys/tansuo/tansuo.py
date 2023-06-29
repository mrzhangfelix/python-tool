import time

from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import win32api,win32con,win32gui
import logging
from threading import Thread


LOG_FILE = 'mylog.log'
file_handler = logging.FileHandler(LOG_FILE) #输出到文件
console_handler = logging.StreamHandler()  #输出到控制台
file_handler.setLevel('INFO')     #error以上才输出到文件
console_handler.setLevel('INFO')   #info以上才输出到控制台
fmt = '%(asctime)s - %(funcName)s - %(lineno)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(fmt)
file_handler.setFormatter(formatter) #设置输出内容的格式
console_handler.setFormatter(formatter)

logger = logging.getLogger('updateSecurity')
logger.setLevel('INFO')     #设置了这个才会把debug以上的输出到控制台
logger.addHandler(file_handler)    #添加handler
logger.addHandler(console_handler)
jieshouImg = Image.open("接受.png")

tiaozhanTotalCount=0
tansuoTotalCount=0

def jieshouyaoqing():
	tiaozhanTotalCountTemp=0
	tansuoTotalCountTemp=0
	while True:
		if button(jieshouImg):
			logger.error("接受悬赏邀请")
		if tiaozhanTotalCountTemp!=tansuoTotalCount or tansuoTotalCountTemp!=tansuoTotalCount:
			tiaozhanTotalCountTemp=tiaozhanTotalCount
			tansuoTotalCountTemp=tansuoTotalCount
			logger.info("挑战结界总共 {} 次，探索总共 {} 次"
						.format(tiaozhanTotalCountTemp,tansuoTotalCountTemp))
		sleep(5)

pos=(0,0,1720,968)

def main():
	thread1=Thread(name='jieshouyaoqing', target=jieshouyaoqing)
	thread1.start()
	# 打开窗口在固定位置
	get_window_pos("阴阳师 - MuMu模拟器",pos)

	while True:
		doJiejie()
		doTansou(50)


def doJiejie():
	logger.info("开始结界")
	attackImg = Image.open("jiejieImg/attack.png")
	noattackImg = Image.open("jiejieImg/medal.png")
	endImg = Image.open("jiejieImg/end.png")
	shibaiImg = Image.open("jiejieImg/shibai.png")
	kaishiImg = Image.open("jiejieImg/打开结界突破.png")
	guanbiImg = Image.open("jiejieImg/关闭结界突破.png")
	shuaxinImg = Image.open("jiejieImg/刷新.png")
	quedingImg = Image.open("jiejieImg/确定退出.png")
	# tuichuImg = Image.open("jiejieImg/退出.png")
	# querenImg = Image.open("jiejieImg/确认.png")
	# kongImg = Image.open("jiejieImg/空勋章.png")
	button(kaishiImg)
	sleep(1)
	chenggongCount=0
	shibaicount=0
	tiaozhancount=1
	while True:
		# 空勋章的刷新逻辑
		# if find(kongImg):
		# 	logger.info("存在空勋章")
		# 	loopcount=0
		# 	while shibaicount<9:
		# 		if button(noattackImg):
		# 			sleep(1)
		# 			if button(attackImg):
		# 				sleep(2)
		# 				if find(attackImg):
		# 					logger.info("挑战券数量为0")
		# 					while button(guanbiImg):
		# 						sleep(1)
		# 					return
		# 				sleep(2)
		# 		# 点击退出
		# 		if button(tuichuImg):
		# 			sleep(2)
		# 		# 点击确认
		# 		if button(querenImg):
		# 			sleep(4)
		# 		if button(shibaiImg):
		# 			sleep(1)
		# 			shibaicount=shibaicount+1
		# 			logger.info("主动退出次数:{}".format(shibaicount))
		# 		sleep(5)
		# 		loopcount=loopcount+1
		# 		if(loopcount>30):
		# 			logger.error("循环次数过多，异常情况，刷新")
		# 			break
		# 	shibaicount=0
		# 	buttonshuaxin(quedingImg, shuaxinImg)
		# 	continue

		if button(noattackImg):
			logger.info("第{}次选择挑战".format(tiaozhancount))
			sleep(1)
			if button(attackImg):
				logger.info("开始第{}次进攻".format(tiaozhancount))
				sleep(2)
				if find(attackImg):
					logger.info("挑战券数量为0")
					while button(guanbiImg):
						logger.info("第{}次，挑战结束关闭".format(tiaozhancount))
						sleep(1)
					return
				sleep(10)
				while True:
					if button(endImg):
						logger.info("第{}次，挑战成功".format(tiaozhancount))
						sleep(1)
						while button(endImg):
							logger.info("第{}次，挑战成功".format(tiaozhancount))
							sleep(1)
						chenggongCount = chenggongCount + 1
						tiaozhancount =tiaozhancount +1
						global tiaozhanTotalCount
						tiaozhanTotalCount=tiaozhanTotalCount+1
						logger.info("成功突破:{}".format(chenggongCount))
						sleep(1)
						break
					if button(shibaiImg):
						logger.info("第{}次，挑战失败".format(tiaozhancount))
						sleep(1)
						while button(shibaiImg):
							logger.info("第{}次，挑战失败".format(tiaozhancount))
							sleep(1)
						shibaicount = shibaicount + 1
						tiaozhancount =tiaozhancount +1
						logger.info("失败突破次数:{}".format(shibaicount))
						sleep(1)
						break
					# logger.info("第{}次，正在挑战中".format(tiaozhancount))
					sleep(5)
		# logger.info("第{}次挑战结界中".format(tiaozhancount))
		sleep(3)
		if not find(noattackImg) and find(shuaxinImg):
			logger.error("没有可以挑战的结界，存在挑战失败")
			buttonshuaxin(quedingImg, shuaxinImg)
	button(guanbiImg)

def doTansou(n):
	logger.info("开始探索")
	leaderCount=1
	attackCount=1
	attackImg = Image.open("tansuoImg/attack.png")
	attackLeaderImg = Image.open("tansuoImg/attackLeader.png")
	pickUpImg = Image.open("tansuoImg/pickUp.png")
	exploreImg = Image.open("tansuoImg/explore.png")
	jieshuImg = Image.open("tansuoImg/结束探索.png")
	while True:
		global tansuoTotalCount
		if button(attackLeaderImg):
			logger.info("attackLeader次数:" + str(leaderCount))
			leaderCount = leaderCount + 1
			tansuoTotalCount=tansuoTotalCount+1
			time.sleep(5)
			continue
		if button(attackImg):
			logger.info("attack次数:" + str(attackCount))
			attackCount = attackCount + 1
			tansuoTotalCount=tansuoTotalCount+1
			time.sleep(5)
			continue
		if button(pickUpImg):
			pyautogui.moveTo(1500, 720)
			pyautogui.click()
			continue
		if find(exploreImg) and attackCount > n:
			button(jieshuImg)
			time.sleep(2)
			break
		if button(exploreImg):
			time.sleep(2)
			continue
		# X: 2196 , Y:  809
		pyautogui.moveTo(1500, 720)
		pyautogui.click()
		time.sleep(2)

def buttonshuaxin(quedingImg, shuaxinImg):
	if button(shuaxinImg):
		logger.info("刷新")
		sleep(1)
		if button(quedingImg):
			logger.info("刷新成功")
			sleep(5)
	else:
		logger.info("刷新冷却中")
		while not button(shuaxinImg):
			logger.info("没有找到刷新按钮")
			sleep(30)
		if button(quedingImg):
			logger.info("刷新成功")
			sleep(2)

def button(Img):
	msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True,region=pos)
	if msg == None:
		return False
	else:
		x, y, width, height = msg
		# logger.info("X={},Y={}，宽{}像素,高{}像素".format(x, y, width, height))
		center=pyautogui.center((x,y,width,height))
		pyautogui.click(center)
		return True

def find(Img):
	msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True,region=pos)
	if msg == None:
		return False
	else:
		return True

def find0(Img):
	msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=False,region=pos)
	if msg == None:
		return False
	else:
		return True

def get_window_pos(name,pos):
	handle = win32gui.FindWindow(0, name)
	# 获取窗口句柄
	if handle == 0:
		logger.info("not found windows")
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
		logger.info('已启动【'+str(tit)+'】窗口')
		logger.info('-----------------')


if __name__ == '__main__':
	main()
