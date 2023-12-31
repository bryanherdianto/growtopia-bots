import pydirectinput
import keyboard
import pyautogui

def main():
    pyautogui.sleep(4)

    while True:
        if keyboard.is_pressed('2'):
            exit()

        pydirectinput.press('down', 6)
        pydirectinput.press('left', 2)

        # error handling
        gem = pyautogui.screenshot(region=(1233, 522, 2, 2))
        for x in range(gem.width):
            for y in range(gem.height):
                if not gem.getpixel((x, y))[0] > 240:
                    exit()

if __name__ == '__main__':
    main()