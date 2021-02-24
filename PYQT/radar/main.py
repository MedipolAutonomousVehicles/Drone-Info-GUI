from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from mainUi import Ui_Form
import sys
import random

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.clickButton = self.ui.pushButton
        self.clickButton.clicked.connect(self.func)


    def func(self):
        x = random.randint(20,371)
        y = random.randint(20,381)
        enemyNumber = input("Enter enemy number: ")
        self.ui.changeEnemyPos(int(enemyNumber),x,y)
        #self.enemy.setGeometry(QtCore.QRect(x, y, 16, 16))


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec_()
