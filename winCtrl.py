import win32api,win32con,win32gui
import time

# 測試打開桌面窗口

def get_window_pos(name):
    handle = win32gui.FindWindow(0, '有道云笔记')
    # 获取窗口句柄
    if handle == 0:
        print("not found windows")
        return None
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



