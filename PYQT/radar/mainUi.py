# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 405)
        self.Form = Form
        self._translate = QtCore.QCoreApplication.translate

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 401))
        self.label.setObjectName("label")
        self.translateWidget(self.label,"<html><head/><body><p><img src=\":/newPrefix/radar400x400.png\"/><img src=\":/newPrefix/enemy10x10.png\"/></p></body></html>")

        self.label_2 = QtWidgets.QLabel(self.Form)
        self.label_2.setGeometry(QtCore.QRect(192, 192, 16, 16))
        self.label_2.setObjectName("label_2")
        self.translateWidget(self.label_2,"<html><head/><body><p><img src=\":/newPrefix/enemy10x10.png\"/></p></body></html>")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(165, 385, 60, 20))
        self.pushButton.setObjectName("pushButton")
        self.translateWidget(self.pushButton,"Click Me")

        self.enemyList()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def enemyList(self):
        self.enemy0 = QtWidgets.QLabel(self.Form)
        self.enemy0.setGeometry(QtCore.QRect(192, 192, 16, 16))
        self.enemy0.setObjectName("enemy0")
        self.translateWidget(self.enemy0,"<html><head/><body><p><img src=\":/newPrefix/enemy10x10.png\"/></p></body></html>")

        self.enemy1 = QtWidgets.QLabel(self.Form)
        self.enemy1.setGeometry(QtCore.QRect(192, 192, 16, 16))
        self.enemy1.setObjectName("enemy1")
        self.translateWidget(self.enemy1,"<html><head/><body><p><img src=\":/newPrefix/enemy10x10.png\"/></p></body></html>")



    def changeEnemyPos(self,enemyNumber,x,y):
        enemyList = [self.enemy0, self.enemy1]
        #self.enemy0.setGeometry()
        enemyList[enemyNumber].setGeometry(QtCore.QRect(x,y,16,16))


    def translateWidget(self,widget,dest):
        widget.setText(self._translate("Form",f"{dest}"))

    def retranslateUi(self, Form):
        #_translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(self._translate("Form", "Form"))
        # self.label.setText(self._translate("Form", "<html><head/><body><p><img src=\":/newPrefix/radar400x400.png\"/><img src=\":/newPrefix/enemy10x10.png\"/></p></body></html>"))
        # self.label_2.setText(self._translate("Form", "<html><head/><body><p><img src=\":/newPrefix/enemy10x10.png\"/></p></body></html>"))
        # self.pushButton.setText(self._translate("Form","Click Me"))
import radar_rc
