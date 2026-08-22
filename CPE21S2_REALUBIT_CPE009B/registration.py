import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__() 
        self.title = "Account Registration"
        self.width = 450
        self.height = 420
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.center_window()


        start_x_label = 50
        start_x_entry = 180
        row_spacing = 40      
        y = 80  

        QLabel("First Name:", self).move(start_x_label, y)
        self.first_name = QLineEdit(self)
        self.first_name.move(start_x_entry, y)
    
        y += row_spacing
        QLabel("Last Name:", self).move(start_x_label, y)
        self.last_name = QLineEdit(self)
        self.last_name.move(start_x_entry, y)

        y += row_spacing
        QLabel("Username:", self).move(start_x_label, y)
        self.username = QLineEdit(self)
        self.username.move(start_x_entry, y)

        y += row_spacing
        QLabel("Password:", self).move(start_x_label, y)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.move(start_x_entry, y)

        y += row_spacing
        QLabel("Email Address:", self).move(start_x_label, y)
        self.email = QLineEdit(self)
        self.email.move(start_x_entry, y)


        y += row_spacing
        QLabel("Contact Number:", self).move(start_x_label, y)
        self.contact = QLineEdit(self)
        self.contact.move(start_x_entry, y)
        
        buttons_y = y + row_spacing + 20
        
        self.submit = QPushButton("Submit", self)
        self.submit.move(start_x_entry, buttons_y)
        
        self.clear = QPushButton("Clear", self)
        self.clear.move(start_x_entry + 105, buttons_y)

    def center_window(self):
        screen = self.screen().availableGeometry()
        x = (screen.width() - self.width) // 2
        y = (screen.height() - self.height) // 2
        self.move(x, y)
