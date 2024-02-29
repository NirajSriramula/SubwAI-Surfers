import screenshots
import pygetwindow
from datetime import datetime
import time
import keyboard
cur_folder = 'dump'
start = False
while True:
    pressed_time = datetime.now()
    if keyboard.is_pressed("q"):
        start = False
    if keyboard.is_pressed("s"):
        start = True
    if keyboard.is_pressed("left arrow") and start:
        cur_folder = 'left'
        pressed_time = datetime.now()
    if keyboard.is_pressed("right arrow") and start:
        pressed_time = datetime.now()
        cur_folder = 'right'
    if keyboard.is_pressed("up arrow") and start:
        pressed_time = datetime.now()
        cur_folder = 'up'
    if keyboard.is_pressed("down arrow") and start:
        pressed_time = datetime.now()
        cur_folder = 'down'
    if (datetime.now()-pressed_time).total_seconds()>3 and start:
        cur_folder = 'none'
    if start == True:
        screenshots.take_screenshot(cur_folder)
    
