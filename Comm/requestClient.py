import requests
import simplejson

class ReqClient:
    def __init__(self, ip):
        self.IP = ip
        self.session = requests.Session()
        #self.session.get(ip)

    def jsonSend(self,data):
        jsonData = simplejson.dumps(data)
        resp = requests.post(self.IP,json=jsonData.encode("utf-8"))
        return resp
    # self.connection.send(jsonData.encode("utf-8"))

    def main(self):
        while True:
            dataInput = input("Enter: ")
            dataInput = dataInput.split(" ")
            resp = self.jsonSend(dataInput)
            print(resp)


client = ReqClient("http://192.168.0.12:8080")
client.main()
