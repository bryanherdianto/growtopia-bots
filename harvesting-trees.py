import pydirectinput
import keyboard
import pyautogui

def main():
    pyautogui.sleep(4)

    while True:
        if keyboard.is_pressed('2'):
            exit()

        keyboard.press('a')

if __name__ == '__main__':
    main()