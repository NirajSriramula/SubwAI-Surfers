import numpy as np
import cv2
import time
from PIL import ImageGrab
play_button_img = cv2.imread("playbutton.png")
method = cv2.TM_SQDIFF_NORMED
previous_score_corner = ImageGrab.grab(bbox=(0,0,800,600))
def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, [vertices], 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

# def search_and_hit_play_button(game_grid):
#     result = cv2.matchTemplate(play_button_img, np.array(game_grid), method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     print(max_loc)
#     mouse.moveTo((max_loc[0]),600-max_loc[1])
#     mouse.click()
#     #start_game_playing()
def process_img(original_img):
    # processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(original_img, 200, 300)
    listt = [[20,200],[620,200],[20,440],[620,440]]
    vertices = np.array(listt)
    processed_img = roi(processed_img, vertices)
    return processed_img
while True:
    game_grid = ImageGrab.grab(bbox=(0,0,640,480))
    score_corner = game_grid.crop(box=(560,40,640,80))
    image = np.array(game_grid)
    processed_img = process_img(image)

    if score_corner== previous_score_corner:
        time.sleep(2)
        #search_and_hit_play_button(game_grid)
        print("Game Over biatch")
    previous_score_corner = score_corner
    cv2.imshow('screen', processed_img)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWipndows()
        break
