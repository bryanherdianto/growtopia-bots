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
        # check if there is still chand seed in inventory
        chand_seed = pyautogui.locateCenterOnScreen('./assets/chand-seed.png', confidence=0.95)
        if chand_seed is None:
            return False
    elif farmable_kind == 'ftank':
        # check if there is still ftank seed in inventory
        ftank_seed = pyautogui.locateCenterOnScreen('./assets/ftank-seed.png', confidence=0.95)
        if ftank_seed is None:
            return False
    return True

def refillSeeds(jumps, farmable_kind):
    respawn()
    pyautogui.sleep(4)

    # move left to the chand seed vending machine
    pydirectinput.press('a', presses=6)
    while True:
        try:
            face = pyautogui.locateCenterOnScreen('./assets/gt-body-left.png', confidence=0.85)
            if face is None:
                face = pyautogui.locateCenterOnScreen('./assets/gt-body-right.png', confidence=0.85)
        except:
            pyautogui.sleep(1)
            face = pyautogui.locateCenterOnScreen('./assets/gt-body-left.png', confidence=0.85)
            if face is None:
                face = pyautogui.locateCenterOnScreen('./assets/gt-body-right.png', confidence=0.85)
        pyautogui.sleep(1)
        if face[0] < 970:
            pydirectinput.press('d', presses=1)
        elif face[0] > 1020:
            pydirectinput.press('a', presses=1)
        else:
            break

    # change to wrench
    wrench_inventory = pyautogui.locateCenterOnScreen('./assets/wrench-inventory.png', confidence=0.9)
    if wrench_inventory is None:
        pydirectinput.leftClick(491, 933)

    # get chand seed from vend
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

    # click on the seed in inventory
    if farmable_kind == 'chand':
        chand_seed = pyautogui.locateCenterOnScreen('./assets/chand-seed.png', minSearchTime=2, confidence=0.95)
        while chand_seed is None:
            pyautogui.moveTo(646, 700)
            pyautogui.scroll(-1)
            chand_seed = pyautogui.locateCenterOnScreen('./assets/chand-seed.png', minSearchTime=2, confidence=0.95)
        pydirectinput.leftClick(x=chand_seed[0], y=chand_seed[1])
    elif farmable_kind == 'ftank':
        ftank_seed = pyautogui.locateCenterOnScreen('./assets/ftank-seed.png', minSearchTime=2, confidence=0.95)
        while ftank_seed is None:
            pyautogui.moveTo(646, 700)
            pyautogui.scroll(-1)
            ftank_seed = pyautogui.locateCenterOnScreen('./assets/ftank-seed.png', minSearchTime=2, confidence=0.95)
        pydirectinput.leftClick(x=ftank_seed[0], y=ftank_seed[1])
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

    # click on the seed
    if farmable_kind == 'chand':
        chand_seed = pyautogui.locateCenterOnScreen('./assets/chand-seed.png', minSearchTime=2, confidence=0.95)
        pydirectinput.leftClick(x=chand_seed[0], y=chand_seed[1])
    elif farmable_kind == 'ftank':
        ftank_seed = pyautogui.locateCenterOnScreen('./assets/ftank-seed.png', minSearchTime=2, confidence=0.95)
        pydirectinput.leftClick(x=ftank_seed[0], y=ftank_seed[1])

def puttingSeeds():
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
    print("Input at what level you are: ")
    jumps = int(input())
    jumps += 1
    full = True

    # input kind of farmable (chand / ftank)
    farmable_kind = input()

    print("... Now let the program do all the work :) ...")
    
    # delay 3 seconds
    pyautogui.sleep(3)

    while True:
        jumps = increaseJumps(jumps)

        full = needRefill(farmable_kind)
        if full is False:
            refillSeeds(jumps=jumps, farmable_kind=farmable_kind)

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
