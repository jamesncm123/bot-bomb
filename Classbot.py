from PIL import ImageGrab
import os
import time
from numpy import *
import win32api,win32con

class Mybot():
    def __init__(self):
        self.grab = ImageGrab
        self.minipath = os.path.dirname(__file__)
        self.pathphoto = os.path.join(self.minipath, 'photo')
        self.box = ()

    def Grab_img(self):
        self.box = (450, 378, 1086, 850)
        img = self.grab.grab(self.box)
        img.save(f"{self.pathphoto}/xxx.jpg")


bot = Mybot()
bot.Grab_img()
