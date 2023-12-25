'''
The character needs to be in maximum zoom for the program to work
'''

import pydirectinput
import pyautogui

count = 1
max = int(input())

pyautogui.sleep(3)

while True:
    # 1. Wrench the object first
    pydirectinput.leftClick(180, 450)

    # click the chosen textbox
    pyautogui.sleep(1)
    pydirectinput.leftClick(452, 361)

    # backspace all words first
    pydirectinput.press("backspace", presses=15)

    # 2. Type the word
    pyautogui.keyDown("shift")
    pyautogui.typewrite(";")
    pyautogui.keyUp("shift")
    pydirectinput.typewrite("naikturun" + str(count))

    # 3. Press "OK"
    pydirectinput.leftClick(418, 797)
    pyautogui.sleep(1)
    if count == max:
        break

    # 4. Jump
    pydirectinput.press("up", presses=2)
    count = count + 1