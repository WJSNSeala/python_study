# -*- coding: utf-8 -*-

"""

filename: server
date: 2018-03-23
purpose: send json data

"""
import socket
import datetime

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 12222
    data = {}

    date_time = datetime.datetime.now()

    data["curtime"] = str(date_time)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))

    s.listen(5)
    c = None

    while True:
        if c is None:
            # Halts
            print('[Waiting for connection...]')
            c, addr = s.accept()  # (socket object, address info) return
            print('Got connection from', addr)
        else:
            # Halts
            print('[Waiting for response...]')
            c.send(str(data).encode('utf-8'))

    return


if __name__ == "__main__":
    main()
