import sys
from PyQt5.QtWidgets import (QApplication,
        QDialog)
from PyQt5 import QtGui,QtCore

from PyQt5.uic import loadUi 
from main import Eva
from passlib.hash import pbkdf2_sha256
from data.conection import DbUser
from data.methods import methodsUSER
from data.CreationDb import Data
class InitSesion(QDialog):
    def __init__(self):
        super().__init__()
        self.db = DbUser()
        self.ui = loadUi('ui/initsesion.ui', self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #BBDD = Data()
        self.idUser = ''
        self.ui.btn_sesion_destroy.clicked.connect(lambda:self.close())
        iconBtnDelete = QtGui.QIcon()
        iconBtnDelete.addPixmap(QtGui.QPixmap("iconos/icons/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ui.btn_sesion_destroy.setIcon(iconBtnDelete)
        
        self.ui.Frame_Top.mouseMoveEvent = self.MoveWindow
        iconReduce = QtGui.QIcon()
        iconReduce.addPixmap(QtGui.QPixmap("iconos/icons/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ui.btn_sesion_minimize.setIcon(iconReduce)

        self.ui.btn_sesion_minimize.clicked.connect(self.showMinimized)
        self.ui.lbl_paper.setPixmap(QtGui.QPixmap("iconos/remove_paper.png"))

        self.ui.btn_init_sesion.clicked.connect(self.InitSesion)
        self.ui.btn_init_sesion.setDefault(True)
        self.show()


        self.ui.btn_sesion_destroy



    def InitSesion(self):
        usuario = self.ui.Input_user.text().strip()
        password = self.ui.Input_pass.text().strip()
        if len(usuario) > 0 and len(password) > 0:
            query = self.db.SelectFromDB(name = usuario,selection=methodsUSER['USER'])
            try:
                if usuario == query[1] and password == query[2]:
                    self.idUser = query[0]
                    
                    self.ui.hide()
                    Eva(self.idUser,usuario)
                else:
                    Eva.mensagges(self, 'el usuario es incorrecto o la contraseña')
                   
                
                          
            except Exception as e:
                print('en exeption',e) 
                Eva.mensagges(self, 'el usuario es incorrecto o la contraseña')                
        else:
            Eva.mensagges(self,'No hay datos Introduce tus datos')


    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def MoveWindow(self, event):
        try:
            if self.isMaximized() == False and event.buttons() ==QtCore.Qt.LeftButton:
                
                self.move(self.pos()+ event.globalPos() - self.clickPosition)
                self.clickPosition= event.globalPos()
                event.accept()
       
        except Exception as e:
            Eva.mensagges(self, 'para mover la pantalla preciona la parte superior izquierda')

if __name__=='__main__':
    app = QApplication(sys.argv)
    Sesion = InitSesion()
    Sesion.show()

    sys.exit(app.exec_())