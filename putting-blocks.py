import pydirectinput
import keyboard
import pyautogui

portalColor = (11, 100, 255)
updated = False

def respawn():
    pyautogui.click(1209, 94)
    pyautogui.click(639, 299)

def needRefill():
    inventory = pyautogui.screenshot(region=(794, 931, 2, 2))
    for x in range(inventory.width):
        for y in range(inventory.height):
            if inventory.getpixel((x, y))[0] > 240:
                return True
    return False

def refillBlocks(jumps):
    respawn()
    pyautogui.sleep(3)
    pydirectinput.press('left', presses=7)
    for i in range(jumps):
        if i == 0:
            pydirectinput.press('up', presses=3)
            pyautogui.sleep(0.5)
            continue
        pydirectinput.press('up', presses=2)
        pyautogui.sleep(0.5)
    pydirectinput.leftClick(794, 931)

def puttingBlocks():
    pydirectinput.press('left', presses=2)
    pydirectinput.leftClick(800, 500)

def increaseJumps(jumps):
    global updated
    block = pyautogui.screenshot(region=(36, 554, 2, 2))

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
    full = True
    
    pyautogui.sleep(3)

    while True:
        jumps = increaseJumps(jumps)

        full = needRefill()
        if full is False:
            refillBlocks(jumps=jumps)

        puttingBlocks()

        if keyboard.is_pressed('2'):
            exit()

if __name__ == '__main__':
    main()