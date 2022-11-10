import play
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication
import sys
import pygame
class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        pygame.init()
        pygame.mixer.init()
    #main menu
        self.setWindowTitle('Самолеты')
        self.setWindowIcon(QtGui.QIcon('main.png'))
        self.resize(879, 704)
        self.setFixedSize(self.size())
        image = QtGui.QImage("main_menu_fon.png")
        sImage = image.scaled(QtCore.QSize(879, 704))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)
    #button play
        self.Play = QPushButton(self)
        self.Play.setGeometry(QtCore.QRect(320, 210, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(30)
        self.Play.setFont(font)
        self.Play.setText("PLAY")
        self.Play.setStyleSheet("QPushButton {background-color: rgba(47, 4, 4, 0.69); color: red; border-radius: 18px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.Play.clicked.connect(play.main)
    #button record
        self.see_the_record = QPushButton(self)
        self.see_the_record.setGeometry(QtCore.QRect(320, 290, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(30)
        self.see_the_record.setFont(font)
        self.see_the_record.setText("RECORD")
        self.see_the_record.setStyleSheet("QPushButton {background-color: rgba(47, 4, 4, 0.69); color: red; border-radius: 18px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.see_the_record.clicked.connect(self.press_record)
    #button login
        self.login = QPushButton(self)
        self.login.setGeometry(QtCore.QRect(20, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(10)
        self.login.setFont(font)
        self.login.setText("LOG IN")
        self.login.setStyleSheet("QPushButton {background-color: rgba(47, 4, 4, 0.69); color: red; border-radius: 18px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
    #button exit
        self.exit = QPushButton(self)
        self.exit.setGeometry(QtCore.QRect(320, 370, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(30)
        self.exit.setFont(font)
        self.exit.setText("EXIT")
        self.exit.setStyleSheet("QPushButton {background-color: rgba(47, 4, 4, 0.69); color: red; border-radius: 18px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.exit.clicked.connect(self.press_exit)
    #the function closes the program on pressing the button "EXIT"
    def press_exit(self):
        sys.exit()
    #the function shows the user's record
    def press_record(self):
        count = 100
        record_mes = QtWidgets.QMessageBox()
        record_mes.setIcon(QtWidgets.QMessageBox.Information)
        record_mes.setText(f"Your record - {100}")
        record_mes.setWindowTitle("RECORD")
        record_mes.setStandardButtons(QtWidgets.QMessageBox.Ok)
        record_mes.exec_()
def application():
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()

