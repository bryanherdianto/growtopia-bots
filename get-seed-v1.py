'''
v1 is used for a different growtopia world: TYANDEL
'''

import pyautogui
import keyboard
import pydirectinput
import time

portalColor = (11, 100, 255)
updated = False

def respawn():
    pyautogui.click(1209, 94)
    pyautogui.click(639, 299)

def chand_seed_is_full():
    # check if there is already 200 chand seed in inventory
    chand_seed_inventory = pyautogui.locateCenterOnScreen('./assets/chand-seed-200.png', confidence=0.95)
    if chand_seed_inventory is None:
        return False
    return True

def loadSeed(jumps):
    # stop moving
    pydirectinput.keyUp('a')

    respawn()
    pyautogui.sleep(4)

    # move left to the chand seed vending machine
    pydirectinput.press('left', presses=6)
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
    wrench_inventory = pyautogui.locateCenterOnScreen('./assets/wrench-inventory.png', confidence=0.95)
    if wrench_inventory is None:
        pydirectinput.leftClick(491, 933)

    # load seed to vend
    try:
        face = pyautogui.locateCenterOnScreen('./assets/gt-body-left.png', confidence=0.85)
        if face is None:
            face = pyautogui.locateCenterOnScreen('./assets/gt-body-right.png', confidence=0.85)
    except:
        pyautogui.sleep(1)
        face = pyautogui.locateCenterOnScreen('./assets/gt-body-left.png', confidence=0.85)
        if face is None:
            face
    pydirectinput.leftClick(x=face[0], y=face[1])
    pyautogui.sleep(3)

    # get coordinates of 'put item' button
    put_item = pyautogui.locateCenterOnScreen('./assets/put-item.png', confidence=0.9)
    if put_item is None:
        # click 'add to machine'
        add = pyautogui.locateCenterOnScreen('./assets/add-machine.png', confidence=0.95)
        pydirectinput.leftClick(x=add[0], y=add[1])
    else:
        # click 'put item to machine'
        pydirectinput.leftClick(x=put_item[0], y=put_item[1])

        chand_seed_inventory = pyautogui.locateCenterOnScreen('./assets/chand-seed-200.png', confidence=0.95)
        pydirectinput.leftClick(x=chand_seed_inventory[0], y=chand_seed_inventory[1])

    pyautogui.sleep(3)
    if jumps == 0:
        pydirectinput.press('left', presses=6)
        pydirectinput.press('up', presses=1)
    elif jumps > 0:
        for i in range(0, jumps):
            if i == 0:
                pydirectinput.press('up', presses=3)
                pyautogui.sleep(0.5)
                continue
            pydirectinput.press('up', presses=2)
            pyautogui.sleep(0.5)

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
    start_time = time.time()

    print("Input at what level you are: ")
    jumps = int(input())
    full = True

    pyautogui.sleep(3)

    while True:
        jumps = increaseJumps(jumps)

        full = chand_seed_is_full()
        if full is True:
            loadSeed(jumps=jumps)

        # move left
        pydirectinput.keyDown('a')

        if keyboard.is_pressed('2'):
            pydirectinput.keyUp('a')
            exit()

        if int(time.time() - start_time) % 15 == 0:
            pydirectinput.keyUp('a')
            pydirectinput.keyDown('a')

        # error handling
        gem = pyautogui.screenshot(region=(1233, 522, 2, 2))
        for x in range(gem.width):
            for y in range(gem.height):
                if not gem.getpixel((x, y))[0] > 240:
                    exit()

if __name__ == '__main__':
    main()
