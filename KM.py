import cv2
import os
from mss import mss
import numpy as np
import win32api
import win32con  # Import win32con to detect key presses
import serial

os.system("color 2")
os.system("cls")
print("       _                   _                   _             _           ")
print("   .:'´::::`';           ,·/::::`;'         ,·´/:::::'`:,   ,:´/::::'`:,'      ")
print("  /:::::::::'¦      ,:´::/::::::/'‚       '/  /:::::::::'`·/::/::::::::/'\\     ")
print(" /·'´ '¯ `';:;| .:´:::;'´ ¯'`:;/  ‘       /,·'´ ¯¯'`·;:::/:;·´ ¯ '`·;/:::i   ")
print(";         '¦:/:::::'´       / ‘        /            '`;':/            \\:::';  ")
print("i         '|/:::·´      .·'´         ,'               `'               ';:::i°")
print("';         '·´   ,.-:'´:`;.         ,'                                  ;::i‘' ")
print(" ';         ;',    `;·;:::::'`,      ;'       ,^,         ,:^,          'i::;°")
print("  ';        ;';'\\      '`;:::::'`,   'i        ;:::\\       ;/   ',         'i:;' ")
print("   ';      ';:/  '\\       '`;:::::'; 'i       'i::/  \\     /      ;        ;/   ")
print("    ';     ;/     ',        '`;:::/  ;      'i:/     `*'´       'i       ;/ °  ")
print("     \\   '/        '`·,      _';/'‚  '`.    ,'                   '.     /      ")
print("      `'´              `'*'´¯          `*´                      `'*'´         ")
print("                                     KingMethod                                  ")
print("                                                                                     ")

fov = int(input("FOV: "))

sct = mss()

arduino = serial.Serial('COM6', 115200)

screenshot = sct.monitors[1]
screenshot['left'] = int((screenshot['width'] / 2) - (fov / 2))
screenshot['top'] = int((screenshot['height'] / 2) - (fov / 2))
screenshot['width'] = fov
screenshot['height'] = fov
center = fov / 2

embaixo = np.array([140, 111, 160])
emcima = np.array([148, 154, 194])

speed = float(input("SPEED: "))
os.system("cls")
print(" __        ______        ___       _______   _______  _______  ")
print("|  |      /  __  \\      /   \\     |       \\ |   ____||       \\ ")
print("|  |     |  |  |  |    /  ^  \\    |  .--.  ||  |__   |  .--.  |")
print("|  |     |  |  |  |   /  /_\\  \\   |  |  |  ||   __|  |  |  |  |")
print("|  `----.|  `--'  |  /  _____  \\  |  '--'  ||  |____ |  '--'  |")
print("|_______| \\______/  /__/     \\__\\ |_______/ |_______||_______/ ")
print("                                                               ")

def mousemove(x):
    if x < 0:
        x = x + 256

    pax = [int(x)]
    arduino.write(pax)

while True:
    # Check if either LMB (0x01) or the 'K' key (0x4B) is pressed
    if win32api.GetAsyncKeyState(0x01) < 0 or win32api.GetAsyncKeyState(ord('K')) < 0:
        img = np.array(sct.grab(screenshot))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, embaixo, emcima)
        kernel = np.ones((3, 3), np.uint8)
        dilated = cv2.dilate(mask, kernel, iterations=5)
        thresh = cv2.threshold(dilated, 60, 255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) != 0:
            mouse = cv2.moments(thresh)
            pixel = (int(mouse["m10"] / mouse["m00"]), int(mouse["m01"] / mouse["m00"]))

            aimzao = pixel[0] + 2

            diff_x = int(aimzao - center)

            alvo = diff_x * speed

            mousemove(alvo)
