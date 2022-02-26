import sys
from PyQt5.QtWidgets import (QApplication,
        QDialog, QSizeGrip,
        QHeaderView,QMessageBox, 
        QAbstractItemView, QTableWidgetItem)
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve, Qt
from PyQt5 import QtGui
from PyQt5.uic import loadUi 
import re
from data.dbManage import DbUser


class InitSesion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = loadUi('QdialogsUi/initsesion.ui', self)
        self.ui.btn_sesion_destroy.clicked.connect(lambda:self.close())

        iconBtnDelete = QtGui.QIcon()
        iconBtnDelete.addPixmap(QtGui.QPixmap("iconos/icons/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ui.btn_sesion_destroy.setIcon(iconBtnDelete)


        iconReduce = QtGui.QIcon()
        iconReduce.addPixmap(QtGui.QPixmap("iconos/icons/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ui.btn_sesion_minimize.setIcon(iconReduce)


        self.ui.lbl_paper.setPixmap(QtGui.QPixmap("iconos/remove_paper.png"))


        self.show()


        self.ui.btn_sesion_destroy



if __name__=='__main__':
    app = QApplication(sys.argv)

    Sesion = InitSesion()
    Sesion.show()

    sys.exit(app.exec_())