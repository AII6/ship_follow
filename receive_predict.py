import socket
import threading
import tkinter.scrolledtext
from tkinter import *
import cv2
import numpy as np
from predict import predict

socket_list = []
s = socket.socket()
s.bind(('192.168.1.100', 30000))
s.listen()

conn, addr = s.accept()
print(str(addr) + ' Joined!')
while True:

    content = conn.recv(921600)
    while len(content) < 921600:
        a = conn.recv(921600-len(content))
        content += a
    if content is None:
        break
    else:
        image = np.frombuffer(content, dtype='uint8')
        result = image.reshape(480, 640, 3)

        predict(result)

