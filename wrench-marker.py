'''
The character needs to be in maximum zoom for the program to work
'''

import pydirectinput
import pyautogui

count = 1
max = int(input())

pyautogui.sleep(3)

while True:
    if count == max:
        pydirectinput.leftClick(1027, 238)
        pydirectinput.press("backspace", presses=15)
        pydirectinput.typewrite("naikturun" + str(count))
        pydirectinput.leftClick(442, 600)
        break

    # 1. Wrench the object first
    pydirectinput.leftClick(982, 463)

    # backspace all words first
    pydirectinput.press("backspace", presses=15)

    # 2. Type the words
    pydirectinput.typewrite("naikturun" + str(count))

    # 3. Press "OK"
    pydirectinput.leftClick(442, 600)
    pyautogui.sleep(1)
    
    # 4. Jump
    pydirectinput.press("up", presses=2)
    count = count + 1