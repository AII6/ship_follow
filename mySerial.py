import sys

import numpy as np

from sendDir import sendDir


def quit(signum, frame):
    data = np.array([9, 9, 9], dtype='uint8')
    for i in range(5):
        sendDir(data)
    print("exit!!!")
    sys.exit(0)     # 手动终止程序