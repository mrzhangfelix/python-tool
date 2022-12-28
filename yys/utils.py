import pyautogui
import win32api,win32con,win32gui
import time
from PIL import Image, ImageGrab
import pytesseract

# 点击图片的按钮
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

# 打开指定窗口
def get_window_pos(name):
    handle = win32gui.FindWindow(0, name)
    # 获取窗口句柄
    if handle == 0:
        print("not found windows")
    else:
        # win32gui.SendMessage(handle,win32con.WM_SYSCOMMAND,win32con.SC_RESTORE,0)
        #发送还原最小化窗口的信息
        win32gui.ShowWindow(handle, win32con.SW_SHOWMINIMIZED)
        time.sleep(1)
        win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)
        time.sleep(1)
        win32gui.ShowWindow(handle, win32con.SW_SHOW)
        time.sleep(1)
        win32gui.SetWindowPos(handle, win32con.HWND_TOP, 0, 0, 500, 700, win32con.SWP_SHOWWINDOW)
        time.sleep(1)
        win32gui.SetForegroundWindow(handle)  # 获取控制
        time.sleep(1)
        # 窗口的标题
        tit = win32gui.GetWindowText(handle)
        # 窗口的坐标
        (x1, y1, x2, y2)=win32gui.GetWindowRect(handle)
        print('已启动【'+str(tit)+'】窗口')
        print('-----------------')


# 抓取坐标文字并识别
def wenzishibie(x1, y1, x2, y2):
    img_ready = ImageGrab.grab((x1, y1, x2, y2))
    # 截图
    img_ready.show()
    # 读取图片
    # im = Image.open('medal.png')
    # 识别文字
    string = pytesseract.image_to_string(img_ready)
    print(string)
    return string
    # 展示