import pyautogui
import time
from win32api import mouse_event, SetCursorPos, GetAsyncKeyState
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, VK_CAPITAL

'''
function to get position of mouse location until the CAPS LOCK key is pressed
'''
def getMouseLoc():
    while(GetAsyncKeyState(VK_CAPITAL) != 0):
        time.sleep(0.5)
        print(pyautogui.position())

'''
function that clicks on a location given by tuple tup
'''
def click(tup):
    x = tup[0]
    y = tup[1]
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0)

'''
main bot function
'''
def bot():
    # position of the right and left buttons to click
    lButton = (1485, 843)
    rButton = (1515, 840)
    # position of restart button after one match minimum
    restart = (1424, 932)
    # time from clicking restart to 
    triggerTime = 4.139949
    # key that will break the loop
    stopKey = 'K'

    click(restart)
    time.sleep(triggerTime)
    while(True):
        click(lButton)
        time.sleep(0.01)
        click(rButton)
        if GetAsyncKeyState(ord(stopKey)) != 0:
            break

bot()
