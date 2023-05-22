from PyQt5.QtWidgets import  QMainWindow, QSizeGrip, QMessageBox,QTableWidgetItem
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import QtGui,QtCore
from PyQt5.uic import loadUi 
from DialogsScripts.QinsertGastoIngresos import Dialog
from datetime import datetime
from DialogsScripts.Update import UpdateTable
from DialogsScripts.Delete import DeleteVTable
from DialogsScripts.userAdd import WindowUserAdd
from data.conection import DbUser as db
from data.methods import methodsUSER 
class Eva(QMainWindow):
    def __init__(self,*args, parent = None):
        super(Eva,self).__init__(parent)
        self.load = loadUi('ui/EvaSystem.ui',self)
        self.id = args[0]
        horaYfecha =  str(datetime.now().ctime()) 
        self.load.fecha_visualized.setText(horaYfecha)
        self.load.user_lbl.setText(str(args[1]).capitalize())
        self.db = db()
        self.load.stackedWidget.setCurrentWidget(self.load.stk_Ingresos)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.Frame_Superior.mouseMoveEvent = self.MoveWindow
############################## hide Buttons ###########################################    
        self.load.btn_reduce.hide()
        self.load.btn_menu.hide()
#################   Deberia Funcionar en windows   ########################################
        self.gripSize = 5
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
#####################    botones de cerrar minimizar y expandir   ###########################
        iconClose = QtGui.QIcon()
        iconClose.addPixmap(QtGui.QPixmap("iconos/icons/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_close.setIcon(iconClose)

        self.load.btn_close.clicked.connect(lambda:self.close())
        self.load.btn_expand.clicked.connect(lambda:self.btnExpandWindow(self,self.load.btn_expand,self.load.btn_reduce))
        self.load.minimize.clicked.connect(self.showMinimized)
        self.load.btn_reduce.clicked.connect(lambda: self.ReduceWindow(self,self.load.btn_expand ,self.load.btn_reduce))
        self.load.btn_menu.clicked.connect(self.MenuHideAndShow)
        self.load.slide_close_btn.clicked.connect(self.MenuHideAndShow)
        self.load.show()
        
################################   Buttoms Event    ###################################
        self.load.btn_insert.clicked.connect(lambda: self.EjecutionDialog(Dialog))
        self.load.btn_update.clicked.connect(lambda: self.EjecutionDialog(UpdateTable))
        self.load.btn_delete.clicked.connect(lambda: self.EjecutionDialog(DeleteVTable))
        self.load.btn_user_add.clicked.connect(lambda: self.EjecutionDialog(WindowUserAdd))
################################   Buttoms ingresos stk    ###################################
        self.load.Ingresosbtn_stk_ing.clicked.connect(lambda:self.Tables(self.load.Tabla_Ingresos,8,'ingresosdiarios',names=['ID','Fecha','T_de_pago','Categoria', 'Divisa', 'Valor','Descripcion','Usuario']))

        self.load.gastosbtn_stk_ing.clicked.connect(lambda:self.Tables(self.load.Tabla_gastos,8,'gastosdiarios',names=['ID','Fecha','T_de_pago','Categoria', 'Divisa', 'Valor','Descripcion','Usuario']))

        self.load.balancebtn_stk_ing.clicked.connect(self.Balance)
################################   Buttoms gastos stk    ###################################
        self.load.ingresobtn_stk_gas.clicked.connect(lambda: self.Tables(self.load.Tabla_Ingresos,8,'ingresosdiarios',names=['ID','Fecha','T_de_pago','Categoria', 'Divisa', 'Valor','Descripcion','Usuario']))

        self.load.balancebtn_stk_gas.clicked.connect(self.Balance)

        self.load.gastosbtn_stk_gas.clicked.connect(lambda:self.Tables(self.load.Tabla_gastos,8,'gastosdiarios',names=['ID','Fecha','T_de_pago','Categoria', 'Divisa', 'Valor','Descripcion','Usuario']))
################################   Buttoms balance stk    ###################################  
        self.load.balancebtn_stk_bal.clicked.connect(self.Balance)

        self.load.gastosbtn_stk_bal.clicked.connect(lambda:self.Tables(self.load.Tabla_gastos,8,'gastosdiarios',names=['ID','Fecha','T_de_pago','Categoria', 'Divisa', 'Valor','Descripcion','Usuario']))
        
        self.load.Ingresosbtn_stk_bal.clicked.connect(lambda: self.Tables(self.load.Tabla_Ingresos,8,'ingresosdiarios',names=['ID','Fecha','T_de_pago','Categoria', 'Divisa', 'Valor','Descripcion','Usuario']))
        # self.load.btn_costosygastos.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.stk_CostosGastos))
        
        # self.load.btn_show_home.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.homeStkInventary))

        # # self.load.btn_busisness.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.stk_busisness))


        # # self.load.btn_clientes.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.stk_Clientes))

        # self.load.btn_proveedor.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.stk_Proveedores))

        # self.load.btn_domicilios.clicked.connect(lambda:self.load.stackedWidget.setCurrentWidget(self.load.Domicilios_stk))

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
        iconBtnHome.addPixmap(QtGui.QPixmap("iconos/icons/editar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load.btn_insert.setIcon(iconBtnHome)

        self.load.lbl_user_text.setPixmap(QtGui.QPixmap("iconos/icons/user.svg"))

        iconBtnUpdate = QtGui.QIcon()
        iconBtnUpdate.addPixmap(QtGui.QPixmap("iconos/icons/actualizar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_update.setIcon(iconBtnUpdate)

        iconBtnDelete = QtGui.QIcon()
        iconBtnDelete.addPixmap(QtGui.QPixmap("iconos/icons/borrar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        
        self.load.btn_delete.setIcon(iconBtnDelete)


        iconBtntodo = QtGui.QIcon()
        iconBtntodo.addPixmap(QtGui.QPixmap("iconos/icons/lista.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_todo.setIcon(iconBtntodo)

        iconBtnTrans = QtGui.QIcon()
        iconBtnTrans.addPixmap(QtGui.QPixmap("iconos/icons/trans.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_trans.setIcon(iconBtnTrans)

        iconBtnEstadistics = QtGui.QIcon()
        iconBtnEstadistics.addPixmap(QtGui.QPixmap("iconos/icons/estadisticas.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_estadistics.setIcon(iconBtnEstadistics)

        iconBtnAddUser = QtGui.QIcon()
        iconBtnAddUser.addPixmap(QtGui.QPixmap("iconos/icons/plus-circle.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_user_add.setIcon(iconBtnAddUser)

        iconBtnAddEdit = QtGui.QIcon()
        iconBtnAddEdit.addPixmap(QtGui.QPixmap("iconos/icons/edit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_user_edit.setIcon(iconBtnAddEdit)

        iconBtnAddDelete = QtGui.QIcon()
        iconBtnAddDelete.addPixmap(QtGui.QPixmap("iconos/icons/trash-2.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_user_delete.setIcon(iconBtnAddDelete)

        iconBtnLeft = QtGui.QIcon()
        iconBtnLeft.addPixmap(QtGui.QPixmap("iconos/icons/chevron-left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_left.setIcon(iconBtnLeft)
        
        iconBtnright = QtGui.QIcon()
        iconBtnright.addPixmap(QtGui.QPixmap("iconos/icons/chevron-right.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_right.setIcon(iconBtnright)
        
        iconBtnSearchTables = QtGui.QIcon()
        iconBtnSearchTables.addPixmap(QtGui.QPixmap("iconos/icons/search.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.btn_search_tables.setIcon(iconBtnSearchTables)
     

        icontoolbox = QtGui.QIcon()
        icontoolbox.addPixmap(QtGui.QPixmap("iconos/icons/chevron-down.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.load.toolBox.setItemIcon(0,icontoolbox)
        self.load.toolBox.setItemIcon(1,icontoolbox)
        # self.load.toolBox.setItemIcon(2,icontoolbox)
        
       

        
       



############ Tables Strectchs ##########################3

        # self.load.table_proveedor.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.load.Tabla_Ingresos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.load.Table_inventary_home.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)











#################  functions section  ##############################

    def MoveWindow(self, event):
        if self.isMaximized() == False and event.buttons() ==QtCore.Qt.LeftButton:
            self.move(self.pos()+ event.globalPos() - self.clickPosition)

    def Balance(self):
        self.load.stackedWidget.setCurrentWidget(self.load.stk_Balance)
        
        self.db.conection()
        data = self.db.SelectFromDB( selection='balance', SelectTable='DetallesIngGastos', ID='idDetailIngGasto')
        if data[2] > 0:
            self.load.IngresosQuantity.setStyleSheet("color: #008000; font-size:24px")
        else:
            self.load.IngresosQuantity.setStyleSheet("color: #ff0000; font-size:24px")
        self.load.GastosQuantity.setStyleSheet("color: #ff0000; font-size:24px")

        if data[3] > 0:
            self.load.BalanceQuantity.setStyleSheet("color: #008000; font-size:24px")
        else:
            self.load.BalanceQuantity.setStyleSheet("color: #ff0000; font-size:24px")

        self.load.IngresosQuantity.setText(str(data[2]))
        self.load.GastosQuantity.setText(str(data[1]))
        self.load.BalanceQuantity.setText(str(data[3]))

        if data[2] > data[1]:
            self.load.ComoVas.setStyleSheet('color: #008000; font-size:24px')
            self.load.ComoVas.setText('Vas bien sigue asi')
        else:
            self.load.ComoVas.setStyleSheet("color: #ff0000; font-size:24px")
            self.load.ComoVas.setText('Revisa Tus Gastos algo no pinta Muy bien')
        
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

    def EjecutionDialog(self,dialog):
        dialogo = dialog(self.id,self.mensagges,self.ReduceWindow, self.btnExpandWindow)
        dialogo.exec_()


    def ReduceWindow(self,window, btnExpand, btnReduce):
        window.showNormal()
        btnReduce.hide()
        btnExpand.show()



    def btnExpandWindow(self,window, btnExpand, btnReduce):
        window.showMaximized()
        btnExpand.hide()
        btnReduce.show()

        
    def mensagges(self, mensajeInf):
        self.msj = QMessageBox()
        self.msj.setWindowTitle('Informacion Del sistema')
        self.msj.setText(mensajeInf)
        self.msj.setIcon(QMessageBox.Information)
        self.msj.exec_()


    def Tables(self,tabla,columns,tableselect,names=None):
        if tableselect == 'gastosdiarios':
            self.load.stackedWidget.setCurrentWidget(self.load.stk_Gastos)
        elif tableselect == 'ingresosdiarios':
            self.load.stackedWidget.setCurrentWidget(self.load.stk_Ingresos)
        else:
            self.load.stackedWidget.setCurrentWidget(self.load.stk_Balance)

        self.db.conection()
        self.data = self.db.SelectFromDB( selection = methodsUSER['ing']['ing'], SelectTable=tableselect,names=names)
      
        try:
            stylesheet = "::section{Background-color:rgb(24,24,36)}"
            tabla.horizontalHeader().setStyleSheet(stylesheet)
            tabla.verticalHeader().setStyleSheet(stylesheet)
            tabla.setColumnCount(columns)
            for rang in range(0,columns):
                tabla.setColumnWidth(rang,100)
            tabla.setHorizontalHeaderLabels(self.data[0].keys())
            tabla.setRowCount(len(self.data))
            name = names
            row = 0 
            
            for e in self.data:
                for i in range(0,len(e)):
                    tabla.setItem(row, i, QTableWidgetItem(str(e[name[i]])))
                row +=1

        except Exception as e:
            self.mensagges('No deben de haber datos en base de datos verifica y intentalo nuevamente')