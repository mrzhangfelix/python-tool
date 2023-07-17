import pyautogui
import sys
import os
import constant


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 判断sys中是否存在frozen变量,即是否是打包程序
        base_path = sys._MEIPASS  # sys._MEIPASS在一些编辑器中会报错，不用理会
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def buttonWithPos(Img, pos):
    msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True, region=pos)
    if msg == None:
        return False
    else:
        x, y, width, height = msg
        # print("X={},Y={}，宽{}像素,高{}像素".format(x, y, width, height))
        center = pyautogui.center((x, y, width, height))
        pyautogui.click(center)
        return True


def button(Img):
    return buttonWithPos(Img, (0, 0, constant.resolution_x, constant.resolution_y))


def find(Img):
    msg = pyautogui.locateOnScreen(Img,
                                   confidence=0.9,
                                   grayscale=True,
                                   region=(0, 0, constant.resolution_x, constant.resolution_y))
    if msg == None:
        return False
    else:
        return True


def click():
    pyautogui.click(constant.ready_x, constant.ready_y)


def clickPos(x, y):
    pyautogui.click(x, y)


def autoAlert(msg):
    pyautogui.alert(msg)
