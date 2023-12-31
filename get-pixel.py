import pyautogui

while True:
    pyautogui.sleep(3)

    posX,posY = pyautogui.position()

    block = pyautogui.screenshot(region=(posX, posY, 2, 2))
    
    for x in range(block.width):
        for y in range(block.height):
            print(f"({posX}, {posY}) --> {block.getpixel((x,y))}")