import pyautogui
import time
import keyboard

ratio = 3.14
start_time = time.time()
speed_max = False
time_max = 140
time_passed = 0

# Testing If Record
time_all = time.time()
record_time = 0

# Main Loop
time.sleep(3)
while True:
    # Setting Up time_passed
    if not speed_max:
        time_passed = time.time() - start_time
        if time_passed > time_max:
            time_passed = time_max
            speed_max = True

    # Getting Screenshot and Background Color
    im = pyautogui.screenshot()
    screen = im.getpixel((250, 250))[0]

    # Jump Over Obstacles (Can Jump and Has Obstacles)
    if im.getpixel((136, 700)) != screen and im.getpixel((152, 721)) != screen:
        for i in range(510, 220 - round(ratio * time_passed), -5):
            if im.getpixel((i - 5 + ratio * time_passed, 680))[0] != screen or \
                    im.getpixel((i + 5 + ratio * time_passed, 600))[0] != screen:
                pyautogui.press('space')
                break

    # Checking if Exit (user exit or game ends)
    game_ends = im.getpixel((685, 466))[0]
    game_ends2 = im.getpixel((760, 466))[0]
    game_ends3 = im.getpixel((838, 466))[0]
    if keyboard.is_pressed('s'):
        break
    if (screen == 255 and (80 <= game_ends <= 85 and 80 <= game_ends2 <= 85 and 80 <= game_ends3 <= 85)) or \
            (screen == 0 and (170 <= game_ends <= 175 and 170 <= game_ends2 <= 175 and 170 <= game_ends3 <= 175)):
        current_time = time.time()
        break
    time.sleep(0.02)
