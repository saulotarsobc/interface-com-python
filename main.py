#! py
import sys
from time import sleep
import interface as home
from PyQt5 import QtWidgets

app = home.QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = home.Ui_MainWindow()
ui.setupUi(MainWindow)


def teste():
    print('teste')

if __name__ == "__main__":    
    """ init """
    MainWindow.show()
    sys.exit(app.exec_())
    teste()
    sleep(3)