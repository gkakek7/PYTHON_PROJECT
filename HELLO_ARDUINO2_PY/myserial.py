import serial
import time

my_serial = serial.Serial(port='COM4',baudrate=9600)

for i in range(10):
    time.sleep(1)
    my_serial.write("a\n".encode())
    time.sleep(1)
    my_serial.write("b\n".encode())
    time.sleep(1)
    my_serial.write("a\n".encode())
    time.sleep(1)
    my_serial.write("b\n".encode())