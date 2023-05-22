from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi 
from PyQt5 import QtCore

class WindowUserAdd(QDialog):
    def __init__(self,*args, parent=None):
        super(WindowUserAdd,self).__init__(parent)
        # self.parent = parent
        self.UI = loadUi("ui/userAdd.ui",self)
        self.UI.show()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.UI.closed.clicked.connect(lambda:self.close())
        self.UI.minimized.clicked.connect(self.showMinimized)