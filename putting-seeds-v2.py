'''
v2 is used for a different growtopia world: ANEDSD
'''

import pydirectinput
import keyboard
import pyautogui

portalColor = (11, 100, 255)
updated = False

def respawn():
    pyautogui.click(1209, 94)
    pyautogui.click(639, 299)

def needRefill():
    # check if there is still chand seed in inventory
    chand_seed = pyautogui.locateCenterOnScreen('chand-seed.png', confidence=0.95)
    if chand_seed is None:
        return False
    return True

def refillSeeds(jumps):
    respawn()
    pyautogui.sleep(4)

    # move left to the chand seed vending machine
    pydirectinput.press('a', presses=6)
    while True:
        try:
            face = pyautogui.locateCenterOnScreen('gt-body-left.png', confidence=0.85)
            if face is None:
                face = pyautogui.locateCenterOnScreen('gt-body-right.png', confidence=0.85)
        except:
            pyautogui.sleep(1)
            face = pyautogui.locateCenterOnScreen('gt-body-left.png', confidence=0.85)
            if face is None:
                face = pyautogui.locateCenterOnScreen('gt-body-right.png', confidence=0.85)
        pyautogui.sleep(1)
        if face[0] < 970:
            pydirectinput.press('d', presses=1)
        elif face[0] > 1020:
            pydirectinput.press('a', presses=1)
        else:
            break

    # change to wrench
    wrench_inventory = pyautogui.locateCenterOnScreen('wrench-inventory.png', confidence=0.9)
    if wrench_inventory is None:
        pydirectinput.leftClick(491, 933)

    # get chand seed from vend
    try:
        face = pyautogui.locateCenterOnScreen('gt-body-left.png', confidence=0.85)
        if face is None:
            face = pyautogui.locateCenterOnScreen('gt-body-right.png', confidence=0.85)
    except:
        pyautogui.sleep(1)
        face = pyautogui.locateCenterOnScreen('gt-body-left.png', confidence=0.85)
        if face is None:
            face = pyautogui.locateCenterOnScreen('gt-body-right.png', confidence=0.85)
    pydirectinput.leftClick(x=face[0], y=face[1])
    pyautogui.sleep(3)

    # click 'empty the machine'
    empty = pyautogui.locateCenterOnScreen('empty-machine.png', minSearchTime=2, confidence=0.9)
    try:
        pydirectinput.leftClick(x=empty[0], y=empty[1])
    except:
        pyautogui.sleep(2)
        empty = pyautogui.locateCenterOnScreen('empty-machine.png', minSearchTime=2, confidence=0.9)
        pydirectinput.leftClick(x=empty[0], y=empty[1])

    # change to fist
    pyautogui.sleep(3)
    pydirectinput.leftClick(491, 933)
    pyautogui.sleep(3)

    # open inventory
    inventory = pyautogui.locateCenterOnScreen('inventory.png', confidence=0.95)
    pydirectinput.moveTo(x=inventory[0], y=inventory[1])
    pydirectinput.mouseDown(button='left')
    pydirectinput.moveTo(646, 256)
    pydirectinput.mouseUp(button='left')
    pyautogui.sleep(3)

    # click on chand seed in inventory
    chand = pyautogui.locateCenterOnScreen('chand-seed.png', minSearchTime=2, confidence=0.85)
    pydirectinput.leftClick(x=chand[0], y=chand[1])
    pyautogui.sleep(3)

    # close inventory
    pydirectinput.moveTo(646, 256)
    pydirectinput.mouseDown(button='left')
    pydirectinput.moveTo(x=inventory[0], y=inventory[1])
    pydirectinput.mouseUp(button='left')
    pyautogui.sleep(3)

    for i in range(jumps):
        pydirectinput.press('up', presses=2)
        pyautogui.sleep(0.5)

    # click on chand seed
    chand = pyautogui.locateCenterOnScreen('chand-seed.png', minSearchTime=2, confidence=0.85)
    pydirectinput.leftClick(x=chand[0], y=chand[1])

def puttingSeeds():
    # get character position
    face = pyautogui.locateCenterOnScreen('gt-body-left.png', confidence=0.85)
    if face is None:
        face = pyautogui.locateCenterOnScreen('gt-body-right.png', confidence=0.85)

    # move left
    pydirectinput.press('a', presses=2)

    # put chand on character position
    try:
        if face[0] < 1100:
            pydirectinput.leftClick(x=face[0]+110, y=face[1])
    except:
        pyautogui.sleep(2)
        face = pyautogui.locateCenterOnScreen('gt-body-left.png', confidence=0.85)
        if face is None:
            face = pyautogui.locateCenterOnScreen('gt-body-right.png', confidence=0.85)
        if face[0] < 1100:
            pydirectinput.leftClick(x=face[0]+110, y=face[1])

def increaseJumps(jumps):
    global updated
    block = pyautogui.screenshot(region=(36, 554, 2, 2))

    # increase jump if there is portal in screen
    for x in range(block.width):
        for y in range(block.height):
            if block.getpixel((x, y)) == portalColor and updated is False:
                updated = True
                return jumps + 1
            if block.getpixel((x, y)) != portalColor:
                updated = False
    return jumps

def main():
    print("Input at what level you are: ")
    jumps = int(input())
    jump += 1
    full = True

    print("... Now let the program do all the work :) ...")
    
    # delay 3 seconds
    pyautogui.sleep(3)

    while True:
        jumps = increaseJumps(jumps)

        full = needRefill()
        if full is False:
            refillSeeds(jumps=jumps)

        puttingSeeds()

        if keyboard.is_pressed('2'):
            exit()

        # error handling
        gem = pyautogui.screenshot(region=(1233, 522, 2, 2))
        for x in range(gem.width):
            for y in range(gem.height):
                if not gem.getpixel((x, y))[0] > 240:
                    exit()

if __name__ == '__main__':
    main()