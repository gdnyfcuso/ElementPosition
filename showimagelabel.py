
from PyQt5.QtGui import QImage,QPixmap
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
 
 
class showimageposition(QLabel):
    x0 = 150
    y0 = 120
    x1 = 400
    y1 = 220
 
    #绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
        painter.drawRect(rect)
    def updatepositionarea(self,rectangle=None):
        if rectangle is not None:
            self.x0 = rectangle[0][0]
            self.y0 = rectangle[0][1]
            self.x1 = rectangle[3][0]
            self.y1 =rectangle[3][1]
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.showarealabel = showimageposition("输入区") #重定义的label
        # img = cv2.imread('aa.png')
        # showImage = QImage(img.data, img.shape[1], img.shape[0],
        #              QImage.Format_RGB888)  # 把读取到的图片数据变成QImage形式
        # 往显示视频的Label里 显示QImage
        cutimag= QtGui.QPixmap('bb.bmp')
        self.showarealabel.setGeometry(cutimag.rect())
        # self.cutlabel.setGeometry()
        self.showarealabel.setPixmap(cutimag)
        self.showarealabel.setCursor(Qt.CrossCursor)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.addWidget(self.showarealabel)
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = Example()
    sys.exit(app.exec_())