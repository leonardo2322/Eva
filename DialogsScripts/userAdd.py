from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi 

class WindowUserAdd(QDialog):
    def __init__(self,*args, parent=None):
        super(WindowUserAdd,self).__init__(parent)
        # self.parent = parent
        self.UI = loadUi("ui/userAdd.ui",self)
        self.UI.show()

        self.UI.closed.clicked.connect(lambda:self.close())
        self.UI.minimized.clicked.connect(self.showMinimized)