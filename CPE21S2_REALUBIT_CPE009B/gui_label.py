import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__() #initializes the main window like the previous one
        # window = QMainWindow()
        self.title = "PyQt Button"
        self.x = 200 #or left
        self.y = 200 #or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('python.ico'))

        self.textboxbl = QLabel("Hello, World! ", self)
        self.textboxbl.move(30, 25)

        self.textboxb2 = QLabel("This program is written in Pycharm", self)
        self.textboxb2.move(50,140)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())