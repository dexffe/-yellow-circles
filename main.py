import sys
import random
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import Qt


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.qwe)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.draw:
            painter = QPainter(self)
            painter.begin(self)
            self.run(painter)
            painter.end()
            self.draw = False

    def run(self, painter):
        self.size = random.randint(10, 200)
        self.x = random.randint(0, self.width() - self.size)
        self.y = random.randint(0, self.height() - self.size)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.drawEllipse(self.x, self.y, self.size, self.size)

    def qwe(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
