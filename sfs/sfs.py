import keyboard
import pyautogui as pp
import time

play = 1896,1038
def brain():
    time.sleep(10)
    pp.keyDown("e")
    time.sleep(2)
    pp.keyUp("e")
    time.sleep(20)
    pp.keyDown("e")
    time.sleep(2)
    pp.keyUp("e")
    time.sleep(13)
    pp.hotkey('x')
    pp.click(play)
    pp.click(play)
    time.sleep(30)
    pp.keyDown("e")
    time.sleep(7)
    pp.keyUp("e")
    pp.hotkey('z')
    time.sleep(7)
    pp.hotkey('x')
    pp.click(play)
    pp.click(play)
    pp.click(play)
    pp.click(play)
    pp.keyDown("e")
    time.sleep(4)
    pp.keyUp("e")
    pp.hotkey('z')
    time.sleep(10)
    pp.keyDown("e")
    time.sleep(3)
    pp.keyUp("e")
    pp.hotkey('z')
    time.sleep(25)
    pp.hotkey("x")
    pp.click(play)
    time.sleep(3)
    pp.hotkey("m")
    time.sleep(1)
    pp.hotkey("m")
    print("you have reached orbit!")



def launch():
    time.sleep(1.5)
    pp.scroll(-90000)
    pp.scroll(-90000)
    pp.scroll(-90000)
    pp.scroll(-90000)
    pp.scroll(-90000)
    pp.keyDown("shift")
    time.sleep(2)
    pp.keyUp("shift")
    pp.click(play)
    pp.click(play)
    pp.hotkey("space")
    brain()



def med():
    pp.hotkey("esc")
    time.sleep(0.3)
    pp.click(1046,293)
    pp.click(1046,293)
    x = pp.locateOnScreen('ff.png', confidence = 0.6)
    if x != None:
        pp.click(x)
        pp.click(x)
    else:
        x = pp.locateOnScreen('ff.png', confidence = 0.6)
        print("coulndt locate faf")
        time.sleep(0.5)

    pp.click(1237,847)
    pp.click(1237,847)
    pp.moveTo(1884,21)
    pp.click()
    pp.click()
    pp.click(1068,603)
    pp.click(1068,603)
    launch()



while not keyboard.is_pressed('x'):
    if keyboard.is_pressed('o'):
        med()
    if keyboard.is_pressed('p'):
        launch()