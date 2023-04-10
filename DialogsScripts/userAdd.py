from PyQt5.QtWidgets import  QMainWindow
from PyQt5.uic import loadUi 

class WindowUserAdd(QMainWindow):
    def __init__(self,parent=None):
        super(WindowUserAdd,self).__init__()
        # self.parent = parent
        self.UI = loadUi("QdialogsUi/tableUserCreate.ui",self)
        self.UI.show()

        self.UI.closed.clicked.connect(lambda:self.close())
        self.UI.minimized.clicked.connect(self.showMinimized)