from selenium import webdriver
import time
import pyautogui
import webbrowser
import os


# refreshrate=int(2)
# driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
# driver.get("localhost:8000")
# while True:
#     pyautogui.hotkey('f5')

os.system("start \"\" http://localhost:8000")
while True:
    time.sleep(2)
    pyautogui.hotkey('f5')