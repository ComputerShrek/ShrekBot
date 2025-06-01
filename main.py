import random
import pyautogui
import string
import time
import os
import sys
import types
sys.modules['mouseinfo'] = types.ModuleType('mouseinfo')
# 

# !DISCLAIMER!
# This Script is for educational purposes only.
# Never bot on any website, your account will be banned.
# I am not responsible for any misuse of this script, as I do not condone or support any illegal activities.
#!DISCLAIMER!
time.sleep(2)
print("searching for comment button...")
commentbtn = pyautogui.locateCenterOnScreen("commentbtn.png")
if commentbtn is None:
    print("Comment button not found. Please ensure the image is correct and visible on the screen.")
    exit()
else:
    print("Comment button found at:", commentbtn)
    pyautogui.click(commentbtn)