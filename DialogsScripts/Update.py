from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi 
from PyQt5 import QtGui
from data.conection import DbUser as db

class UpdateTable(QDialog):
    def __init__(self,*args, parent = None ): 
        super(UpdateTable,self).__init__(parent)
        self.load = loadUi('ui/EditTable.ui',self)
        self.id = args[0]
        self.messages = args[1]
        self.ReduceWindow = args[2]
        self.btnMinimizeWindow = args[3]
        self.btnExpandWindow = args[4]



################################ btn events #########################################################
        self.load.btn_reduce.hide()
        self.load.btn_maximize.clicked.connect(lambda: self.btnExpandWindow(self,self.load.btn_maximize,self.load.btn_reduce))
        self.load.btn_reduce.clicked.connect(lambda: self.ReduceWindow(self,self.load.btn_maximize,self.load.btn_reduce ))