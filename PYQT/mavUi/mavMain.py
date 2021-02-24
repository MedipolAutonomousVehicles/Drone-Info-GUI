from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from mavUi import Ui_Form
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec_()
