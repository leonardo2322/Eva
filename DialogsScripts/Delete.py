from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi 
from PyQt5 import QtGui
from data.conection import DbUser as db
from data.methods import methodsUSER

class DeleteVTable(QDialog):
    def __init__(self,*args, parent = None ): 
        super(DeleteVTable,self).__init__(parent)
        self.load = loadUi('ui/TableDelete.ui',self)
        self.load.show()
        self.id = args[0]
        self.messages = args[1]
        self.db = db()
        self.idDelete = None
        self.tablaDelete = None
################################ icons      #########################################################
        iconBtnClose = QtGui.QIcon()
        iconBtnClose.addPixmap(QtGui.QPixmap("iconos/icons/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_close.setIcon(iconBtnClose)

        iconBtnDelete = QtGui.QIcon()
        iconBtnDelete.addPixmap(QtGui.QPixmap("iconos/icons/borrar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_delete.setIcon(iconBtnDelete)

        iconBtnSearchTables = QtGui.QIcon()
        iconBtnSearchTables.addPixmap(QtGui.QPixmap("iconos/icons/search.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_Search.setIcon(iconBtnSearchTables)

        iconMinimize = QtGui.QIcon()
        iconMinimize.addPixmap(QtGui.QPixmap("iconos/icons/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_minimize.setIcon(iconMinimize)

################################ btn events actions #########################################################
        self.load.btn_minimize.clicked.connect(self.showMinimized)
        self.load.btn_close.clicked.connect(lambda: self.close())
        self.load.Btn_cancel_D.clicked.connect(lambda: self.close())
        
        self.load.btn_Search.clicked.connect( self.ActionSearch)
        self.load.btn_delete.clicked.connect( self.ActionDelete)
################################ btn  #########################################################
    def ActionSearch(self):
        desc = str(self.load.Inp_Desc.text()).strip()

        if desc.__len__() > 0:
                self.tablaDelete = self.load.Cb_TablaSearch.currentText()
                self.db.conection()
                result = self.db.SelectFromDB(name=desc , selection = methodsUSER['ID'],tableSearch = self.tablaDelete)
                print(result)
                if  result == None or result == 'error':
                        self.messages('No se encontro el elemento')
                        self.load.Lbl_RSearch.setText(' No se encontro el elemento que buscas vuelve a intentarlo ')
                else:
                        self.load.Lbl_RSearch.setText(str(result[0]))
                        self.idDelete = int(result[0][0])
        else:
              self.messages('escribe que vas a buscar')

    def ActionDelete(self):
        self.db.conection()
        desc = str(self.load.Inp_Desc.text()).strip()

        if desc.__len__() > 0:
            if self.tablaDelete == 'ingresosdiarios':
                result = self.db.QueryDelete(self.tablaDelete, self.idDelete, 'idIngresos')
                if result == 'success':
                    self.messages('eliminacion Exitosa')
                    self.load.Lbl_RSearch.setText('')
                    self.load.Inp_Desc.setText('')
                else:
                    self.messages('Sucedio algo puede ser que no existe el elemento que deseas eliminar, debes buscar el elemento')
            elif self.tablaDelete == 'gastosdiarios':
                result = self.db.QueryDelete(self.tablaDelete, self.idDelete,'idGastos')
                if result == 'success':
                    self.messages('eliminacion Exitosa')
                    self.load.Lbl_RSearch.setText('')
                    self.load.Inp_Desc.setText('')
                else:
                    self.messages('Sucedio algo puede ser que no existe el elemento que deseas eliminar, debes buscar el elemento')
        else:
             self.messages('Introduce la descripcion y busca el elemento a eliminar')