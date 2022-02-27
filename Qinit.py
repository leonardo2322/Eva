import sys
from PyQt5.QtWidgets import (QApplication,
        QDialog)
from PyQt5 import QtGui
from PyQt5.uic import loadUi 
from data.dbManage import DbUser
from main import Eva
from threading import Thread

class treadding(Thread):
    def __init__(self, windo):
        Thread.__init__(self)
        self.ventan = windo
        self.mostrar()
    def mostrar(self):
        Sesion.hide()
        self.ventan()
        self.start()

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

        self.ui.btn_init_sesion.clicked.connect(self.InitSesion)
        self.show()


        self.ui.btn_sesion_destroy

    def InitSesion(self):
        usuario = self.ui.Input_user.text().strip()
        password = self.ui.Input_pass.text().strip()
        if len(usuario) > 0 and len(password) > 0:
            try:
                self.dab = DbUser().usersInit(usuario, password)
                if self.dab[1] == usuario:
                    if self.dab[2] == password:
                        treadding(Eva)
                    else:
                        Eva.mensagges(self,'la contraseña son incorrectos')
                else:
                    Eva.mensagges(self, 'el usuario es incorrecto')       
            except:
                Eva.mensagges(self, 'ocurrio un error datos incorrectos')
                
        else:
            Eva.mensagges(self,'No hay datos Introduce tus datos')






if __name__=='__main__':
    app = QApplication(sys.argv)
    Sesion = InitSesion()
    Sesion.show()

    sys.exit(app.exec_())