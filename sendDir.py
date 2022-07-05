import socket
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

s = socket.socket()
s.connect(('192.168.1.103', 40000))


def sendDir(data):
    global s
    while True:
        s.sendall(data)

