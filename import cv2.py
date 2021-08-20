import numpy as np
import cv2
import screeninfo
import aircv as ac
import pythoncom
import PyHook3 as pyHook
import time
import threading
import datetime
import sys
import win32api
import win32con
import win32gui
import win32.win32clipboard as win32clipboard
import getfullscreenimage 
import pictureElementPosigioning 


from ctypes import *
import tkinter
 
# print circle_center_pos
def draw_circle(img, pos, circle_radius, color, line_width):
    cv2.circle(img, pos, circle_radius, color, line_width)
    cv2.imshow('objDetect', imsrc) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    user32 = windll.user32
    hwnd = user32.GetForegroundWindow()    
    win32gui.CloseWindow(hwnd) # 窗口最小化
    
    simagename='aa.png'

    iscurrentscreen=False
    
    if iscurrentscreen:
        getfullscreenimage.window_capture(simagename)

    po=dict(spath=simagename,dpath=r'bb.png')
    pos=pictureElementPosigioning.getPositionBylocationmap(po)
    
    imsrc = ac.imread(simagename)
#     imobj = ac.imread('bb.png')
 
#  # find the match position
#     pos = ac.find_template(imsrc, imobj)
    print(pos)
    if pos is not None:
        circle_center_pos = pos['result']
        myrectangle=pos['rectangle']
        circle_radius = 50
        color = (0, 0, 255)
        line_width = 1
    
    # draw circle
        cv2.rectangle(imsrc, myrectangle[0],myrectangle[3], color, line_width)
        screen_id= 0
        is_color= True
    
        # get the size of the screen
        screen= screeninfo.get_monitors()[screen_id]
        width, height= screen.width, screen.height
    
        # create image
        if is_color:
            image= np.ones((height, width,3), dtype=np.float32)
            image[:10, :10]= 0  # black at top-left corner
            image[height- 10:, :10]= [1,0,0] # blue at bottom-left
            image[:10, width- 10:]= [0,1,0] # green at top-right
            image[height- 10:, width- 10:]= [0,0,1] # red at bottom-right
        else:
            image= np.ones((height, width), dtype=np.float32)
            image[0,0]= 0  # top-left corner
            image[height,0]= 0  # bottom-left
            image[0, width]= 0  # top-right
            image[height, width]= 0  # bottom-right
    
        window_name= 'output_style_full_screen'
        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(window_name, screen.x- 1, screen.y- 1)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                            cv2.WINDOW_FULLSCREEN)
        cv2.imshow(window_name, imsrc) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    #draw_circle(imsrc, (int(circle_center_pos[0]),int(circle_center_pos[1])), circle_radius, color, line_width)
    else:
        print("匹配失败")