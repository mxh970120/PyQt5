# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

# 通过QObject创建的对象可以发出信号。
class Communicate(QObject):
    # 信号closeApp是Communicate的类属性，它由pyqtSignal()创建。
    closeApp = pyqtSignal(int)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建了一个名为closeApp的信号。这个信号会在按下鼠标时触发，它连接着QMainWindow的close()插槽。
        self.c = Communicate()

        # 一个信号连接多个槽
        self.c.closeApp.connect(self.close)
        self.c.closeApp.connect(self.signalCall)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def signalCall(self, val):
        print(val)

    # 当在窗体上点击鼠标时会触发closeApp信号，使程序退出。(这个函数继承自父类)
    def mousePressEvent(self, event):
        self.c.closeApp.emit(1)  # 发射信号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
