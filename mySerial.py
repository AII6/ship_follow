import sys
from sendDir import sendDir


def quit(signum, frame):
    data = "999\r\n"
    for i in range(5):
        sendDir(data)
    print("exit!!!")
    sys.exit(0)     # 手动终止程序