from PIL import Image, ImageChops
from pathlib import Path
import pyautogui
import keyboard
import time
from ppadb.client import Client as AdbClient
from Setting import Settings
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
client = AdbClient("127.0.0.1", 5037)
devices = client.devices()
device = devices[0]

class SmallFunctions:
    def DoingScreenshot(self):
        result = device.screencap()
        with open("screen.png", "wb") as fp:
            fp.write(result)

    def AllianceCollect(self):  # заходит в альянс, строения альянса
        time.sleep(2)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('Alliance.png', 'screen.png')
        print(Coordinates)
        if Coordinates is not None:
            device.input_tap(Coordinates[0], Coordinates[1])
        time.sleep(2)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('BuildOfAlliance.png', 'screen.png')
        print(Coordinates)
        if Coordinates is not None:
            device.input_tap(Coordinates[0], Coordinates[1])
        time.sleep(2)

    def GoCollect(self):  # нажимает кнопку сбора+кнопку в походе
        time.sleep(2)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('Collect.png', 'screen.png', grayscale=True, confidence=0.8)
        print(Coordinates)
        if Coordinates is not None:
            device.input_tap(Coordinates[0], Coordinates[1])
        time.sleep(2)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('GoAttack.png', 'screen.png', grayscale=True, confidence=0.8)
        print(Coordinates)
        if Coordinates is not None:
            device.input_tap(Coordinates[0], Coordinates[1])
        time.sleep(2)

    def SwipeFields(self):  # Скроллит по одной шахте
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('screen.png', 'screen.png')
        device.input_swipe(Coordinates[2] - Coordinates[2] // 3.81179, Coordinates[3] - Coordinates[3] // 2.05421,
                           Coordinates[2] - Coordinates[2] // 3.765, Coordinates[3] - Coordinates[3] // 1.45631, 1500)

    def isThisTheFreeMine(self):  # Проверяет пустая шахта или нет
        time.sleep(2)
        self.DoingScreenshot()
        cords = pyautogui.locate('screen.png', 'screen.png')
        im = Image.open('screen.png')
        im_crop1 = im.crop((0, cords[3] - cords[3] // 1.3, cords[2], cords[3] - cords[3] // 1.7))
        im_crop1.save('test0.png', guality=100)
        cords = pyautogui.locate('FreeMine.png', 'test0.png', grayscale=True, confidence=0.8)
        print(cords)
        if cords is not None:
            return True
        else:
            return False

    def AllFields(self):  # открывает список владений
        time.sleep(2)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('screen.png', 'screen.png')
        device.input_tap(Coordinates[2] - Coordinates[2] // 22, Coordinates[3] - Coordinates[3] // 14)
        time.sleep(5)
        device.input_tap(Coordinates[2] - Coordinates[2] // 22, Coordinates[3] - Coordinates[3] // 14)
        time.sleep(5)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('screen.png', 'screen.png')
        device.input_tap(Coordinates[2] // 2, Coordinates[3] // 2)
        time.sleep(2)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('AllFieldsHere.png', 'screen.png', grayscale=True, confidence=0.8)
        print(Coordinates)
        if Coordinates is not None:
            device.input_tap(Coordinates[0], Coordinates[1])
        time.sleep(2)

    def HowMuchIcanCollect(self):
        time.sleep(2)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('Hero.png', 'screen.png')
        if Coordinates is not None:
            device.input_tap(Coordinates[0], Coordinates[1])
        time.sleep(2)
        self.DoingScreenshot()
        cords = pyautogui.locate('screen.png', 'screen.png')
        im = Image.open('screen.png')
        im_crop1 = im.crop((cords[2]-cords[2] // 3.83, cords[3] - cords[3] // 4.3, cords[2] - cords[2] // 5, cords[3] - cords[3] // 5.43))
        im_crop1.save('test0.png', guality=100)
        image = cv2.imread("test0.png")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        config = r'--oem 3 --psm 6'
        string = pytesseract.image_to_string(image, 'rus', config=config)
        alfavite = '0123456789'
        Nagryzka = ''
        for i in range(len(string)):
            if string[i] in alfavite:
                Nagryzka += string[i]
        print(Nagryzka)
        Nagryzka = int(Nagryzka)
        time.sleep(2)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('Back.png', 'screen.png')
        if Coordinates is not None:
            device.input_tap(Coordinates[0], Coordinates[1])
        time.sleep(2)
        self.DoingScreenshot()
        Coordinates = pyautogui.locate('Out.png', 'screen.png')
        if Coordinates is not None:
            device.input_tap(Coordinates[0], Coordinates[1])
        return Nagryzka

    def SkolkoMozhnoSobrat(self):
        time.sleep(4)
        self.DoingScreenshot()
        cords = pyautogui.locate('screen.png', 'screen.png')
        im = Image.open('screen.png')
        im_crop1 = im.crop((cords[2]-cords[2] // 2.2, cords[3] - cords[3] // 1.55, cords[2] - cords[2] // 2.96, cords[3] - cords[3] // 1.65))
        im_crop1.save('test0.png', guality=100)
        image = cv2.imread("test0.png")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        config = r'--oem 3 --psm 6'
        string = pytesseract.image_to_string(image, 'rus', config=config)
        ICanCollect = ''
        for i in range(len(string)):
            if string[i]!='/':
                ICanCollect += string[i]
            else:
                break
        print(ICanCollect)
        ICanCollect = int(ICanCollect)
        time.sleep(2)
        return ICanCollect