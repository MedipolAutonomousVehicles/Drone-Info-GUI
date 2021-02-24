from tkinter import *
from tkinter import ttk
from Comm.betaClient import Client
import json
from time import sleep
class Gui:
    def __init__(self):
        self.width = 600
        self.height = 400
        self.root = Tk()
        self.root.title("IS")
        self.canvas = Canvas(self.root, bg="white")  # , width=self.WIDHT, height=self.HEIGHT)
        self.canvas.pack(fill=BOTH, expand=True)
        style = ttk.Style()
        style.configure("new.TFrame", background="white")

        self.checkConnection = False
        self.connection = Client()

        self.layout()
        self.dataLayout()

        self.root.mainloop()

    def layout(self):

        firstFrame = ttk.Frame(self.canvas, style="new.TFrame")
        firstFrame.pack(side="top", expand=True)

        self.serverLabel = Label(firstFrame, text="Server IP:")
        self.serverLabel.pack(side="left", expand=True)
        self.serverLabel.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)

        self.serverIP = Entry(firstFrame, justify="left")
        self.serverIP.pack(side="left", expand=True)
        self.serverIP.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.serverIP.insert(0,"169.254.94.221")

        self.portLabel = Label(firstFrame, text="Port Number:")
        self.portLabel.pack(side="left", expand=True)
        self.portLabel.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)

        self.portNum = Entry(firstFrame, bg="white", bd=0, justify="left")
        self.portNum.pack(side="right", expand=True)
        self.portNum.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.portNum.insert(0,13377)

        secondFrame = ttk.Frame(self.canvas,style="new.TFrame")
        secondFrame.pack(side="top", expand=True, anchor=N)

        self.connectButton = ttk.Button(secondFrame, text="Connect",command=self.connectFunction)
        self.connectButton.pack(side="left", expand=True)

        self.disconnectButton = ttk.Button(secondFrame, text="Disconnect",command=self.disconnectFunction)
        self.disconnectButton.pack(side="right", expand=True)

        self.sendButton = ttk.Button(secondFrame, text="Send",command=self.sendDatas)
        self.sendButton.pack(side="right", expand=True)

    def connectFunction(self):
        IP = self.serverIP.get()
        PORT = self.portNum.get()
        if not self.checkConnection:
            if self.connection.connectServer(IP,int(PORT)):
                self.checkConnection = True
                print("Connected")
            else:
                self.refresh()
                print("Couldn't connect")
        else:
            print("Already Connected")

    def disconnectFunction(self):
        if self.checkConnection:
            self.refresh()
            self.checkConnection = False
            print("Disconnected")
        else:
            print("Not connected yet")

    def refresh(self):
        self.connection.disconnect()
        self.connection = Client()


    def queue(self):
        self.root.after(2000,self.sendDatas())

    def sendDatas(self):
        if self.checkConnection:

            with open("dataFile.json", "r") as readFile:
                self.datas = json.load(readFile)

            self.insertDatasToLabels()
            sentMessage = self.connection.sendData("dataFile.json") # sending data
            if not sentMessage:
                print("No Connection")
                self.refresh()
                self.checkConnection = False
            else:
                print("SENT")
        else:
            self.refresh()
            self.checkConnection = False
            print("No Connection")


    def insertDatasToLabels(self):
        self.teamNumberValue.delete(0,END)
        self.gpsHourValue.delete(0,END)
        self.gpsMinuteValue.delete(0,END)
        self.gpsSecondValue.delete(0,END)
        self.gpsSplitSecondValue.delete(0,END)
        self.serverHourValue.delete(0,END)
        self.serverMinuteValue.delete(0,END)
        self.serverSecondValue.delete(0,END)
        self.serverSplitSecondValue.delete(0,END)
        self.uavLatitudeValue.delete(0,END)
        self.uavLongitudeValue.delete(0,END)
        self.uavAltitudeValue.delete(0,END)
        self.uavVerticalValue.delete(0,END)
        self.uavOrientationValue.delete(0,END)
        self.uavBankValue.delete(0,END)
        self.velocityValue.delete(0,END)
        self.batteryValue.delete(0,END)

        self.uavModeValue.delete(0,END)
        self.lockingTargetValue.delete(0,END)
        self.lockFrameCenterXValue.delete(0,END)
        self.lockFrameCenterYValue.delete(0,END)
        self.lockFrameWidthValue.delete(0,END)
        self.lockFrameHeightValue.delete(0,END)
        self.hunterTeamNumberValue.delete(0,END)
        self.lockingNumberValue.delete(0,END)
        self.gpuHourLockStartValue.delete(0,END)
        self.gpuMinuteLockStartValue.delete(0,END)
        self.gpuSecondLockStartValue.delete(0,END)
        self.gpuSplitSecondLockStartValue.delete(0,END)
        self.gpuHourLockStopValue.delete(0,END)
        self.gpuMinuteLockStopValue.delete(0,END)
        self.gpuSecondLockStopValue.delete(0,END)
        self.gpuSplitSecondLockStopValue.delete(0,END)


        self.teamNumberValue.insert(0,self.datas["Takım Numarası"])
        self.gpsHourValue.insert(0,self.datas["GPS Saat"])
        self.gpsMinuteValue.insert(0,self.datas["GPS Dakika"])
        self.gpsSecondValue.insert(0,self.datas["GPS Saniye"])
        self.gpsSplitSecondValue.insert(0,self.datas["GPS Salise"])
        self.serverHourValue.insert(0,self.datas["Server Saat"])
        self.serverMinuteValue.insert(0,self.datas["Server Dakika"])
        self.serverSecondValue.insert(0,self.datas["Server Saniye"])
        self.serverSplitSecondValue.insert(0,self.datas["Server Salise"])
        self.uavLatitudeValue.insert(0,self.datas["İHA Enlem"])
        self.uavLongitudeValue.insert(0,self.datas["İHA Boylam"])
        self.uavAltitudeValue.insert(0,self.datas["İHA İrtifa"])
        self.uavVerticalValue.insert(0,self.datas["Dikilme"])
        self.uavOrientationValue.insert(0,self.datas["Yönelme"])
        self.uavBankValue.insert(0,self.datas["Yatış"])
        self.velocityValue.insert(0,self.datas["Hız"])
        self.batteryValue.insert(0,self.datas["Pil"])

        self.uavModeValue.insert(0,self.datas["İHA Modu"])
        self.lockingTargetValue.insert(0,self.datas["Kilitlenme Durumu"])
        self.lockFrameCenterXValue.insert(0,self.datas["Kilit Çerçevesi Merkezi X"])
        self.lockFrameCenterYValue.insert(0,self.datas["Kilit Çerçevesi Merkezi Y"])
        self.lockFrameWidthValue.insert(0,self.datas["Kilit Çerçevesi Genişliği"])
        self.lockFrameHeightValue.insert(0,self.datas["Kilit Çerçevesi Yüksekliği"])
        self.hunterTeamNumberValue.insert(0,self.datas["Avcı Takım Numarası"])
        self.lockingNumberValue.insert(0,self.datas["Kilitlenme Numarası"])
        self.gpuHourLockStartValue.insert(0,self.datas["GPS Saat Kilitlenme Başlangıç"])
        self.gpuMinuteLockStartValue.insert(0,self.datas["GPS Dakika Kilitlenme Başlangıç"])
        self.gpuSecondLockStartValue.insert(0,self.datas["GPS Saniye Kilitlenme Başlangıç"])
        self.gpuSplitSecondLockStartValue.insert(0,self.datas["GPS Salise Kilitlenme Başlangıç"])
        self.gpuHourLockStopValue.insert(0,self.datas["GPS Saat Kilitlenme Bitiş"])
        self.gpuMinuteLockStopValue.insert(0,self.datas["GPS Dakika Kilitlenme Bitiş"])
        self.gpuSecondLockStopValue.insert(0,self.datas["GPS Saniye Kilitlenme Bitiş"])
        self.gpuSplitSecondLockStopValue.insert(0,self.datas["GPS Salise Kilitlenme Bitiş"])


    def dataLayout(self):
        self.datas = {"Takım Numarası":"","GPS Saat":"","GPS Dakika":"","GPS Saniye":"","GPS Salise":"",
                      "Server Saat":"","Server Dakika":"","Server Saniye":"","Server Salise":"","İHA Enlem":"",
                      "İHA Boylam":"","İHA İrtifa":"","Dikilme":"","Yönelme":"","Yatış":"","Hız":"","Pil":"",
                      "İHA Modu":"","Kilitlenme Durumu":"","Kilit Çerçevesi Merkezi X":"","Kilit Çerçevesi Merkezi Y":"",
                      "Kilit Çerçevesi Genişliği":"","Kilit Çerçevesi Yüksekliği":"","Avcı Takım Numarası":"",
                      "Kilitlenme Numarası":"","GPS Saat Kilitlenme Başlangıç":"","GPS Dakika Kilitlenme Başlangıç":"",
                      "GPS Saniye Kilitlenme Başlangıç":"","GPS Salise Kilitlenme Başlangıç":"",
                      "GPS Saat Kilitlenme Bitiş":"","GPS Dakika Kilitlenme Bitiş":"","GPS Saniye Kilitlenme Bitiş":"",
                      "GPS Salise Kilitlenme Bitiş":""}
        #Third Frame
        thirdFrame = ttk.Frame(self.canvas,style="new.TFrame")
        thirdFrame.pack(side="left", expand=True)
        third2Frame = ttk.Frame(self.canvas,style="new.TFrame")
        third2Frame.pack(side="left", expand=True)

        teamNumber = Label(thirdFrame, text="Takım Numarası:")
        gpsHour = Label(thirdFrame, text="GPS Saat:")
        gpsMinute = Label(thirdFrame, text="GPS Dakika:")
        gpsSecond = Label(thirdFrame, text="GPS Saniye:")
        gpsSplitSecond = Label(thirdFrame, text="GPS Salise:")
        serverHour = Label(thirdFrame, text="Server Saat:")
        serverMinute = Label(thirdFrame, text="Server Dakika:")
        serverSecond = Label(thirdFrame,text= "Server Saniye:")
        serverSplitSecond = Label(thirdFrame,text="Server Salise:")
        uavLatitude = Label(thirdFrame,text="İHA Enlem:")
        uavLongitude = Label(thirdFrame,text="İHA Boylam:")
        uavAltitude = Label(thirdFrame,text="İHA İrtifa:")
        uavVertical = Label(thirdFrame,text="Dikilme:")
        uavOrientation = Label(thirdFrame,text="Yönelme:")
        uavBank = Label(thirdFrame,text="Yatış:")
        velocity = Label(thirdFrame,text="Hız:")
        battery = Label(thirdFrame,text="Pil:")
        self.teamNumberValue = Entry(third2Frame)
        self.gpsHourValue = Entry(third2Frame)
        self.gpsMinuteValue = Entry(third2Frame)
        self.gpsSecondValue = Entry(third2Frame)
        self.gpsSplitSecondValue = Entry(third2Frame)
        self.serverHourValue = Entry(third2Frame)
        self.serverMinuteValue = Entry(third2Frame)
        self.serverSecondValue = Entry(third2Frame)
        self.serverSplitSecondValue = Entry(third2Frame)
        self.uavLatitudeValue = Entry(third2Frame)
        self.uavLongitudeValue = Entry(third2Frame)
        self.uavAltitudeValue = Entry(third2Frame)
        self.uavVerticalValue = Entry(third2Frame)
        self.uavOrientationValue = Entry(third2Frame)
        self.uavBankValue = Entry(third2Frame)
        self.velocityValue = Entry(third2Frame)
        self.batteryValue = Entry(third2Frame)


        teamNumber.pack(side="top",anchor="w")
        gpsHour.pack(side="top",anchor="w")
        gpsMinute.pack(side="top",anchor="w")
        gpsSecond.pack(side="top",anchor="w")
        gpsSplitSecond.pack(side="top",anchor="w")
        serverHour.pack(side="top",anchor="w")
        serverMinute.pack(side="top",anchor="w")
        serverSecond.pack(side="top",anchor="w")
        serverSplitSecond.pack(side="top",anchor="w")
        uavLatitude.pack(side="top",anchor="w")
        uavLongitude.pack(side="top", expand=True,anchor="w")
        uavAltitude.pack(side="top", expand=True,anchor="w")
        uavVertical.pack(side="top", expand=True,anchor="w")
        uavOrientation.pack(side="top", expand=True,anchor="w")
        uavBank.pack(side="top", expand=True,anchor="w")
        velocity.pack(side="top", expand=True,anchor="w")
        battery.pack(side="top", expand=True,anchor="w")
        self.teamNumberValue.pack(side="top",anchor="e")
        self.gpsHourValue.pack(side="top", expand=True,anchor="e")
        self.gpsMinuteValue.pack(side="top", expand=True,anchor="e")
        self.gpsSecondValue.pack(side="top", expand=True,anchor="e")
        self.gpsSplitSecondValue.pack(side="top", expand=True,anchor="e")
        self.serverHourValue.pack(side="top", expand=True,anchor="e")
        self.serverMinuteValue.pack(side="top", expand=True,anchor="e")
        self.serverSecondValue.pack(side="top", expand=True,anchor="e")
        self.serverSplitSecondValue.pack(side="top", expand=True,anchor="e")
        self.uavLatitudeValue.pack(side="top", expand=True,anchor="e")
        self.uavLongitudeValue.pack(side="top", expand=True,anchor="e")
        self.uavAltitudeValue.pack(side="top", expand=True,anchor="e")
        self.uavVerticalValue.pack(side="top", expand=True,anchor="e")
        self.uavOrientationValue.pack(side="top", expand=True,anchor="e")
        self.uavBankValue.pack(side="top", expand=True,anchor="e")
        self.velocityValue.pack(side="top", expand=True,anchor="e")
        self.batteryValue.pack(side="top", expand=True,anchor="e")


        teamNumber.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpsHour.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpsMinute.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpsSecond.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpsSplitSecond.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        serverHour.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        serverMinute.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        serverSecond.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        serverSplitSecond.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        uavLatitude.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        uavLongitude.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        uavAltitude.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        uavVertical.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        uavOrientation.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        uavBank.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        velocity.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        battery.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.teamNumberValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpsHourValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpsMinuteValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpsSecondValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpsSplitSecondValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.serverHourValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.serverMinuteValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.serverSecondValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.serverSplitSecondValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.uavLatitudeValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.uavLongitudeValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.uavAltitudeValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.uavVerticalValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.uavOrientationValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.uavBankValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.velocityValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.batteryValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)



        #Fourth Frame
        fourthFrame = ttk.Frame(self.canvas,style="new.TFrame")
        fourthFrame.pack(side="left", expand=True)
        fourth2Frame = ttk.Frame(self.canvas,style="new.TFrame")
        fourth2Frame.pack(side="right",expand=True)

        uavMode = Label(fourthFrame, text="İHA mod")
        lockingTarget = Label(fourthFrame, text="Kilitlenme Durumu")
        lockFrameCenterX = Label(fourthFrame, text="Kilit Çerçevesi Merkezi X")
        lockFrameCenterY = Label(fourthFrame, text="Kilit Çerçevesi Merkezi Y")
        lockFrameWidth = Label(fourthFrame, text="Kilit Çerçevesi Genişliği")
        lockFrameHeight = Label(fourthFrame, text="Kilit Çerçevesi Yüksekliği")
        hunterTeamNumber = Label(fourthFrame, text="Avcı Takım Numarası")
        lockingNumber = Label(fourthFrame, text="Kilitlenme Numarası")
        gpuHourLockStart = Label(fourthFrame, text="GPS Saat Kilitlenme Başlangıç")
        gpuMinuteLockStart = Label(fourthFrame, text="GPS Dakika Kilitlenme Başlangıç")
        gpuSecondLockStart = Label(fourthFrame, text="GPS Saniye Kilitlenme Başlangıç")
        gpuSplitSecondLockStart = Label(fourthFrame, text="GPS Salise Kilitlenme Başlangıç")
        gpuHourLockStop = Label(fourthFrame, text="GPS Saat Kilitlenme Bitiş")
        gpuMinuteLockStop = Label(fourthFrame, text="GPS Dakika Kilitlenme Bitiş")
        gpuSecondLockStop = Label(fourthFrame, text="GPS Saniye Kilitlenme Bitiş")
        gpuSplitSecondLockStop = Label(fourthFrame, text="GPS Salise Kilitlenme Bitiş")
        self.uavModeValue = Entry(fourth2Frame)
        self.lockingTargetValue = Entry(fourth2Frame)
        self.lockFrameCenterXValue = Entry(fourth2Frame)
        self.lockFrameCenterYValue = Entry(fourth2Frame)
        self.lockFrameWidthValue = Entry(fourth2Frame)
        self.lockFrameHeightValue = Entry(fourth2Frame)
        self.hunterTeamNumberValue = Entry(fourth2Frame)
        self.lockingNumberValue = Entry(fourth2Frame)
        self.gpuHourLockStartValue = Entry(fourth2Frame)
        self.gpuMinuteLockStartValue = Entry(fourth2Frame)
        self.gpuSecondLockStartValue = Entry(fourth2Frame)
        self.gpuSplitSecondLockStartValue = Entry(fourth2Frame)
        self.gpuHourLockStopValue = Entry(fourth2Frame)
        self.gpuMinuteLockStopValue = Entry(fourth2Frame)
        self.gpuSecondLockStopValue = Entry(fourth2Frame)
        self.gpuSplitSecondLockStopValue = Entry(fourth2Frame)

        uavMode.pack(side="top", expand=True,anchor="w")
        lockingTarget.pack(side="top", expand=True,anchor="w")
        lockFrameCenterX.pack(side="top", expand=True,anchor="w")
        lockFrameCenterY.pack(side="top", expand=True,anchor="w")
        lockFrameWidth.pack(side="top", expand=True,anchor="w")
        lockFrameHeight.pack(side="top", expand=True,anchor="w")
        hunterTeamNumber.pack(side="top", expand=True,anchor="w")
        lockingNumber.pack(side="top", expand=True,anchor="w")
        gpuHourLockStart.pack(side="top", expand=True,anchor="w")
        gpuMinuteLockStart.pack(side="top", expand=True,anchor="w")
        gpuSecondLockStart.pack(side="top", expand=True,anchor="w")
        gpuSplitSecondLockStart.pack(side="top", expand=True,anchor="w")
        gpuHourLockStop.pack(side="top", expand=True,anchor="w")
        gpuMinuteLockStop.pack(side="top", expand=True,anchor="w")
        gpuSecondLockStop.pack(side="top", expand=True,anchor="w")
        gpuSplitSecondLockStop.pack(side="top", expand=True,anchor="w")
        self.uavModeValue.pack(side="top", expand=True,anchor="e")
        self.lockingTargetValue.pack(side="top", expand=True,anchor="e")
        self.lockFrameCenterXValue.pack(side="top", expand=True,anchor="e")
        self.lockFrameCenterYValue.pack(side="top", expand=True,anchor="e")
        self.lockFrameWidthValue.pack(side="top", expand=True,anchor="e")
        self.lockFrameHeightValue.pack(side="top", expand=True,anchor="e")
        self.hunterTeamNumberValue.pack(side="top", expand=True,anchor="e")
        self.lockingNumberValue.pack(side="top", expand=True,anchor="e")
        self.gpuHourLockStartValue.pack(side="top", expand=True,anchor="e")
        self.gpuMinuteLockStartValue.pack(side="top", expand=True,anchor="e")
        self.gpuSecondLockStartValue.pack(side="top", expand=True,anchor="e")
        self.gpuSplitSecondLockStartValue.pack(side="top", expand=True,anchor="e")
        self.gpuHourLockStopValue.pack(side="top", expand=True,anchor="e")
        self.gpuMinuteLockStopValue.pack(side="top", expand=True,anchor="e")
        self.gpuSecondLockStopValue.pack(side="top", expand=True,anchor="e")
        self.gpuSplitSecondLockStopValue.pack(side="top", expand=True,anchor="e")

        uavMode.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        lockingTarget.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        lockFrameCenterX.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        lockFrameCenterY.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        lockFrameWidth.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        lockFrameHeight.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        hunterTeamNumber.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        lockingNumber.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpuHourLockStart.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpuMinuteLockStart.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpuSecondLockStart.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpuSplitSecondLockStart.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpuHourLockStop.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpuMinuteLockStop.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpuSecondLockStop.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        gpuSplitSecondLockStop.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.uavModeValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.lockingTargetValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.lockFrameCenterXValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.lockFrameCenterYValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.lockFrameWidthValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.lockFrameHeightValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.hunterTeamNumberValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.lockingNumberValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpuHourLockStartValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpuMinuteLockStartValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpuSecondLockStartValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpuSplitSecondLockStartValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpuHourLockStopValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpuMinuteLockStopValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpuSecondLockStopValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)
        self.gpuSplitSecondLockStopValue.config(font=("Segoe", 15, "bold"), fg="black", bg="white", bd=0)

g = Gui()
