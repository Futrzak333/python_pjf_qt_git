from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("qt.ui", self)


app = QApplication(sys.argv)
window = Window()
window.show()
exit(app.exec())
