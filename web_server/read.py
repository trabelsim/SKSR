import serial

ser = serial.Serial('COM7',115200,timeout=1)

while True:
    data = ser.readline()
    # if "Humidity".encode() in ser.read(45):
    #     print(ser.read(45))
    # print(type(data))
    list_data = data.decode()
    if "Temperature" in list_data:
        if "'" in list_data:
            temperatura = list_data[14:19]
            print("temp",temperatura)

    if "Humidity" in list_data:
        if "'" in list_data:
            humidity = list_data[12:14]
            print("hum",humidity)

    if "Pressure" in list_data:
        if "'" in list_data:
            pressure = list_data[11:19]
            print("press",pressure)