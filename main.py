#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

In this example, we create a simple
window in PyQt6.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QToolTip, QMessageBox
from PySide6.QtGui import QFont, Qt, QPainter
from PySide6.QtCore import QRect,QTimer


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ball = QRect()
        self.ball_x = 0
        self.ball_y = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ball)
        self.timer.setInterval(100)
        self.init_ui()
        self.timer.start()

    def init_ui(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.resize(800, 600)
        ball_size = 10
        # self.ball_x = self.ball_x + 10 if self.ball_x < self.width() - ball_size else 0
        # self.ball_y = self.rect().center().y()
        self.ball = QRect(self.ball_x, self.ball_y, ball_size, ball_size)


        # btn = QPushButton('Quit', self)
        # btn.setToolTip('Quit the application')
        # btn.resize(btn.sizeHint())
        # vbox = QVBoxLayout()
        # vbox.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
        # btn.clicked.connect(QApplication.instance().quit)
        # btn.move(50, 50)
        #
        # self.setLayout(vbox)
        # self.setGeometry(300, 300, 300, 200)
        # self.center()
        self.setWindowTitle('Tooltips')
        self.show()

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.fillRect(self.ball, Qt.GlobalColor.white)
        # painter.setBrush(Qt.GlobalColor.white)
        # # ball_size = 10
        # # ball_x = self.rect().center().x() - ball_size
        # # ball_y = self.rect().center().y() - ball_size
        # painter.drawRect(ball_x, ball_y, ball_size,
        #                  ball_size)
        painter.end()

    def update_ball(self):
        self.ball.translate(10, 0)
        if self.ball.left() > self.width():
            self.ball.moveTo(0, self.ball_y)
        self.repaint()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

            event.accept()
        else:

            event.ignore()

    # def center(self):
    #     # qr = self.frameGeometry()
    #     # cp = self.screen().availableGeometry().center()
    #     # qr.moveCenter(cp)
    #     # self.move(qr.topLeft())
    #     width = self.frameGeometry().width()
    #     height = self.frameGeometry().height()
    #     screen_width = self.screen().geometry().width()
    #     screen_height = self.screen().geometry().height()
    #     x = (screen_width - width) // 2
    #     y = (screen_height - height) // 2
    #     self.move(x, y)


def main():
    app = QApplication(sys.argv)

    w = MainWindow()
    # w.resize(250, 250)
    # # w.move(300, 300)
    #
    # w.setWindowTitle('Simple')
    # w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
