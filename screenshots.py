import time
import pyautogui
class screenshots:
    def __init__(self) -> None:
        pass
    def take_screenshot(self, game_location):
        cur_time = str(time.time())
        myScreenshot = pyautogui.screenshot(region=game_location)
        return myScreenshot