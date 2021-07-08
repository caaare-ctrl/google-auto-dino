# https://elgoog.im/t-rex/
# You goal today is to write a Python script to automate the playing of this game.
# Your program will look at the pixels on the screen to determine when it needs
# to hit the space bar and play the game automatically.
# You can see what it looks like when the game is automated with a bot:
# https://elgoog.im/t-rex/?bot

# You might want to look up these two packages:

# https://pypi.org/project/Pillow/
# https://pyautogui.readthedocs.io/en/latest/
# Size(width=1920, height=1080)
# The game window is on the left side, half of the size of the window
import pyautogui
# start the game
pyautogui.click(x=200, y=200)
pyautogui.press('up')
select_region = (183,489,160,100)
# region = left, top, width, and height
# pyautogui.screenshot(imageFilename="example.jpg",region=(5,250,1000,400))
pyautogui.screenshot(imageFilename="test.png",region=select_region)
while True:
    if pyautogui.locateOnScreen("img_6.png", confidence=0.3, region=select_region, grayscale=True):
        pyautogui.press('up')
