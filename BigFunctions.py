from PIL import Image, ImageChops
from pathlib import Path
import pyautogui
import keyboard
import time
from ppadb.client import Client as AdbClient
from Setting import Settings
from SmallFunctions import SmallFunctions
import pytesseract
import cv2

settings = Settings()
Smallfunctions = SmallFunctions()

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
client = AdbClient("127.0.0.1", 5037)
devices = client.devices()
device = devices[0]

class BigFunctions:
    def KillingMonsters(self):
        while True:
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('Out.png', 'screen.png')
            print(Coordinates)
            if Coordinates is not None:
                device.input_tap(Coordinates[0], Coordinates[1])
            time.sleep(3)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('Meshaet.png', 'screen.png')
            print(Coordinates)
            if Coordinates is not None:
                device.input_tap(Coordinates[0], Coordinates[1])
            time.sleep(2)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('Search.png', 'screen.png')
            print(Coordinates)
            if Coordinates is not None:
                device.input_tap(Coordinates[0], Coordinates[1])
            time.sleep(2)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('SearchFree.png', 'screen.png', grayscale=True, confidence=0.6)
            print(Coordinates)
            if Coordinates is not None:
                device.input_tap(Coordinates[0], Coordinates[1])
            time.sleep(2)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('SearchGold.png', 'screen.png')
            print(Coordinates)
            if Coordinates is not None:
                device.input_tap(Coordinates[0], Coordinates[1])
            time.sleep(5)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('screen.png', 'screen.png')
            device.input_tap(Coordinates[2]//2, Coordinates[3]//2)
            time.sleep(5)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('screen.png', 'screen.png')
            device.input_tap(Coordinates[2]//1.45, Coordinates[3]//1.24)
            '''Coordinates = pyautogui.locate('AttackMonster.png', 'screen.png')
            print(Coordinates)
            if Coordinates is not None:
                device.input_tap(Coordinates[0], Coordinates[1])'''
            time.sleep(3)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('GoAttack.png', 'screen.png')
            print(Coordinates)
            if Coordinates is not None:
                device.input_tap(Coordinates[0], Coordinates[1])
            time.sleep(3)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('NeedMoreTonus.png', 'screen.png')
            print(Coordinates)
            if Coordinates is not None:
                print('End')
                break
            time.sleep(60)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('screen.png', 'screen.png')
            device.input_tap(Coordinates[2]//2, Coordinates[3]//2)
            time.sleep(2)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('screen.png', 'screen.png')
            device.input_tap(Coordinates[2]//2, Coordinates[3]//2)
            time.sleep(2)

    def CollectingRss(self):  # сбор ресов
        CountHeroes = int(settings.countHeroes)
        CountAllianceMines = int(settings.countAllianceMines)
        if CountAllianceMines >= 1:  # Если указана только одна шахта клановая, то будет собирать только с общей
            Smallfunctions.AllianceCollect()
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('screen.png', 'screen.png')
            device.input_tap(Coordinates[2] // 2 - Coordinates[2] // 10.5, Coordinates[3] // 2 - Coordinates[3] // 13.7)
            time.sleep(3)
            Smallfunctions.GoCollect()
        if CountAllianceMines >= 2:  # Если указано две шахты, то будет собирать с общей и кем-то поставленной
            Smallfunctions.AllianceCollect()
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('DopCollecting.png', 'screen.png')
            print(Coordinates)
            if Coordinates is not None:
                device.input_tap(Coordinates[0], Coordinates[1])
            time.sleep(2)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('screen.png', 'screen.png')
            device.input_tap(Coordinates[2] // 2 + Coordinates[2] // 3.72, Coordinates[3] // 2 - Coordinates[3] // 14.3)
            time.sleep(2)
            Smallfunctions.GoCollect()
        if CountAllianceMines >= 3:  # Если указано три шахты, будет со всех супершахт собирать
            Smallfunctions.AllianceCollect()
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('DopCollecting.png', 'screen.png')
            print(Coordinates)
            if Coordinates is not None:
                device.input_tap(Coordinates[0], Coordinates[1])
            time.sleep(2)
            Smallfunctions.DoingScreenshot()
            Coordinates = pyautogui.locate('screen.png', 'screen.png')
            device.input_tap(Coordinates[2] // 2 - Coordinates[2] // 10.16,
                             Coordinates[3] // 2 + Coordinates[3] // 3.86)
            Smallfunctions.GoCollect()
        HeroesOnFields = 0  # Кол-во героев на полях(не клановых шахтах)
        while HeroesOnFields < (CountHeroes - CountAllianceMines):
            Nagryzka = Smallfunctions.HowMuchIcanCollect()#кол-во нагрузки у одного героя
            Smallfunctions.AllFields()
            ICanCollect = Smallfunctions.SkolkoMozhnoSobrat()  # кол-во ресурсов в поле
            print(HeroesOnFields)
            print(CountHeroes - CountAllianceMines)
            while not Smallfunctions.isThisTheFreeMine() or Nagryzka>ICanCollect:
                Smallfunctions.SwipeFields()
                time.sleep(5)
                ICanCollect = Smallfunctions.SkolkoMozhnoSobrat()
            Smallfunctions.DoingScreenshot()
            cords = pyautogui.locate('screen.png', 'screen.png')
            device.input_tap(cords[2] - cords[2] // 3.82, cords[3] - cords[3] // 1.45)
            Smallfunctions.GoCollect()
            HeroesOnFields += 1
