from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi 
from PyQt5 import QtGui
from data.conection import DbUser as db
from data.methods import  methodINSERT,  recogDate
from datetime import datetime

class Dialog(QDialog):
    def __init__(self,*args, parent=None):
        super(Dialog,self).__init__(parent)
        self.load = loadUi("ui/DatosDeTabla.ui",self)
        self.load.show()
        self.load.btn_reduce.hide()
        self.load.date_time.setDateTime(datetime.now())
        self.load.date_timeGas.setDateTime(datetime.now())
        self.id = args[0]
        self.database = db()
        self.messageError = args[1]
        self.active = methodINSERT['ing']
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
        self.load.btn_cancelar.clicked.connect(lambda: self.close())
        self.load.btn_guardar.clicked.connect(lambda: self.QueryInsert())

        #-------------clicked actions-------------
        self.load.btn_ingreso.clicked.connect(lambda:self.changeActive('ing'))
        self.load.btn_gasto.clicked.connect(lambda: self.changeActive('gas') )
#################################---Functions----##################################### 
    def changeActive(self,type):
        if type == 'ing':
            self.load.stackedWidget.setCurrentWidget(self.load.IngresoStack), 
            self.active = methodINSERT[type]
        elif type == 'gas':
            self.load.stackedWidget.setCurrentWidget(self.load.GastoStack)
            self.active = methodINSERT[type]

    def QueryInsert(self):
        if self.active == methodINSERT['ing']:
            fechaT = recogDate(self.load.date_time.dateTime())

            data = [{'tipodepago':self.load.Cb_tipoPago.currentText(), 'categoria':self.load.Cb_categoria.currentText(),'divisa': self.load.Cb_divisa.currentText(),'fecha': fechaT, 'valor':self.load.Inp_valor.text(), 'descripcion':self.load.Inp_desc.text(),'iduser':int(self.id) }]
            
            try:
                query = self.database.QueryInsert( datos = data )
                if query == 'ok':
                    self.messageError('Se han introducidos los datos')
                else :
                    self.messageError('verifica algo ocurrio mal asegurate de introducir todos los valores')

            except  Exception as e:
                self.messageError('ocurrio un error verifica que has hecho')
                print(e)
        elif self.active == methodINSERT['gas']:
            fecha = recogDate(self.load.date_timeGas.dateTime())
            data =  [{
                'tipodepago': self.load.Cb_tipoDePagoGas.currentText(), 'categoria':self.load.Cb_cateGas.currentText(),
                'divisa': self.load.Cb_divisaGas.currentText(), 'fecha': fecha, 'valor': self.load.Inp_valorGas.text(), 'descripcion': self.load.Inp_descGas.text(), 'iduser': int(self.id)
            }]

            try:
                database = self.database.QueryInsert( datos= data, type=methodINSERT['gas'] )
                if database == 'ok':
                    self.messageError('Se han introducidos los datos')
                else :
                    self.messageError('verifica algo ocurrio mal asegurate de introducir todos los valores')
            except Exception as e:
                print(e)
        else:
            self.messageError('ocurrio algo verifica que has hecho')


    def showMaximizedWindow(self):
        self.showMaximized()
        self.load.btn_maximize.hide()
        self.load.btn_reduce.show()


    def ReduceWindow(self):
        self.showNormal()
        self.load.btn_reduce.hide()
        self.load.btn_maximize.show()
    
    
