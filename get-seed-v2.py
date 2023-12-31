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
    chand_seed_inventory = pyautogui.locateCenterOnScreen('chand-seed-200.png', confidence=0.95)
    if chand_seed_inventory is None:
        return False
    return True

def loadSeed(jumps):
    # stop moving
    pydirectinput.keyUp('a')

    respawn()
    pyautogui.sleep(4)

    # move left to the chand vending machine
    pydirectinput.press('left', presses=6)

    # change to wrench
    wrench_inventory = pyautogui.locateCenterOnScreen('wrench-inventory.png')
    if wrench_inventory is None:
        pydirectinput.leftClick(491, 933)

    # load seed to vend
    try:
        face = pyautogui.locateCenterOnScreen('gt-body-left.png', confidence=0.85)
        if face is None:
            face = pyautogui.locateCenterOnScreen('gt-body-right.png', confidence=0.85)
    except:
        pyautogui.sleep(1)
        face = pyautogui.locateCenterOnScreen('gt-body-left.png', confidence=0.85)
        if face is None:
            face
    pydirectinput.leftClick(x=face[0], y=face[1])
    pyautogui.sleep(3)

    # get coordinates of 'put item' button
    put_item = pyautogui.locateCenterOnScreen('put-item.png', confidence=0.9)
    if put_item is None:
        # click 'add to machine'
        add = pyautogui.locateCenterOnScreen('add-machine.png', confidence=0.95)
        pydirectinput.leftClick(x=add[0], y=add[1])
    else:
        # click 'put item to machine'
        pydirectinput.leftClick(x=put_item[0], y=put_item[1])

    for i in range(jumps):
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

    jumps = int(input())
    jumps += 1
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