import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi 

class Eva(QMainWindow):
    def __init__(self):
        super(Eva,self).__init__()
        self.load = loadUi('ui/EvaSystem.ui',self)
##############################hide Buttons#############################################33        
        self.load.btn_reduce.hide()
        self.load.slide_close_btn.hide()
#################Deberia Funcionar en windows############################################3
        # self.gripSize = 10
        # self.grip = QSizeGrip(self)
        # self.grip.resize(self.gripSize, self.gripSize)
#####################botones de cerrar minimizar y expandir############################3
        self.load.btn_close.clicked.connect(lambda:self.close())
        self.load.btn_expand.clicked.connect(self.btnExpandWindow)
        self.load.minimize.clicked.connect(self.btnMinimizeWindow)
        self.load.btn_reduce.clicked.connect(self.ReduceWindow)
        self.load.btn_menu.clicked.connect(self.MenuHideAndShow)
        self.load.slide_close_btn.clicked.connect(self.MenuHideAndShow)
        self.load.show()
        
    def MenuHideAndShow(self):
        if True:
            widt = self.load.Slide_bar.width()
            normal = 0
            extender = 300
            if widt == 0:
                self.load.slide_close_btn.hide()
                self.load.btn_menu.show()
            else:
                
                self.load.slide_close_btn.show()
                self.load.btn_menu.hide()
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
if __name__=="__main__":
    app = QApplication(sys.argv)

    ventana= Eva()
    ventana.show()

    sys.exit(app.exec_())