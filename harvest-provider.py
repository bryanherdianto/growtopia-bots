import pydirectinput
import keyboard
import pyautogui

def main():
    pyautogui.sleep(4)

    while True:
        if keyboard.is_pressed('2'):
            exit()

        pydirectinput.press('down', 1)
        pydirectinput.press('left', 2)

if __name__ == '__main__':
    main()