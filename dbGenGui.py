# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbGen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DBConnectionGen(object):
    def setupUi(self, DBConnectionGen):
        DBConnectionGen.setObjectName("DBConnectionGen")
        DBConnectionGen.resize(497, 600)
        self.centralwidget = QtWidgets.QWidget(DBConnectionGen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Aero")
        font.setPointSize(22)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.preview_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.preview_text.setGeometry(QtCore.QRect(15, 350, 471, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.preview_text.setFont(font)
        self.preview_text.setObjectName("preview_text")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 69, 321, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(32)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.extention = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.extention.setFont(font)
        self.extention.setObjectName("extention")
        self.extention.addItem("")
        self.extention.addItem("")
        self.gridLayout.addWidget(self.extention, 0, 1, 1, 1)
        self.server = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.server.setFont(font)
        self.server.setObjectName("server")
        self.gridLayout.addWidget(self.server, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 3, 1, 1, 1)
        self.database = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.database.setFont(font)
        self.database.setObjectName("database")
        self.gridLayout.addWidget(self.database, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.generate = QtWidgets.QPushButton(self.layoutWidget)
        self.generate.setFlat(False)
        self.generate.setObjectName("generate")
        self.gridLayout.addWidget(self.generate, 5, 0, 1, 1)
        self.generate.clicked.connect(self.changetext)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 2, 1, 1, 1)
        self.preview = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setObjectName("preview")
        self.gridLayout.addWidget(self.preview, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        DBConnectionGen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DBConnectionGen)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        DBConnectionGen.setStatusBar(self.statusbar)

        self.retranslateUi(DBConnectionGen)
        QtCore.QMetaObject.connectSlotsByName(DBConnectionGen)

    def retranslateUi(self, DBConnectionGen):
        _translate = QtCore.QCoreApplication.translate
        DBConnectionGen.setWindowTitle(_translate("DBConnectionGen", "MainWindow"))
        self.label.setText(_translate("DBConnectionGen", "Database Connection Generator"))
        self.preview_text.setHtml(_translate("DBConnectionGen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.extention.setItemText(0, _translate("DBConnectionGen", ".js"))
        self.extention.setItemText(1, _translate("DBConnectionGen", ".php"))
        self.label_3.setText(_translate("DBConnectionGen", "Username"))
        self.label_6.setText(_translate("DBConnectionGen", "Database"))
        self.label_2.setText(_translate("DBConnectionGen", "Server"))
        self.generate.setText(_translate("DBConnectionGen", "Generate"))
        self.label_5.setText(_translate("DBConnectionGen", "Extention"))
        self.preview.setText(_translate("DBConnectionGen", "Preview"))
        self.label_4.setText(_translate("DBConnectionGen", "Password"))

    def changetext(self):
        self.label.setText('hello')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DBConnectionGen = QtWidgets.QMainWindow()
    ui = Ui_DBConnectionGen()
    ui.setupUi(DBConnectionGen)
    DBConnectionGen.show()
    sys.exit(app.exec_())