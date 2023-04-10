from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi 
from PyQt5 import QtGui

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog,self).__init__(parent)
        self.load = loadUi("ui/DatosDeTabla.ui",self)
        self.load.btn_reduce.hide()
#################################---Icons----########################################        
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

        self.load.btn_guardar.setIcon(iconSave)
#################################---Events Clicked----############################### 

        self.load.btn_reduce.clicked.connect(self.ReduceWindow)
        self.load.btn_close.clicked.connect(lambda: self.close())
        self.load.btn_maximize.clicked.connect(self.showMaximizedWindow)
        self.load.btn_minimize.clicked.connect(lambda: self.showMinimized())


        #-------------clicked actions-------------
        self.load.btn_ingreso.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.IngresoStack))
        self.load.btn_gasto.clicked.connect(lambda: self.load.stackedWidget.setCurrentWidget(self.load.GastoStack))
#################################---Functions----##################################### 

   
    def showMaximizedWindow(self):
        self.showMaximized()
        self.load.btn_maximize.hide()
        self.load.btn_reduce.show()


    def ReduceWindow(self):
        self.showNormal()
        self.load.btn_reduce.hide()
        self.load.btn_maximize.show()