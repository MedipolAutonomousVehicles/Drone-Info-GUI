import requests
from time import sleep

def getPublicIp():
    try:
        req = requests.get("https://www.ifconfig.me")
    except:
        sess = requests.Session()
        sleep(0.4)
        req = sess.get("https://www.ifconfig.me")
    ip = req.text
    return ip

def getLocalIp():
    import socket
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip
