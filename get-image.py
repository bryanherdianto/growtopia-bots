import pyautogui

while True:
    # delay 3 seconds
    pyautogui.sleep(3)

    # get the coordinates of the center of the image on the screen
    seed = pyautogui.locateCenterOnScreen('chand-seed.png')

    # print coordinates
    print(seed)