import pydirectinput
import keyboard
import pyautogui
import time

def main():
    pyautogui.sleep(4)

    start_time = time.time()

    while True:
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
