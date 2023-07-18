import time
import pyautogui
import keyboard


def getRealtimeMouseCoordinates():
    try:
        while True:
            if keyboard.wait(hotkey='ctrl+alt') is None:
                xNew, yNew = pyautogui.position()
                screenshot = pyautogui.screenshot()
                color = screenshot.getpixel((xNew, yNew))
                print('X:', '{:>4}'.format(xNew), ', Y:', '{:>4}'.format(yNew), ', RGB:',
                      '({:>3}, {:>3}, {:>3})'.format(color[0], color[1], color[2]))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Exit')


        
if __name__ == '__main__':
    getRealtimeMouseCoordinates()