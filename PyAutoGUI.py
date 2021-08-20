import os
os.environ["DISPLAY"] = ":0" # 注意这行代码需要写在"import pyautogui"之前
import pyautogui
import pyperclip
pyautogui.click(33.5,56.5,"left")
pyautogui.hotkey('ctrl','N')#组合按键（同时按）


pyautogui.click()
pyautogui.click(300, 300, button='right')#在指定位置左键点击，button可以
pyautogui.mouseDown()#按下不放
pyautogui.mouseUp()#释放鼠标按键
pyautogui.doubleClick()#双击左键
pyautogui.rightClick()#双击右键
pyautogui.middleClick()#双击中键


pyperclip.copy("启动自动防故障功能（鼠标移到屏幕的做上角，将导致pyautogui产生pyautogui.FailSafeException异常）在自动化测试项目中，为了不自动跳出用例脚本，通常设置未False")
pyperclip.paste()
pyautogui.typewrite("message李行周") #输入内容
pyperclip.copy("qqqqqqqqqqqqqqqqqqqqqqqqqqqqq启动自动防故障功能（鼠标移到屏幕的做上角，将导致pyautogui产生pyautogui.FailSafeException异常）在自动化测试项目中，为了不自动跳出用例脚本，通常设置未False")
pyperclip.paste()
pyautogui.PAUSE = 1#，每个执行动作之后，都会等待1s
pyautogui.FAILSAFE = True#，启动自动防故障功能（鼠标移到屏幕的做上角，将导致pyautogui产生pyautogui.FailSafeException异常）在自动化测试项目中，为了不自动跳出用例脚本，通常设置未False
print(pyautogui.size())
pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveRel(300, 350, duration=0.25)
#pyautogui.positon()

pyautogui.dragTo()#鼠标拖动到一个位置
pyautogui.dragRel()#相对当前拖到一个距离的位置
pyautogui.scroll(3) #上下滚动的单位
image = pyautogui.screenshot()# ，image是一个屏幕快照的对象

#image.getpixel(300,400)# 返回图像中坐标处的像素对象，返回值是一个RGB元组，包含3个整数。
#pyautogui.pixelMatchesColor(50, 200,(130,135,144)) >>True
pyautogui.typewrite("message") #输入内容
pyautogui.typewrite(['ctrl','alt','a','left'])#从左到右，先后顺序按键盘的按键
pyautogui.keyDown('shift')#按住不放
#pyautogui.keyUp()#键盘松开
pyautogui.press('ctrl')#单个按键
pyautogui.hotkey('ctrl','v')#组合按键（同时按）