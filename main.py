import sys
from PyQt5.QtWidgets import (QApplication,
        QMainWindow, QSizeGrip,
        QHeaderView,QMessageBox, 
        QAbstractItemView, QTableWidgetItem)
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve, Qt
from PyQt5 import QtGui
from PyQt5.uic import loadUi 
import re
from data.dbManage import DbUser
import datetime
class Eva(QMainWindow):
    def __init__(self):
        super(Eva,self).__init__()

        self.db = DbUser()
        self.patron = '[a-zA-Z]+'
        self.patronNum = '[1-9]+[0-9]*'
        self.regex = re

        self.load = loadUi('ui/EvaSystem.ui',self)
############################## hide Buttons ###########################################    
        self.load.btn_reduce.hide()
        self.load.btn_menu.hide()
#################   Deberia Funcionar en windows   ########################################
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
#####################    botones de cerrar minimizar y expandir   ###########################
        iconClose = QtGui.QIcon()
        iconClose.addPixmap(QtGui.QPixmap("iconos/icons/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_close.setIcon(iconClose)

        self.load.btn_close.clicked.connect(lambda:self.close())
        self.load.btn_expand.clicked.connect(self.btnExpandWindow)
        self.load.minimize.clicked.connect(self.btnMinimizeWindow)
        self.load.btn_reduce.clicked.connect(self.ReduceWindow)
        self.load.btn_menu.clicked.connect(self.MenuHideAndShow)
        self.load.slide_close_btn.clicked.connect(self.MenuHideAndShow)
        self.load.show()
        
################################   Buttoms Event    ###################################

        self.load.btn_costosygastos.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.stk_CostosGastos))
        
        self.load.btn_show_home.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.homeStkInventary))

        self.load.btn_busisness.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.stk_busisness))


        self.load.btn_clientes.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.stk_Clientes))

        self.load.btn_proveedor.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.stk_Proveedores))

        self.load.btn_domicilios.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.Domicilios_stk))

        self.load.btn_delete_cyg.clicked.connect(self.DeleteDb)
        self.load.btn_insert_data_in_cyg.clicked.connect(self.dbQueryesInsert)
        self.load.cbb_data_table_products.currentIndexChanged.connect(self.TableEvents)
