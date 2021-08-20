import sys
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut
from Ui_CutFullScreenImagecopy import Ui_MainWindow
from PyQt5.QtWidgets import *

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+Q")), self, self.close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())