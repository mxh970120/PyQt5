# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

# Pyqt5使用OOP编程。这里我们创建一个新的类为Example。Example继承自QWidget类。
class Example(QWidget):

    def __init__(self):
        # super() 函数是用于调用父类的一个方法。
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小(x, y, 长, 宽)
        self.setGeometry(300, 300, 300, 300)
        # 设置窗口的标题
        self.setWindowTitle('Icontest')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('Icon.JPG'))

        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())