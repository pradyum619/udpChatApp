#!/usr/bin/env python
# coding: utf-8

import socket

send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recvIp = "192.168.0.105"
recvPort = 1234
toSendIp = "192.168.0.106"
toSendPort = 1234

recv.bind((recvIp, recvPort))

while True:
    send.sendto((input("Enter msg: ").encode()), (toSendIp, toSendPort))
    x = recv.recvfrom(1024)
    clientip = x[1][0]
    msg = x[0].decode()
    print(clientip + " :" + msg)

