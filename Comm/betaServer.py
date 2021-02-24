import socket
import simplejson
import os
import base64
import sys


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.acceptComing()

    def acceptComing(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print(f"Listening {self.ip}:{self.port}")
        self.listener.bind((self.ip, self.port))
        self.listener.listen(0)
        self.connection, connectionAddress = self.listener.accept()
        print("Connection ok from: ", connectionAddress)

    def jsonReceive(self):
        jsonData = ""
        while True:
            try:
                msg = print(self.connection.recv(1024).decode())
            except ValueError:
                break
            jsonData = jsonData + msg
            if jsonData != "" or jsonData != None:
                return simplejson.loads(jsonData)
            else:
                return False


    def startSocket(self):
        while True:
            try:
                dataInput = self.jsonReceive()
                if not dataInput:
                    self.connection.close()
                    print("Disconnected")
                    self.acceptComing()
                else:

                    print(dataInput)
            except KeyboardInterrupt:
                sys.exit()



SERVERIP = "169.254.94.221"
PORT = 13377

socketObj = Server(SERVERIP, PORT)
socketObj.startSocket()




