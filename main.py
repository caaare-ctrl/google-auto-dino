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
import pyautogui
# pyautogui.screenshot("example.jpg")
# start the game
pyautogui.click(x=100, y=200)
pyautogui.press('up')
images = ["img.png","img_1.png","img_2.png","img_3.png","img_4.png","img_5.png"]
# region = left, top, width, and height
pyautogui.screenshot(imageFilename="example.jpg",region=(5,250,1000,400))
pyautogui.screenshot(imageFilename="test.png",region=(176,478,170,100))
while True:
    if pyautogui.locateOnScreen("img_6.png", confidence=0.4, region=(179,478,160,100), grayscale=True):
        pyautogui.press('up')

