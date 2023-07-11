#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import time
import tkinter as tk
from threading import Thread
from threading import Event

import jiejieExit
from yys.client import win32guiUtil

# 日志处理的类
class TextboxHander(logging.Handler):
    def __init__(self, textbox):
        logging.Handler.__init__(self)
        self.textbox = textbox

    def emit(self, record):
        msg = self.format(record)
        self.textbox.delete("1.0", "end")
        self.textbox.insert("end", msg + "\n")


class App:
    def threadTest(self, event):
        for i in range(100):
            if event.is_set():
                print("tread is stopping")
                self.log.info("tread is stopping" + str(i))
                break
            time.sleep(1)
            print("tread is running")
            self.log.info("tread is running" + str(i))

    def threadJieJieExit(self, event,ExitCount):
        jiejie_exit = jiejieExit.jiejieExit()
        pos = (0, 0, 1720, 968)
        # 打开窗口在固定位置
        win32guiUtil.get_window_pos("阴阳师 - MuMu模拟器", pos)
        shibaiCount=0
        while shibaiCount<int(ExitCount):
            if event.is_set():
                self.log.info("JieJieExit is stopping,shibaicount:" + str(shibaiCount))
                break
            time.sleep(1)
            shibaiCount = jiejie_exit.dowork()
            self.log.info("JieJieExit is running,shibaicount:" + str(shibaiCount))

    def start(self, startType):
        self.event.clear()
        # daemon 表示 主线程不需要等待子线程结束才能结束，如果daemon等于flase(默认)，那么结束主进程会去等子进程结束
        if startType == 1:
            print(self.entryExitCount.get())
            self.thread1 = Thread(name='jiejieExitThread', target=self.threadJieJieExit, args=(self.event,self.entryExitCount.get()), daemon=True)
        self.thread1.start()

    def end(self):
        self.log.info("end all task")
        self.event.set()

    def __init__(self, window):
        window.title("yyds")
        # 控制线程终止
        self.event = Event()
        # jiejieExit功能1
        frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame1.grid(row=0, column=0)
        labelJiejieExit = tk.Label(master=frame1, text="结界退出：",background="red")
        labelExitCount = tk.Label(master=frame1, text="退出次数")
        self.entryExitCount = tk.Entry(master=frame1, width=20)
        startBtn = tk.Button(master=frame1, text="start", width=20, command=lambda: self.start(1))

        labelJiejieExit.pack(side=tk.LEFT)
        labelExitCount.pack(side=tk.LEFT)
        self.entryExitCount.pack(side=tk.LEFT)
        startBtn.pack(side=tk.LEFT)

        # 功能2
        frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame2.grid(row=1, column=0)

        label2 = tk.Label(master=frame2, text="文本标签")
        entry2 = tk.Entry(master=frame2, width=20)
        startBtn2 = tk.Button(master=frame2, text="Click me!", width=20)

        label2.pack(side=tk.LEFT)
        entry2.pack(side=tk.LEFT)
        startBtn2.pack(side=tk.LEFT)

        logFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        logFrame.grid(row=2, column=0)
        logLabel = tk.Label(master=logFrame, text="日志", width=10)
        logLabel.pack(side=tk.LEFT)
        logText = tk.Text(master=logFrame, width=50, height=5)
        logText.pack(side=tk.LEFT)

        self.log = logging.getLogger("log")
        self.log.setLevel(logging.INFO)
        handler = TextboxHander(logText)
        self.log.addHandler(handler)

        endFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        endFrame.grid(row=3, column=0)
        endBtn = tk.Button(master=endFrame, text="end", width=20, command=self.end)
        endBtn.pack(side=tk.LEFT)


def main():
    window = tk.Tk()
    app = App(window)
    window.mainloop()


if __name__ == '__main__':
    main()
