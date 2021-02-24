import socket

import socket

UDP_IP = "169.254.64.241"
UDP_PORT = 13377
sock = socket.socket(socket.AF_INET,  # Internet
socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))
print("Listening")
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print("received message: %s" % data.decode())

