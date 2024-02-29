import cv2
import numpy as np
import matplotlib.pyplot as plt
from screenshots import screenshots
from gymnasium import Env
from gymnasium.spaces import Box, Discrete
import time
import keyboard
import pyautogui as mouse
import pytesseract
from callback import TrainAndLoggingCallback
class WebGame(Env):

    def __init__(self) -> None:
        super().__init__()
        self.observation_space = Box(low=0,high=255,shape=(1,150,200),dtype=np.uint8)
        self.action_space = Discrete(5)
        self.capture_image = screenshots()
        self.game_location = (300,200,1200,660)
        self.play_again_location = (1360,200,120,54)

        
    def step(self, action):
        actions = {0:'up arrow',1:'down arrow',2:'left arrow',3:'right arrow',4:'nothing'}
        if action!=4:
            keyboard.press_and_release(actions[action])
        reward = 1
        info = {}
        done = self.get_done()
        new_observation = self.get_observation()
        return new_observation, reward, done, info
    

    def render(self):
        return super().render()
    

    def reset(self):
        time.sleep(2)
        mouse.leftClick()
        time.sleep(2)
        keyboard.press_and_release("space")

    def close(self):
        cv2.destroyAllWindows()
    
    
    def get_observation(self):
        raw = np.array(self.capture_image.take_screenshot(self.game_location))[:,:,:3]
        gray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (200,150))
        channel = np.reshape(resized, (1,150,200))
        return channel
    

    def get_done(self):
        done = False
        done_cap = np.array(self.capture_image.take_screenshot(self.play_again_location))[:,:,:3]
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        res = pytesseract.image_to_string(done_cap)[:4]
        if res=='':
            done = True
        return done, done_cap