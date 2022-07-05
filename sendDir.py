import socket
import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

s = socket.socket()
s.connect(('192.168.1.103', 40001))
# s.connect(('192.168.43.167', 40001))


def sendDir(data):
    global s
    s.sendall(data)

