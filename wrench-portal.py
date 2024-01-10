'''
The character needs to be in maximum zoom for the program to work
'''

import pydirectinput
import pyautogui

count = 1

# there are usually 25 levels of platform
print("Input 'how many levels of platform are there' - 1 or press '0' to go till infinity:")
max = int(input())

pyautogui.sleep(3)

while True:
    # 1. Wrench the object first
    pydirectinput.leftClick(180, 700)

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