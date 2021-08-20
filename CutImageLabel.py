

from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QFileDialog,QMessageBox,QMainWindow
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
import cv2
import sys

class CutImageLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    runing=True
    mainwidow=None

    def start(self,Ui_MainWindow=None):
        self.setCursor(Qt.CrossCursor)
        self.runing=True
        self.mainwidow=Ui_MainWindow
    def stop(self):
        self.setCursor(Qt.ArrowCursor)
        self.runing=False
        self.hide()


#鼠标点击事件
    def mousePressEvent(self,event):
        if self.runing:
            if event.button() == Qt.LeftButton:
                self.flag = True
                self.x0 = event.x()
                self.y0 = event.y()
    #鼠标释放事件
    def mouseReleaseEvent(self,event):
        if self.runing:
             if event.button() == Qt.LeftButton:
                self.flag = False
                # rect = QRect(self.label.startPoint, self.label.endPoint)
                rect = QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))

                # A = QMessageBox.question(self,'确认','选择结束',QMessageBox.Yes | QMessageBox.No)
                # if A == QMessageBox.Yes:
                    #outputRegion = self.img.copy(rect)# screenshot.copy(rect)
                    #self.temp=self.pixmap().copy();/home/lixingzhou/下载/元素定位/
                outputRegion =self.img.copy(rect)# screenshot.copy(rect)
                outputRegion.save('/home/lixingzhou/下载/元素定位/bb.png', format='png', quality=100)
                self.stop()
                if self.mainwidow is not None:
                    self.mainwidow.showcutImage()                                        

    #鼠标移动事件
    def mouseMoveEvent(self,event):
        if self.runing:
            if self.flag:
                self.x1 = event.x()
                self.y1 = event.y()
                self.update()
    #绘制事件
    def paintEvent(self, event):
        if self.runing:
            super().paintEvent(event)
            rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
            painter.drawRect(rect)
        else:
            super().paintEvent(event)
            rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
            painter = QPainter(self)
            painter.setPen(QPen(Qt.NoPen))
            painter.drawRect(rect)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(675, 300)
        self.setWindowTitle('在label中绘制矩形')
        self.lb = CutImageLabel(self) #重定义的label
        self.lb.setGeometry(QRect(30, 30, 511, 541))
        img = cv2.imread('aa.png')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine,QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        self.lb.img=pixmap
        self.lb.setPixmap(pixmap)
        self.lb.setCursor(Qt.CrossCursor)
        self.lb.start()
        self.show()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    x = Example()
    sys.exit(app.exec_())