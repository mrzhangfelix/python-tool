import pyautogui

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