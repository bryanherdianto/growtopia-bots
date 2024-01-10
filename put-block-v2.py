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

def needRefill(farmable_kind):
    if farmable_kind == 'chand':
        # check if there is still chand in inventory
        chand_block = pyautogui.locateCenterOnScreen('./assets/chand.png', confidence=0.95)
        if chand_block is None:
            return False
    elif farmable_kind == 'ftank':
        # check if there is still ftank in inventory
        ftank_block = pyautogui.locateCenterOnScreen('./assets/ftank.png', confidence=0.95)
        if ftank_block is None:
            return False
    return True

def refillBlocks(jumps, farmable_kind):
    respawn()
    pyautogui.sleep(4)

    # move left to the chand vending machine
    pydirectinput.press('left', presses=4)

    # change to wrench
    pydirectinput.leftClick(491, 933)

    # get blocks from vend
    try:
        face = pyautogui.locateCenterOnScreen('./assets/gt-body-left.png', confidence=0.85)
        if face is None:
            face = pyautogui.locateCenterOnScreen('./assets/gt-body-right.png', confidence=0.85)
    except:
        pyautogui.sleep(1)
        face = pyautogui.locateCenterOnScreen('./assets/gt-body-left.png', confidence=0.85)
        if face is None:
            face = pyautogui.locateCenterOnScreen('./assets/gt-body-right.png', confidence=0.85)
    pydirectinput.leftClick(x=face[0], y=face[1])
    pyautogui.sleep(3)

    # click 'empty the machine'
    empty = pyautogui.locateCenterOnScreen('./assets/empty-machine.png', minSearchTime=2, confidence=0.9)
    try:
        pydirectinput.leftClick(x=empty[0], y=empty[1])
    except:
        pyautogui.sleep(2)
        empty = pyautogui.locateCenterOnScreen('./assets/empty-machine.png', minSearchTime=2, confidence=0.9)
        pydirectinput.leftClick(x=empty[0], y=empty[1])

    # change to fist
    pyautogui.sleep(3)
    pydirectinput.leftClick(491, 933)
    pyautogui.sleep(3)

    # open inventory
    inventory = pyautogui.locateCenterOnScreen('./assets/inventory.png', confidence=0.95)
    pydirectinput.moveTo(x=inventory[0], y=inventory[1])
    pydirectinput.mouseDown(button='left')
    pydirectinput.moveTo(646, 256)
    pydirectinput.mouseUp(button='left')
    pyautogui.sleep(3)

    # click on block in inventory
    if farmable_kind == 'chand':
        # click on chand in inventory
        chand = pyautogui.locateCenterOnScreen('./assets/chand.png', minSearchTime=2, confidence=0.85)
        pydirectinput.leftClick(x=chand[0], y=chand[1])
    elif farmable_kind == 'ftank':
        # click on ftank in inventory
        ftank = pyautogui.locateCenterOnScreen('./assets/ftank.png', minSearchTime=2, confidence=0.85)
        pydirectinput.leftClick(x=ftank[0], y=ftank[1])
    pyautogui.sleep(3)

    # close inventory
    pydirectinput.moveTo(646, 256)
    pydirectinput.mouseDown(button='left')
    pydirectinput.moveTo(x=inventory[0], y=inventory[1])
    pydirectinput.mouseUp(button='left')
    pyautogui.sleep(3)

    # jump to the platform intended
    for i in range(jumps):
        pydirectinput.press('up', presses=2)
        pyautogui.sleep(0.5)

    # click on block in simplified inventory
    if farmable_kind == 'chand':
        # click on chand in simplified inventory
        chand = pyautogui.locateCenterOnScreen('./assets/chand.png', minSearchTime=2, confidence=0.85)
        pydirectinput.leftClick(x=chand[0], y=chand[1])
    elif farmable_kind == 'ftank':
        # click on ftank in simplified inventory
        ftank = pyautogui.locateCenterOnScreen('./assets/ftank.png', minSearchTime=2, confidence=0.85)
        pydirectinput.leftClick(x=ftank[0], y=ftank[1])

def puttingBlocks():
    # get character position
    face = pyautogui.locateCenterOnScreen('./assets/gt-body-left.png', confidence=0.85)
    if face is None:
        face = pyautogui.locateCenterOnScreen('./assets/gt-body-right.png', confidence=0.85)

    # move left
    pydirectinput.press('a', presses=2)

    # put chand on character position
    try:
        if face[0] < 1100:
            pydirectinput.leftClick(x=face[0]+110, y=face[1])
    except:
        pyautogui.sleep(2)
        face = pyautogui.locateCenterOnScreen('./assets/gt-body-left.png', confidence=0.85)
        if face is None:
            face = pyautogui.locateCenterOnScreen('./assets/gt-body-right.png', confidence=0.85)
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
    jumps = int(input())
    jumps += 1
    full = True

    # input kind of farmable (chand / ftank)
    farmable_kind = input()
    
    # delay 3 seconds
    pyautogui.sleep(3)

    while True:
        jumps = increaseJumps(jumps)

        full = needRefill(farmable_kind=farmable_kind)
        if full is False:
            refillBlocks(jumps=jumps, farmable_kind=farmable_kind)

        puttingBlocks()

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