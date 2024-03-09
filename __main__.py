from Ui_ConvertLines import Ui_Form, QtWidgets, QtCore 
import sys

class MainApp(QtWidgets.QMainWindow): 
    
    def __init__(self, parent=None, *args): 
        super(MainApp, self).__init__(parent=parent) 

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.btn_cont.clicked.connect(self.func_convert)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    
        #* Mover ventana
        self.ui.fr_fondo.mouseMoveEvent = self.move_window
	  
    ##* mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def move_window(self, event):
        try:
            if self.isMaximized() == False: 
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()
        except: pass
    
    def func_convert(self):
        text = self.ui.ptxte_lines.toPlainText(
        ).replace('\n', '\\n').replace('"', '\\"')
        
        self.ui.txte_line.setText(u'' + text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    window = MainApp() 
    window.show() 
    sys.exit(app.exec_())

#* Author: Francisco Velez
