from PIL import Image, ImageChops
from pathlib import Path
import pyautogui
import keyboard
import time
import cv2
from ppadb.client import Client as AdbClient
from Setting import Settings
from BigFunctions import BigFunctions
from SmallFunctions import SmallFunctions
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
settings = Settings()
Bigfunctions = BigFunctions
Smallfunctions = SmallFunctions()

client = AdbClient("127.0.0.1", 5037)#в ноксе было 5037
devices = client.devices()
device = devices[0]

while True:
    Bigfunctions.KillingMonsters(None)
    #Bigfunctions.CollectingRss(None)
    #print('End')
    #break

#Bigfunctions.CollectingRss(None)



