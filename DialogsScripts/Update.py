from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi 
from PyQt5 import QtGui,QtCore
from data.conection import DbUser as db
from data.methods import methodsUSER,recogDate
class UpdateTable(QDialog):
    def __init__(self,*args, parent = None ): 
        super(UpdateTable,self).__init__(parent)
        self.load = loadUi('ui/EditTable.ui',self)
        self.load.show()
        self.id = args[0]
        self.messages = args[1]
        self.ReduceWindow = args[2]
        self.btnExpandWindow = args[3]
        self.IDEdit = None
        self.table = None
        self.db = db()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
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

        self.load.BtnEditSearch.clicked.connect(self.SearchID)
        self.load.BtnEditSave.clicked.connect(self.UpdateData)
################################ Functions #########################################################
    def UpdateData(self):
        if len(self.load.InpEditFecha.text()) > 0 and len(self.load.InpEditTipodepago.text()) > 0 and len(self.load.InpEditCategoria.text()) >0 and len(self.load.InpEditDivisa.text()) and len(self.load.InpEditValor.text()) > 0 and len(self.load.InpEditDescripcion.text()) > 0 and self.IDEdit is not None:
                data = [self.load.InpEditFecha.text(),self.load.InpEditTipodepago.text(),self.load.InpEditCategoria.text(),self.load.InpEditDivisa.text(),int(self.load.InpEditValor.text()),self.load.InpEditDescripcion.text()] 
                if self.table == 'ingresosdiarios':
                      result = self.db.QueryUpdate( self.IDEdit,self.table,'idingresos', data=data)
                      if result == 'ok':
                            self.messages('actualizacion exitosa')
                      else:
                            self.messages('ocurrio un error')
                elif self.table == 'gastosdiarios':
                      result = self.db.QueryUpdate( self.IDEdit,self.table,'idgastos', data=data)
                      if result == 'ok':
                            self.messages('actualizacion exitosa')
                      else:
                            self.messages('ocurrio un error')
        else:
              self.messages('busca el elemento a editar')


    def SearchID(self):
        id = self.load.Inp_edit_ID.text()
        tabla = self.load.Cb_Desc_search.currentText()
        if len(id) > 0:
                if tabla == 'ingresosdiarios':
                        result = self.db.SelectFromDB(selection=methodsUSER['search'], SelectTable=tabla, ID=id,**{'ide':'idingresos'} )
                elif tabla == 'gastosdiarios':
                        result = self.db.SelectFromDB(selection=methodsUSER['search'], SelectTable=tabla, ID=id,**{'ide':'idgastos'} )
                self.IDEdit = result[0]
                self.table = tabla
                fecha = str(result[1])
                self.load.InpEditFecha.setText(fecha)
                self.load.InpEditTipodepago.setText(result[2])
                self.load.InpEditCategoria.setText(result[3])
                self.load.InpEditDivisa.setText(result[4])
                self.load.InpEditValor.setText(str(result[5]))
                self.load.InpEditDescripcion.setText(result[6])
        else:
             self.messages('indtroduce un id para proceder con la busqueda')