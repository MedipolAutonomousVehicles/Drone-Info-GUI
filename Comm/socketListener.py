import socket
import base64
import simplejson


class Client:

    def __init__(self,ip,port):
        self.listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print(self.listener.bind((ip,port)))
        print(self.listener.listen(0))
        self.connection, connectionAddress = self.listener.accept()
        print("Connection ok from ",connectionAddress)

    def jsonSend(self,data):
        jsonData = simplejson.dumps(data)
        self.connection.send(jsonData.encode("utf-8"))

    def jsonReceive(self):
        jsonData = ""
        while True:
            try:
                jsonData = jsonData + self.connection.recv(1024).decode()
                return simplejson.loads(jsonData)
            except ValueError:
                continue

    def startListener(self):
        while True:
            dataInput = input("Enter: ")
            dataInput = dataInput.split(" ")
            print(dataInput)
            self.jsonSend(dataInput)


SERVERIP = "192.168.0.2"
PORT = 54321

socketListener = Client(SERVERIP,PORT)
socketListener.startListener()