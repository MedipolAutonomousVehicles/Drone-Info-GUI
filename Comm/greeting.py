from tkinter import *
from ipAddress import getPublicIp
import pyautogui
from PIL import ImageTk,Image
from functools import partial # to send arguments to function
from mySocket import MySocket




class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="Hello")
        label.pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        topFrame = Frame(self)
        topFrame.pack(side="top",expand=True)
        guestLabel = Label(topFrame, text=f"Guest IP:")
        guestLabel.pack(side="left", expand=True)
        self.guest = Label(topFrame,text=f"{getPublicIp()}")
        self.guest.pack(side="right",expand=True)

        midFrame = Frame(self)
        midFrame.pack(side="top",expand=True)
        serverLabel = Label(midFrame, text="Server IP:")
        serverLabel.pack(side="left", fill="both", expand=True)
        self.server = Text(midFrame,height=1, width=15)
        self.server.pack(side="right",expand=True)

        bottomFrame = Frame(self)
        bottomFrame.pack(side="bottom",expand=True)
        self.connect = Button(bottomFrame,text="Connect",command=self.getServerIp)
        self.connect.pack(side="bottom")

    def getServerIp(self):
        serverIp = self.server.get(0.0,END)[0:-1]
        print(type(serverIp))
        self.connectServer(serverIp)

    def connectServer(self,serverIp):
        mySocketObject = MySocket(serverIp, 8080)
        mySocketObject.start_socket()

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class MainView(Frame):
    def __init__(self, *args,**kwargs):
        Frame.__init__(self,*args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        nextButtonframe = Frame(self)
        backButtonframe = Frame(self)
        container = Frame(self)

        nextButtonframe.pack(side="right", fill="y", expand=False)
        backButtonframe.pack(side="left", fill="y", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(nextButtonframe, text="Next", command=p2.lift,width=5,height=100,bg="white",fg="black")
        b1.pack(side="right")

        b2 = Button(backButtonframe, text="Back", command=p1.lift,width=5,height=100,bg="white",fg="black")
        b2.pack(side="left")

        # b3 = Button(buttonframe, text="Page 3", command=p3.lift)
        # b3.pack(side="left")

        p2.show()


if __name__ == "__main__":
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    #root.wm_geometry("1600x900")
    root.geometry(f"{int(w/2)}x{int(h/2)}")

    root.mainloop()
