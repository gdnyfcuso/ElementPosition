#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dogtail.tree import *
import time

# 获取应用程序（根据程序名称查找）
app = root.application(appName="Sample01", description="/home/waleon/workspace/demos/build-Samples-unknown-Debug/Sample01/Sample01")

# 获取按钮（根据 accessibleName 递归查找）
button = app.child('button')

# 模拟鼠标点击
for i in range(3):
    button.click()
    sleep(1)