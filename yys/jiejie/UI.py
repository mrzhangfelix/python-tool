#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import threading
import time
import urllib

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QAction, QProgressBar,
                             QTextEdit, QGridLayout, QApplication)

import jiejie


# UI界面绘制
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # 定义变量
        self.label1 = QLabel('等待分钟数')
        self.label2 = QLabel('突破次数')
        self.info = QLabel('信息')

        self.delayEdit = QLineEdit("0")
        self.countEdit = QLineEdit("666")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.label1, 1, 0)
        grid.addWidget(self.delayEdit, 1, 1)

        grid.addWidget(self.label2, 2, 0)
        grid.addWidget(self.countEdit, 2, 1)

        grid.addWidget(self.info, 3, 0)

        self.btn = QPushButton('Start', self)
        # self.btn.move(65, 230)
        self.btn.clicked.connect(self.doAction)
        grid.addWidget(self.btn, 4, 0)
        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('yys')
        self.show()


    def doAction(self):
        delay = self.delayEdit.text()
        count = self.countEdit.text()
        self.info.setText('开始结界突破')
        jiejie.main(int(delay),int(count))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
