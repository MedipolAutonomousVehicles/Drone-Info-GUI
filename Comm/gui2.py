from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from PIL import ImageTk, Image
from ipAddress import getPublicIp
#from mySocket import MySocket
#from socketListener import SocketListener


class Gui:

    def __init__(self):
        self.root = Tk()
        self.img1 = ImageTk.PhotoImage(Image.open(r"D:\MAV\Connect.png"))
        self.WIDHT = 1600
        self.HEIGHT = 900
        self.root.geometry(f"{self.WIDHT}x{self.HEIGHT}")
        self.root.title("Gui")
        self.canvas = Canvas(self.root, bg="midnight blue", width=self.WIDHT, height=self.HEIGHT)
        self.canvas.pack(fill=BOTH, expand=True)
        self.layout()
        self.root.mainloop()

    def layout(self):
        topFrame = ttk.Frame(self.canvas, padding=10)
        topFrame.pack(side="top", expand=True, anchor=NE)
        self.hostLabel = Label(topFrame, text="Host: ", width=15, height=2)
        self.hostLabel.pack(side="left", expand=True)
        self.hostLabel.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)

        self.hostIp = Label(topFrame, text=f"{getPublicIp()}", width=15, height=2)
        self.hostIp.pack(side="right", expand=True)
        self.hostIp.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)

        midFrame = ttk.Frame(self.canvas, padding=10)
        midFrame.pack(side="top", expand=True, anchor=NE)
        self.serverLabel = Label(midFrame, text="Server IP:", width=15, height=2)
        self.serverLabel.pack(side="left", expand=True)
        self.serverLabel.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)

        self.serverIp = Text(midFrame, width=15, height=1)
        self.serverIp.pack(side="right", expand=True)
        self.serverIp.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)

        conFrame = ttk.Frame(self.canvas, padding=10)
        conFrame.pack(side="top", expand=True, anchor=NE)
        self.connect = Button(conFrame, image=self.img1, command=self.conButton)
        self.connect.pack(side="top", expand=True)

        dataFrame = ttk.Frame(self.canvas, padding=10)
        dataFrame.pack(side="bottom", expand=True)

        self.data = scrolledtext.ScrolledText(dataFrame, wrap=WORD, width=195, height=49)
        self.data.grid(row=3, column=0, pady=10, padx=10, columnspan=4)
        self.data.focus()

    def conButton(self):
        serverIp = self.serverIp.get(0.0, END)[0:-1]
        self.connectServer()

    def connectServer(self):
        my_socket_object = SocketListener("192.168.1.5", 8080)
        my_socket_object.start_listener()


Gui()
