import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectButton.clicked.connect(self.printValue())


    def printValue(self):
        print(self.ui.serverIp.text())





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
