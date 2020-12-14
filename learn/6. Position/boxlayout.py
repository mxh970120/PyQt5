# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        okButton2 = QPushButton("OK2")
        cancelButton2 = QPushButton("Cancel2")

        # QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局。
        # 创建一个水平布局和添加一个伸展因子和两个按钮。两个按钮前的伸展增加了一个可伸缩的空间。这将推动他们靠右显示。
        hbox1 = QHBoxLayout()
        # The addStretch method adds a QSpacerItem to the end of a box layout. A QSpacerItem is an adjustable blank space.
        hbox1.addStretch(1)
        hbox1.addWidget(okButton)
        hbox1.addWidget(cancelButton)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(okButton2)
        hbox2.addStretch(1)
        hbox2.addWidget(cancelButton2)

        # 创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)


        # 设置窗口的布局界面
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())