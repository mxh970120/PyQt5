# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication)
from PyQt5.QtCore import QDate

# 创建了一个日历控件和一个标签控件。选择的日期会显示在标签控件中。
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        # 如果我们从部件选择一个日期,点击[QDate]发出信号。我们将这个信号连接到用户定义的showDate()方法。
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        # 检索所选日期通过调用selectedDate()方法。然后我们将date对象转换为字符串,并将其设置为小部件的标签。
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())