import socket
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')


def sendDir(s, data):

    while True:
        s.sendall(data)

