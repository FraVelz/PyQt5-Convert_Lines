# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Convert_lines.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def __style__(self):
        with open('./style.qss', 'r') as f: style = f.read()
        return style
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 410)
        
        Form.setStyleSheet(self.__style__())

        self.fr_fondo = QtWidgets.QFrame(Form)
        self.fr_fondo.setGeometry(QtCore.QRect(20, 10, 561, 381))
        self.fr_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_fondo.setObjectName("fr_fondo")

        self.btn_cont = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_cont.setGeometry(QtCore.QRect(380, 320, 121, 31))
        self.btn_cont.setObjectName("btn_cont")

        self.lbl_autor = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_autor.setGeometry(QtCore.QRect(0, 330, 221, 51))
        self.lbl_autor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_autor.setObjectName("lbl_autor")
        
        self.lbl_titulo = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_titulo.setGeometry(QtCore.QRect(70, 0, 421, 61))
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        
        self.btn_cerrar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_cerrar.setGeometry(QtCore.QRect(520, 20, 21, 23))
        self.btn_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cerrar.setText("")
        self.btn_cerrar.setObjectName("btn_cerrar")

        self.btn_minimizar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_minimizar.setGeometry(QtCore.QRect(20, 20, 21, 23))
        self.btn_minimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimizar.setText("")
        self.btn_minimizar.setObjectName("btn_minimizar")

        self.txte_line = QtWidgets.QLineEdit(self.fr_fondo)
        self.txte_line.setGeometry(QtCore.QRect(70, 270, 431, 31))
        self.txte_line.setText("")
        self.txte_line.setObjectName("txte_line")
        
        self.ptxte_lines = QtWidgets.QPlainTextEdit(self.fr_fondo)
        self.ptxte_lines.setGeometry(QtCore.QRect(70, 80, 430, 170))
        self.ptxte_lines.setObjectName("ptxte_lines")

        self.retranslateUi(Form)

        self.btn_minimizar.clicked.connect(Form.showMinimized)
        self.btn_cerrar.clicked.connect(Form.close)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alarma"))

        self.btn_cont.setText(_translate("Form", "Convertir"))
        self.lbl_autor.setText(_translate("Form", "Author: FraVelz"))
        self.lbl_titulo.setText(_translate("Form", "Convert Lines to One Line"))



if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()

    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

#* Author: FraVelz
