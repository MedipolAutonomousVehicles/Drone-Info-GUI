from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from mainUi import Ui_Form
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1024, 1024)

        self.originalImage = QtGui.QPixmap("needle.png").transformed(QtGui.QTransform().rotate(-90))
        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(self.originalImage)
        self.label.setGeometry(QtCore.QRect(200,200,self.originalImage.width(),self.originalImage.height()))

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(500, 100, 80, 20))
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(500,120,80,20))
        button.setText("Click me")
        button.clicked.connect(self.rotate)
        self.angle = 0

    def rotate(self):
        angle = self.angle
        #angle = self.lineEdit.text()#int(input("Enter angle: "))
        if self.angle == 360:
            self.angle = 0
        tranform = QtGui.QTransform().rotate(int(angle))
        print(self.angle)
        #self.image = self.originalImage.scaled(self.originalImage.width(),self.originalImage.height(),QtCore.Qt.KeepAspectRatio)
        self.image = self.originalImage.transformed(tranform)
        self.label.setPixmap(self.image)
        if self.angle < 90:
            self.label.setGeometry(300-self.image.width()+5, 300-self.image.height(), self.image.width(), self.image.height())
        else:
            self.label.setGeometry(300, 300-self.image.height(), self.image.width(), self.image.height())

        print(self.image.width(),self.image.height())
        self.angle += 5



app =QApplication(sys.argv)
window = UI()
window.show()
app.exec_()

# class UI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#
#
#         self.ui.pushButton.clicked.connect(self.func)
#
#     def func(self):
#         transform90 = QtGui.QTransform().rotate(90)
#         try:
#             print(1)
#             self.ui.pixmap = self.ui.pixmap.transformed(transform90)
#         except Exception as e:
#             print(e)
#
# app = QApplication(sys.argv)
# window = UI()
# window.show()
# app.exec_()
