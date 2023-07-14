import pyautogui

def buttonWithPos(Img,pos):
    msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True,region=pos)
    if msg == None:
        return False
    else:
        x, y, width, height = msg
        # print("X={},Y={}，宽{}像素,高{}像素".format(x, y, width, height))
        center=pyautogui.center((x,y,width,height))
        pyautogui.click(center)
        return True
def button(Img):
    buttonWithPos(Img,(0,0,1720,968))

def find(Img):
    msg = pyautogui.locateOnScreen(Img, confidence=0.9, grayscale=True,region=(0,0,1720,968))
    if msg == None:
        return False
    else:
        return True

def click():
    pyautogui.click(1500,720)