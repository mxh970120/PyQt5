# -*- coding: utf-8 -*-

import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.Qtwidgets模块中。
# Qtwidgets模块包含创造经典桌面风格的用户界面提供了一套UI元素的类。
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    # QWidget部件是pyqt5所有用户界面对象的基类。
    w = QWidget()
    # resize()方法调整窗口的大小。
    w.resize(400, 400)
    # 窗口所在位置x = 300，y = 300。
    w.move(300, 300)
    # 设置窗口的标题
    w.setWindowTitle('Simple')
    # 显示在屏幕上
    w.show()
    # exit()方法确保应用程序干净的退出
    # exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替(用于兼容pyqt4, 如果不考虑兼容，不需要下划线)
    sys.exit(app.exec())