import os
import subprocess
import sys
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QWidget,
    QGridLayout,
)
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebView


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Cmd:
    def sensor_start(self):
        print("Sensor Start button click")
        subprocess.Popen("exec " + "python remotedata.py", shell=True)

    def sensor_end(self):
        print("Sensor End button click")

    subprocess.Popen("pkill -f remotedata.py", shell=True)

    def mission_start(self):
        print("Mission Start button click")
        subprocess.Popen("rosrun mavros mavsafety arm", shell=True)
        time.sleep(1)
        subprocess.Popen("rosrun mavros mavsys mode -c OFFBOARD", shell=True)

    def mission_end(self):
        print("Mission End button click")
        subprocess.Popen("rosrun mavros mavsys mode -c AUTO.RTL", shell=True)

    def mission_hold(self):
        print("Mission Hold button click")
        subprocess.Popen("rosrun mavros mavsys mode -c AUTO.LOITER", shell=True)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(1280, 800))
        self.setWindowTitle("Ocean Exploration UAV")
        self.statusBar().showMessage(
            "Copyright 2020 www.uaslaboratory.com. All rights reserved."
        )

        # SENSOR
        self.nameLabel0 = QLabel("Sensor:")

        # MISSION
        self.nameLabel1 = QLabel("Mission:")

        # SENSOR: Start Data Logging
        button_start_logging = QPushButton("Start", toolTip="Start data logging")
        button_start_logging.clicked.connect(cmd.sensor_start)

        # SENSOR: Start Data Logging
        button_end_logging = QPushButton("End", toolTip="End data logging")
        button_end_logging.clicked.connect(cmd.sensor_end)

        # MISSION: Start Mission
        button_start_uav = QPushButton("Start", toolTip="Start UAV mission")
        button_start_uav.clicked.connect(cmd.mission_start)

        # MISSION: End Mission
        button_end_uav = QPushButton("End", toolTip="End UAV mission")
        button_end_uav.clicked.connect(cmd.mission_end)

        # MISSION: Hold Mission
        button_hold_uav = QPushButton("Hold", toolTip="Hold UAV mission")
        button_hold_uav.clicked.connect(cmd.mission_hold)

        web = QWebView()
        web.settings().setAttribute(QWebSettings.JavascriptEnabled, True)

        filename = os.path.join(CURRENT_DIR, "map.html")
        url = QUrl.fromLocalFile(filename)
        web.load(url)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        lay = QGridLayout(central_widget)
        lay.addWidget(self.nameLabel0, 0, 0)
        lay.addWidget(button_start_logging, 0, 1)
        lay.addWidget(button_end_logging, 0, 2)
        lay.addWidget(self.nameLabel1, 1, 0)
        lay.addWidget(button_start_uav, 1, 1)
        lay.addWidget(button_end_uav, 1, 2)
        lay.addWidget(button_hold_uav, 1, 3)
        lay.addWidget(web, 2, 0, 1, 5)
        lay.setColumnStretch(4, 1)


if __name__ == "__main__":
    cmd = Cmd()

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()

    sys.exit(app.exec_())
    time.sleep(5)