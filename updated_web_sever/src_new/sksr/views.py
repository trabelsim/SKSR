from django.http import HttpResponse
from django.shortcuts import render
import serial
from selenium import webdriver
import time

def home_page(request):
        hum_pomiar = take_hum()
        temp_pomiar = take_temp()
        press_pomiar = take_press()

        return render(request,"index.html",{"title":temp_pomiar,"title2":hum_pomiar,"title3":press_pomiar})


#
# def refresh_browser():
#     refresh = 1
#     driver = webdriver.Chrome(r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
#     driver.get("http://localhost:8000")
#     while True:
#         time.sleep(refresh)
#         driver.refresh()



def take_temp():
    ser = serial.Serial('COM7',115200,timeout=1)
    while True:
        data = ser.readline()
        list_data = data.decode()
        if "Temperature" in list_data:
            if "'" in list_data:
                temperatura = list_data[14:19]
                return temperatura

def take_hum():
    ser = serial.Serial('COM7', 115200, timeout=1)
    while True:
        data = ser.readline()
        list_data = data.decode()
        if "Humidity" in list_data:
            if "'" in list_data:
                humidity = list_data[12:14]
                return humidity

def take_press():
    ser = serial.Serial('COM7', 115200, timeout=1)
    while True:
        data = ser.readline()
        list_data = data.decode()
        if "Pressure" in list_data:
            if "'" in list_data:
                pressure = list_data[11:19]
                return pressure




