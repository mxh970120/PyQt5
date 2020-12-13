# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    # 这是继承自父类的函数，当关闭窗口时触发
    def closeEvent(self, event):

        # reply = QMessageBox.critical(self, 'Message', "Are you sure to quit?",
        #                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # reply = QMessageBox.warning(self, 'Message', "Are you sure to quit?",
        #                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())