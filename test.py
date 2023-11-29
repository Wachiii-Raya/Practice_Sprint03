import serial 
import time

print("hello world")

serialHandler = serial.Serial("COM7", 9600)

while True:
    
    # read from serial port
    data = serialHandler.read(3)
    print(data)