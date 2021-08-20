# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'i:\Python\git\元素定位\qttest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.JieImg = QtWidgets.QPushButton(self.centralwidget)
        self.JieImg.setObjectName("JieImg")
        self.gridLayout.addWidget(self.JieImg, 1, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 2, 1, 1, QtCore.Qt.AlignTop)
        self.myRPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.myRPlainTextEdit.setObjectName("myRPlainTextEdit")
        self.gridLayout.addWidget(self.myRPlainTextEdit, 2, 1, 1, 1)
        self.MytextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.MytextEdit.setStyleSheet("color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));\n"
"selection-color: rgb(255, 255, 255);")
        self.MytextEdit.setObjectName("MytextEdit")
        self.gridLayout.addWidget(self.MytextEdit, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.lixz = QtWidgets.QAction(MainWindow)
        self.lixz.setCheckable(True)
        self.lixz.setObjectName("lixz")

        self.retranslateUi(MainWindow)
        self.JieImg.clicked.connect(self.myRPlainTextEdit.paste)
        self.myRPlainTextEdit.blockCountChanged['int'].connect(self.MytextEdit.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeepAiImagePosigion"))
        self.JieImg.setText(_translate("MainWindow", "截图"))
        self.progressBar.setToolTip(_translate("MainWindow", "<html><head/><body><p>进度条</p></body></html>"))
        self.myRPlainTextEdit.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>这是源数据表</p></body></html>"))
        self.lixz.setText(_translate("MainWindow", "123"))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())