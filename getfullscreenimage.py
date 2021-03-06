
import time
import win32gui, win32ui, win32con, win32api


def window_capture(filename):
    hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


    
if __name__ == "__main__":
    beg = time.time()
    for i in range(10):
        window_capture("haha.jpg")
        end = time.time()
        print(end - beg)

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5 import QtGui,QtCore
# import keyboard
# import random


# class Trans(QWidget):
#     def cut(self):
#         screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
#         outputRegion = screenshot.copy()
#         outputRegion.save('sho54t.bmp', format = 'bmp', quality = 100)
#         self.close()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     trans = Trans()
#     trans.cut()
#     trans.show()
#     sys.exit(app.exec_())


   