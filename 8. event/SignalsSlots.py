# -*- coding: utf-8 -*-

"""
所有的GUI程序都是事件驱动的。事件主要由用户触发，但也可能有其他触发方式：例如网络连接、window manager或定时器。
当我们调用QApplication的exec()方法时会使程序进入主循环。主循环会获取并分发事件。

在事件模型中，有三个参与者：
事件源: 事件源是状态发生变化的对象。它会生成事件。
事件对象: 事件(对象)封装了事件源中状态的变动。
事件接收者: 事件接收者是要通知的对象。事件源对象将事件处理的工作交给事件接收者。
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # PyQt5有一个独特的signal&slot(信号槽)机制来处理事件。信号槽用于对象间的通信。
        # signal在某一特定事件发生时被触发，slot可以是任何callable对象。当signal触发时会调用与之相连的slot。
        initial = 20
        lcd = QLCDNumber(self)  # QLCDNumber小部件显示一个类似LCD的数字。
        lcd.display(initial)
        sld = QSlider(Qt.Horizontal, self)  # QSlider控件提供一个垂直或者水平的滑动条
        sld.setValue(initial)
        # sld = QSlider(Qt.Vertical, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)  # valueChanged信号连接到lcd的display插槽

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())