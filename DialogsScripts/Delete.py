from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi 
from PyQt5 import QtGui
from data.conection import DbUser as db

class DeleteVTable(QDialog):
    def __init__(self,*args, parent = None ): 
        super(DeleteVTable,self).__init__(parent)
        self.load = loadUi('ui/TableDelete.ui',self)