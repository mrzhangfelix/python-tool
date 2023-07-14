import sys
from time import sleep
import pyautogui
from PIL import Image
import os

# 生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 判断sys中是否存在frozen变量,即是否是打包程序
        base_path = sys._MEIPASS # sys._MEIPASS在一些编辑器中会报错，不用理会
    else:
        base_path = os.path.abspath(".")
    print(base_path)
    return os.path.join(base_path, relative_path)

def main():
    print("开始工作")
    print(sys._MEIPASS)
    ceshiImg = Image.open(resource_path("ceshi.png"))
    print("加载图片成功")
    while True:
        button(ceshiImg)
        sleep(2)

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

def getImg(path):
    image_path = pkg_resources.resource_filename('my_package', path)
    image = Image.open(image_path)

if __name__ == '__main__':
    main()
