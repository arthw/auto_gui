import pyautogui as gui

import time

def startup_app(image_path):
    gui.hotkey('win', 'm')
    time.sleep(1)
    scn = gui.locateOnScreen(image_path)
    center = gui.center(scn)
    gui.doubleClick(center)

def main():
    startup_app('app.png')

if __name__=='__main__':
    main()