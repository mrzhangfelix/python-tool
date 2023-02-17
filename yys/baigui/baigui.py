import time
from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import win32api,win32con,win32gui

def main():
    count=1
    shibaicount=1
    pos=(0,0,1720,968)
    # 打开窗口在固定位置
    get_window_pos("阴阳师 - MuMu模拟器",pos)

    yaoqingImg = Image.open("邀请好友.png")
    jinruImg = Image.open("jinru.png")
    endImg = Image.open("end.png")
    jinxingzhongImg = Image.open("jinxingzhong.png")
    while True:
        if button(yaoqingImg,pos):
            sleep(1)
            # 选好友
            pyautogui.click(700,350)
            sleep(1)
        if button(jinruImg,pos):
            sleep(1)
            # 选鬼王
            pyautogui.click(850,600)
            sleep(1)
            pyautogui.click(1500,750)
            sleep(5)
        while cunzai(jinxingzhongImg,pos):
            pyautogui.click(900,500)
            sleep(0.5)
        if cunzai(endImg,pos):
            im=pyautogui.screenshot(region=pos)
            im.save('screenshot\\img{}.png'.format(time.strftime("%m%d-%H%M%S",time.localtime())))
            print('count:{}'.format(count))
            count=count+1
            pyautogui.click(230,400)
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

def cunzai(Img,pos):
    msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True,region=pos)
    if msg == None:
        return False
    else:
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
