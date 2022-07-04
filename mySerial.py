import serial
import sys


# class mySerial(serial.Serial):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         ser = serial.Serial()
#         ser.port = "COM4"  # 设置端口号
#         ser.baudrate = 115200  # 设置波特率
#         ser.bytesize = 8  # 设置数据位
#         ser.stopbits = 1  # 设置停止位
#         ser.parity = "N"  # 设置校验位
#         ser.open()  # 打开串口,要找到对的串口号才会成功

ser = serial.Serial()
ser.port = "COM4"  # 设置端口号
ser.baudrate = 115200  # 设置波特率
ser.bytesize = 8  # 设置数据位
ser.stopbits = 1  # 设置停止位
ser.parity = "N"  # 设置校验位
# ser.open()  # 打开串口,要找到对的串口号才会成功


def quit(signum, frame):
    data = "999\r\n"
    for i in range(5):
        ser.write(data.encode('gbk'))
    print("exit!!!")
    sys.exit(0)     # 手动终止程序