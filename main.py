from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randrange, choice
from UI import Ui_MainWindow
import sys


class Circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.can_draw = False
        self.draw.clicked.connect(self.draw_el)
        self.setWindowTitle('Рисование кругов')
        self.colors = [Qt.black, Qt.yellow, Qt.red, Qt.darkRed, Qt.green, Qt.darkGreen,
                       Qt.blue, Qt.darkBlue, Qt.cyan, Qt.darkCyan, Qt.magenta, Qt.darkMagenta,
                       Qt.darkYellow, Qt.gray, Qt.darkGray, Qt.lightGray, Qt.transparent, Qt.color0,
                       Qt.color1]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(choice(self.colors),  8, Qt.SolidLine))
        diam = randrange(1, 500)
        painter.drawEllipse(0, 0, diam, diam)

    def draw_el(self):
        self.can_draw = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
