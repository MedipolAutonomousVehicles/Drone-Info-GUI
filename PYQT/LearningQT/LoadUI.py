from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic
from myButton import Ui_Form
import sys

# class UI(QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("myButton.ui",self)
#         #find our widget
#         button = self.findChild(QPushButton,"pushButton")
#         button.clicked.connect(self.clicked_btn)
#     def clicked_btn(self):
#         print("SASAASSASAAS")
# app = QApplication(sys.argv)
# window = UI()
# window.show()
# app.exec_()


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec_()
