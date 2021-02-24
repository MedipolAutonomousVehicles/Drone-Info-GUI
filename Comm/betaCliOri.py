# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
# with open("dataFile.json","w") as writeFile:
#     json.dump(data,writeFile)

# with open("dataFile.json", "r") as read_file:
#     data = json.load(read_file)
#     print(data)

import json
import socket


class Client:

    def __init__(self):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connectServer(self, ip, port):
        try:
            self.connection.connect((ip, port))
            return True
        except Exception as e:
            print(e)
            return False

    def disconnect(self):
        self.connection.close()

    def jsonSend(self, data):
        try:
            self.connection.send(bytes(data,"utf-8"))
            return True
        except:
            return False


    def sendData(self,fileName):
        try:
            with open(fileName, "r") as readFile:
                data = json.load(readFile)
            dataInput = data
            #dataInput = dataInput.split(" ")
            if self.jsonSend(dataInput):
                return True
            else:
                return False
        except:
            self.connection.close()

# SERVERIP = "169.254.94.221"
# PORT = 13377
#
# socketObj = Client()
# socketObj.connectServer(SERVERIP,PORT)
# socketObj.sendData("ş Ş İI ÜĞÜĞÜĞ")