########################  icons    #########################################################
        iconExpand = QtGui.QIcon()
        iconExpand.addPixmap(QtGui.QPixmap("iconos/icons/maximize.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_expand.setIcon(iconExpand)

        iconMinimize = QtGui.QIcon()
        iconMinimize.addPixmap(QtGui.QPixmap("iconos/icons/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.minimize.setIcon(iconMinimize)

        iconReduce = QtGui.QIcon()
        iconReduce.addPixmap(QtGui.QPixmap("iconos/icons/minimize-2.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_reduce.setIcon(iconReduce)

        iconPaper = QtGui.QIcon()
        iconPaper.addPixmap(QtGui.QPixmap("iconos/remove_paper.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.Img_Paper.setIcon(iconPaper)

        iconMenuArrow = QtGui.QIcon()
        iconMenuArrow.addPixmap(QtGui.QPixmap("iconos/icons/chevron-left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.slide_close_btn.setIcon(iconMenuArrow)

        iconMenubars = QtGui.QIcon()
        iconMenubars.addPixmap(QtGui.QPixmap("iconos/icons/menu.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_menu.setIcon(iconMenubars)

        iconEvaAction = QtGui.QIcon()
        iconEvaAction.addPixmap(QtGui.QPixmap("iconos/inteligencia-artificial.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.eva_system_activated.setIcon(iconEvaAction)

        iconBtnHome = QtGui.QIcon()
        iconBtnHome.addPixmap(QtGui.QPixmap("iconos/icons/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_show_home.setIcon(iconBtnHome)

        self.load.lbl_user_text.setPixmap(QtGui.QPixmap("iconos/icons/user.svg"))

        iconCostosygastos = QtGui.QIcon()
        iconCostosygastos.addPixmap(QtGui.QPixmap("iconos/presupuesto.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_costosygastos.setIcon(iconCostosygastos)

        iconClientes = QtGui.QIcon()
        iconClientes.addPixmap(QtGui.QPixmap("iconos/Clientes.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_clientes.setIcon(iconClientes)

        iconProveedores = QtGui.QIcon()
        iconProveedores.addPixmap(QtGui.QPixmap("iconos/proveedor.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_proveedor.setIcon(iconProveedores)

        iconDomicilios = QtGui.QIcon()
        iconDomicilios.addPixmap(QtGui.QPixmap("iconos/repartidor.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_domicilios.setIcon(iconDomicilios)

        icontoolbox = QtGui.QIcon()
        icontoolbox.addPixmap(QtGui.QPixmap("iconos/icons/chevron-down.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.toolBox.setItemIcon(0,icontoolbox)
        self.load.toolBox.setItemIcon(1,icontoolbox)
        self.load.toolBox.setItemIcon(2,icontoolbox)
        self.load.toolBox.setItemIcon(3,icontoolbox)

        iconBtnAdd = QtGui.QIcon()
        iconBtnAdd.addPixmap(QtGui.QPixmap("iconos/icons/user-plus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_user_add.setIcon(iconBtnAdd)

        iconBtnDelete = QtGui.QIcon()
        iconBtnDelete.addPixmap(QtGui.QPixmap("iconos/icons/user-x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_user_delete.setIcon(iconBtnDelete)

        iconBtnEdit = QtGui.QIcon()
        iconBtnEdit.addPixmap(QtGui.QPixmap("iconos/icons/users.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_user_edit.setIcon(iconBtnEdit)

        
        iconBtnRestaurant = QtGui.QIcon()
        iconBtnRestaurant.addPixmap(QtGui.QPixmap("iconos/utensilios-de-restaurante.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_restaurant.setIcon(iconBtnRestaurant)

        iconBtnstores = QtGui.QIcon()
        iconBtnstores.addPixmap(QtGui.QPixmap("iconos/grow-shop.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_store.setIcon(iconBtnstores)

        iconBtnFastFood = QtGui.QIcon()
        iconBtnFastFood.addPixmap(QtGui.QPixmap("iconos/comida.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_fast_food.setIcon(iconBtnFastFood)

        iconBtnbusiness = QtGui.QIcon()
        iconBtnbusiness.addPixmap(QtGui.QPixmap("iconos/negocios.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_business.setIcon(iconBtnbusiness)
        
        iconBtnSearchCostos = QtGui.QIcon()
        iconBtnSearchCostos.addPixmap(QtGui.QPixmap("iconos/icons/search.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_search_in_costos.setIcon(iconBtnSearchCostos)

        iconBtnbusisness = QtGui.QIcon()
        iconBtnbusisness.addPixmap(QtGui.QPixmap("iconos/negocios.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_busisness.setIcon(iconBtnbusisness)


        self.load.btn_search_proveedores.setIcon(iconBtnSearchCostos)

############ Tables Strectchs ##########################3

        self.load.table_proveedor.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.load.Table_inventary_home.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.load.tbl_data_products.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        

##### table #####################


        

    def TableEvents(self):
        db = self.db.SelectFromDB()
        listData = []
        for Dts in db:
            listData.append(Dts)

        self.load.tbl_data_products.setSelectionBehavior(QAbstractItemView.SelectRows)    
        self.load.tbl_data_products.clearContents()
        self.load.tbl_data_products.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.load.tbl_data_products.setSelectionMode(QAbstractItemView.SingleSelection)
        self.load.tbl_data_products.setTextElideMode(Qt.ElideRight)

        self.load.tbl_data_products.resizeColumnsToContents()
        currentIndex = self.load.cbb_data_table_products.currentIndex()
        try:
            if db:
                if currentIndex == 0:
                    self.arr = []
                    for data in (db[0]):
                        self.arr.append(data)
                    for dat in self.arr:
                        idDato = QTableWidgetItem(str(self.arr[0]))
                        idDato.setTextAlignment(Qt.AlignCenter)
                        self.load.tbl_data_products.setItem(0,0,idDato)
                        self.load.tbl_data_products.setItem(0,1,QTableWidgetItem(self.arr[1]))
                        self.load.tbl_data_products.setItem(0,2,QTableWidgetItem(self.arr[2]))
                        self.load.tbl_data_products.setItem(0,3,QTableWidgetItem(str(self.arr[3])))
                elif currentIndex == 1:
                    fetchlastOne = []
                    for d in (db[-1]):
                        fetchlastOne.append(d)
                    for dtb in fetchlastOne:
                        
                        idD= QTableWidgetItem(str(fetchlastOne[0])) 
                        self.load.tbl_data_products.setItem(0,0,idD)
                        self.load.tbl_data_products.setItem(0,1,QTableWidgetItem(fetchlastOne[1]))
                        self.load.tbl_data_products.setItem(0,2,QTableWidgetItem(fetchlastOne[2]))
                        self.load.tbl_data_products.setItem(0,3,QTableWidgetItem(str(fetchlastOne[3])))
                elif currentIndex == 2:
                    fila = 0
                    for datos in db:
                        self.load.tbl_data_products.setRowCount(fila + 1)
                        
                        idDato = QTableWidgetItem(str(datos[0]))
                        idDato.setTextAlignment(Qt.AlignCenter)

                        self.load.tbl_data_products.setItem(fila, 0, idDato)
                        self.load.tbl_data_products.setItem(fila, 1, QTableWidgetItem(datos[1]))
                        self.load.tbl_data_products.setItem(fila, 2, QTableWidgetItem(datos[2]))
                        self.load.tbl_data_products.setItem(fila, 3, QTableWidgetItem(str(datos[3])))
                        fila += 1
                else:
                    self.mensagges('ocurrio un error')
            else:
                self.mensagges('no se pudo conectar a la base de datos')
        except:
            self.mensagges('ocurrio un error')
#################  functions section  ##############################

    def mensagges(self, mensajeInf):
        self.msj = QMessageBox()
        self.msj.setWindowTitle('Informacio Del sistema')
        self.msj.setText(mensajeInf)
        self.msj.setIcon(QMessageBox.Information)
        self.msj.exec_()

    def MenuHideAndShow(self):
        if True:
            widt = self.load.Slide_bar.width()
            normal = 0
            extender = 300
            if widt == 0:
                self.load.slide_close_btn.show()
                self.load.btn_menu.hide()
            else:
                
                self.load.slide_close_btn.hide()
                self.load.btn_menu.show()
                extender = normal
            self.animation = QPropertyAnimation(self.load.Slide_bar,b'maximumWidth')
            self.animation.setStartValue(widt)
            self.animation.setEndValue(extender)
            self.animation.setDuration(500)
            self.animation.setEasingCurve(QEasingCurve.InCubic)
            self.animation.start()

    
        
    def ReduceWindow(self):
        self.showNormal()
        self.load.btn_reduce.hide()
        self.load.btn_expand.show()

    def btnMinimizeWindow(self):
        self.showMinimized()

    def btnExpandWindow(self):
        self.showMaximized()
        self.load.btn_expand.hide()
        self.load.btn_reduce.show()

    def dbQueryesInsert(self):
        
        patronResult = self.regex.compile(self.patron)
        patronNum = self.regex.compile(self.patronNum)


        try:
            valorProducto = self.load.productoLineEdit.text().strip()
            valorProveedor = self.load.proveedorLineEdit.text().strip()   
            valorCosto = int(self.load.costoLineEdit.text().strip())

            if  patronResult.match(self.load.productoLineEdit.text().strip()) is not None:
                if patronResult.match(self.load.proveedorLineEdit.text().strip()) is not None:
                    if patronNum.match(self.load.costoLineEdit.text().strip()) is not None:
                        self.mensagges('los datos han sido instertados')               
                        self.db.QueryInsert(valorProducto, valorProveedor, valorCosto)
                                            
                
                    else:
                        self.mensagges('tiene que insertar numeros sin comas solo digite numeros')
                
                else:
                    self.mensagges('Solo puede insertar cadena de caracteres sin ningun caracter especial')
            
            else:
                self.mensagges('Solo puede insertar cadena de caracteres sin ningun caracter especial')
        except TypeError as e:
            
            return self.mensagges('ocurrio un error inesperado')
        except TimeoutError:
            return self.mensagges('es otro tipo de error')
        except:
            return self.mensagges('Error debe introducir datos en los 3 campos')

        self.load.proveedorLineEdit.setText('')
        self.load.productoLineEdit.setText('')
        self.load.costoLineEdit.setText('')

        
        
    def DeleteDb(self):
        idcyg = self.load.lnEdit_ID_Delete_Cyg.text()

        self.db.QueryDelete(idcyg)       

        self.mensagges('Elemento borrado')

if __name__=="__main__":
    app = QApplication(sys.argv)

    ventana= Eva()
    ventana.show()

    sys.exit(app.exec_())