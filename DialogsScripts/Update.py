from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi 
from PyQt5 import QtGui
from data.conection import DbUser as db

class UpdateTable(QDialog):
    def __init__(self,*args, parent = None ): 
        super(UpdateTable,self).__init__(parent)
        self.load = loadUi('ui/EditTable.ui',self)
        self.load.show()
        self.id = args[0]
        self.messages = args[1]
        self.ReduceWindow = args[2]
        self.btnExpandWindow = args[3]
########################### icons ################################################
        iconBtnClose = QtGui.QIcon()
        iconBtnClose.addPixmap(QtGui.QPixmap("iconos/icons/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_close.setIcon(iconBtnClose)
        
        iconExpand = QtGui.QIcon()
        iconExpand.addPixmap(QtGui.QPixmap("iconos/icons/maximize.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_maximize.setIcon(iconExpand)

        iconMinimize = QtGui.QIcon()
        iconMinimize.addPixmap(QtGui.QPixmap("iconos/icons/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_minimize.setIcon(iconMinimize)

        iconReduce = QtGui.QIcon()
        iconReduce.addPixmap(QtGui.QPixmap("iconos/icons/minimize-2.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_reduce.setIcon(iconReduce)

        iconPaper = QtGui.QIcon()
        iconPaper.addPixmap(QtGui.QPixmap("iconos/remove_paper.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.imgPaper.setIcon(iconPaper)

        iconSave = QtGui.QIcon()
        iconSave.addPixmap(QtGui.QPixmap("iconos/icons/save.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.BtnEditSave.setIcon(iconSave)

        iconBtnSearchTables = QtGui.QIcon()
        iconBtnSearchTables.addPixmap(QtGui.QPixmap("iconos/icons/search.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.BtnEditSearch.setIcon(iconBtnSearchTables)

################################ btn events #########################################################
        self.load.btn_close.clicked.connect(lambda: self.close())
        self.load.BtnEditCancel.clicked.connect(lambda: self.close())
        self.load.btn_minimize.clicked.connect(self.showMinimized)
        self.load.btn_reduce.hide()
        self.load.btn_maximize.clicked.connect(lambda: self.btnExpandWindow(self,self.load.btn_maximize,self.load.btn_reduce))
        self.load.btn_reduce.clicked.connect(lambda: self.ReduceWindow(self,self.load.btn_maximize,self.load.btn_reduce ))