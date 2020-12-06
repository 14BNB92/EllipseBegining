import sys

from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor


class EllipseBegin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(350, 500)
        self.setWindowTitle('EllipseBegin')
        self.do_paint = False
        self.drawbtn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        a = randint(50, 300)
        qp.setBrush(QColor(255, 250, 0))
        qp.drawEllipse(50, 200, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    eb = EllipseBegin()
    eb.show()
    sys.exit(app.exec())
