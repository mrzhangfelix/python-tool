#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import time
import tkinter as tk
from threading import Thread
from threading import Event

import jiejieExit
import jiejie
import clickService
import shuasuipian
import tansuo
from yys.client import win32guiUtil


startTime=time.time()
# 日志处理的类
class TextboxHander(logging.Handler):
    def __init__(self, textbox):
        logging.Handler.__init__(self)
        self.textbox = textbox

    def emit(self, record):
        msg = self.format(record)
        self.textbox.delete("1.0", "end")
        curTime=time.time()
        self.textbox.insert("end", "时间:{}分钟 msg:{}".format(round((curTime - startTime)/60,1),msg)+ "\n")


class App:
    def start(self, startType):
        self.event.clear()
        global startTime
        startTime=time.time()
        # 打开窗口在固定位置
        win32guiUtil.get_window_pos("阴阳师 - MuMu模拟器", (0, 0, 1720, 968))
        # daemon 表示 主线程不需要等待子线程结束才能结束，如果daemon等于flase(默认)，那么结束主进程会去等子进程结束
        if startType == 1:
            exitCount=self.entryExitCount.get()
            if exitCount == "":
                self.log.info("输入参数为空,默认退出9次")
                exitCount=9
            jiejie_exit = jiejieExit.jiejieExit()
            self.threadservice = Thread(name='jiejieExitThread', target=jiejie_exit.threadJieJieExit,
                                        args=(self,int(exitCount)), daemon=True)
        if startType == 2:
            jiejieService = jiejie.jiejie()
            delay_time = self.entryDelayTime.get()
            if delay_time=="":
                delay_time=0
            self.threadservice= Thread(name='jiejieThread', target=jiejieService.threadJieJie,
                                       args=(self, int(delay_time)), daemon=True)
        if startType == 3:
            click=clickService.clickService()
            self.threadservice= Thread(name='clickThread', target=click.threadclick,
                                       args=(self,), daemon=True)
        if startType == 4:
            suipianService = shuasuipian.yaoqi()
            self.threadservice= Thread(name='threadSuipian', target=suipianService.threadSuipian,
                                       args=(self,), daemon=True)
        if startType == 5:
            tansuoService = tansuo.tansuo()
            self.threadservice= Thread(name='threadHuijuan', target=tansuoService.threadHuijuan,
                                       args=(self,), daemon=True)
        self.threadservice.start()

    def end(self):
        self.log.info("end all task")
        self.event.set()

    def __init__(self, window):
        window.title("yyds")
        # 控制线程终止
        self.event = Event()
        rowNum=0

        # 结界退出功能
        frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame1.grid(row=rowNum, column=0)
        labelJiejieExit = tk.Label(master=frame1, text="结界退出：",background="red")
        labelExitCount = tk.Label(master=frame1, text="退出次数")
        self.entryExitCount = tk.Entry(master=frame1, width=20)
        startBtn = tk.Button(master=frame1, text="start jiejie Exit", width=20, command=lambda: self.start(1))

        labelJiejieExit.pack(side=tk.LEFT)
        labelExitCount.pack(side=tk.LEFT)
        self.entryExitCount.pack(side=tk.LEFT)
        startBtn.pack(side=tk.LEFT)

        # 寮结界突破功能
        rowNum+=1
        frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame2.grid(row=rowNum, column=0)

        label2 = tk.Label(master=frame2, text="延时")
        self.entryDelayTime = tk.Entry(master=frame2, width=20)
        startBtn2 = tk.Button(master=frame2, text="开始结界突破!", width=20,command=lambda: self.start(2))

        label2.pack(side=tk.LEFT)
        self.entryDelayTime.pack(side=tk.LEFT)
        startBtn2.pack(side=tk.LEFT)

        # 连续点击功能
        rowNum+=1
        frame3 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame3.grid(row=rowNum, column=0)

        startBtn2 = tk.Button(master=frame3, text="开始连续点击", width=20,command=lambda: self.start(3))
        startBtn2.pack(side=tk.LEFT)

        # 刷碎片功能
        rowNum+=1
        frame4 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame4.grid(row=rowNum, column=0)

        startBtn4 = tk.Button(master=frame4, text="开始刷碎片", width=20,command=lambda: self.start(4))
        startBtn4.pack(side=tk.LEFT)

        # 刷碎片功能
        rowNum+=1
        frame5 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame5.grid(row=rowNum, column=0)

        startBtn5 = tk.Button(master=frame5, text="开始刷绘卷", width=20,command=lambda: self.start(5))
        startBtn5.pack(side=tk.LEFT)

        # 日志显示
        rowNum+=1
        logFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        logFrame.grid(row=rowNum, column=0)
        logLabel = tk.Label(master=logFrame, text="日志", width=10)
        logLabel.pack(side=tk.LEFT)
        logText = tk.Text(master=logFrame, width=50, height=5)
        logText.pack(side=tk.LEFT)

        self.log = logging.getLogger("log")
        self.log.setLevel(logging.INFO)
        handler = TextboxHander(logText)
        self.log.addHandler(handler)

        #结束按钮
        rowNum+=1
        endFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        endFrame.grid(row=rowNum, column=0)
        endBtn = tk.Button(master=endFrame, text="end", width=20, command=self.end)
        endBtn.pack(side=tk.LEFT)

def main():
    window = tk.Tk()
    app = App(window)
    window.mainloop()


if __name__ == '__main__':
    main()
