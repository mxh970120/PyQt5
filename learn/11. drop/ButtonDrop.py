# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

#  我们从QPushButton派生了一个Button类，并重新实现了mouseMoveEvent()与mousePressEvent()方法。mouseMoveEvent()方法是拖放操作产生的地方
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        # 在这里我们设置只在鼠标右击时才执行拖放操作。鼠标左击用于按钮的点击事件
        if e.buttons() != Qt.RightButton:
            return
        # QDrag提供了对基于MIME的拖放的数据传输的支持
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):

        # 鼠标左击按钮时我们会在控制台打印‘press’。注意我们也调用了父按钮的mousePressEvent()方法。否则会看不到按钮的按下效果
        QPushButton.mousePressEvent(self, e)

        if e.button() == Qt.LeftButton:
            print('press')


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        # 释放右键后调用dropEvent()方法中，即找出鼠标指针的当前位置，并将按钮移动过去
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())