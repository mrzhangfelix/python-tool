import win32api,win32con,win32gui
import time

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