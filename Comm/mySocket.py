import socket
import simplejson
import os
import base64
import sys


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.connectHost()

    def connectHost(self):
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.ip, self.port))
        except Exception as e:
            print(e)
            pass
    def jsonSend(self, data):
        jsonData = simplejson.dumps(data)
        resp = self.connection.send(jsonData.encode("utf-8"))
        if resp:
            print("200")

    def startSocket(self):
        while True:
            try:
                dataInput = input("Enter: ")
                if dataInput == "disconnect":
                    self.connection.close()
                    print("Disconnected")
                elif dataInput == "connect":
                    self.connectHost()
                else:
                    self.jsonSend(dataInput)
            except:
                self.connection.close()
                print("Connection Lost")


SERVERIP = "169.254.94.221"
PORT = 1337

socketObj = Client(SERVERIP, PORT)
socketObj.startSocket()
