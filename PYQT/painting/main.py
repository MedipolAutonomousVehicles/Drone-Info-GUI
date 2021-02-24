from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from PyQt5.QtGui import QPen, QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
from sys import argv
class Ui(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Paint")
        self.setGeometry(2500,200,800,800)

        upButton = QPushButton(self)
        upButton.setText("Up")
        upButton.setGeometry(QtCore.QRect(0,0,50,25))
        upButton.clicked.connect(self.up)

        downButton = QPushButton(self)
        downButton.setText("Down")
        downButton.setGeometry(QtCore.QRect(50,0,50,25))
        downButton.clicked.connect(self.down)

        self.x = 0
        self.y = 0

    def up(self):
        self.x += 10
        self.y -= 10
        print(self.x)
        print(self.y)

    def down(self):
        self.x -= 10
        self.y += 10
        print(self.x)
        print(self.y)

    def paintEvent(self, event):
        backPosX = 200
        backPosY = 200
        pixmap = QPixmap("back.png")
        painter = QPainter(self)
        painter.drawPixmap(QtCore.QRect(backPosX,backPosY,pixmap.width(),pixmap.height()), pixmap)
        pen = QPen(Qt.red, 3)
        painter.setPen(pen)
        painter.drawLine(backPosX+pixmap.width()//2-5, backPosY+pixmap.height()//2, 210+self.x,backPosY+pixmap.height()//2+self.y)

app = QApplication(argv)
window = Ui()
window.show()
app.exec_()
