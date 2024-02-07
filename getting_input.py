import numpy as np
import cv2
import time
from PIL import ImageGrab
import pyautogui as mouse
play_button_img = cv2.imread("playbutton.png")
method = cv2.TM_SQDIFF_NORMED
previous_score_corner = ImageGrab.grab(bbox=(0,0,800,600))
def search_and_hit_play_button(game_grid):
    result = cv2.matchTemplate(play_button_img, np.array(game_grid), method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_loc)
    mouse.moveTo((max_loc[0]),600-max_loc[1])
    mouse.click()
time.sleep(10)
while True:
    game_grid = ImageGrab.grab(bbox=(0,0,800,600))
    score_corner = game_grid.crop(box=(700,40,800,100))
    if score_corner== previous_score_corner:
        time.sleep(2)
        search_and_hit_play_button(game_grid)
        print("Game Over biatch")

    previous_score_corner = score_corner
    cv2.imshow('screen', np.array(game_grid))
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWipndows()
        break
