# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\vardiyasorumlusu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VardiyaSorumlusuMainWindow(object):
    def setupUi(self, VardiyaSorumlusuMainWindow):
        VardiyaSorumlusuMainWindow.setObjectName("VardiyaSorumlusuMainWindow")
        VardiyaSorumlusuMainWindow.resize(500, 504)
        self.centralwidget = QtWidgets.QWidget(VardiyaSorumlusuMainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 480))
        self.centralwidget.setMaximumSize(QtCore.QSize(510, 485))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background: #354152;\n"
"}\n"
"\n"
"QLineEdit{\n"
" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:20px;\n"
"    padding-left:15px;\n"
"    height:42px;\n"
"    border-radius:15px;\n"
"    border-color: #303030;\n"
"    background: transparent;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton#btn_login:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"}\n"
"QCommandLinkButton{\n"
"font-size: 16px;\n"
"background: #4c5d75;\n"
"}\n"
"QCommandLinkButton:pressed{\n"
"    background-color: rgb(92, 186, 138);\n"
"}\n"
"\n"
"\n"
"QCheckBox{\n"
"font-size:16px;;\n"
"color:white;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator{\n"
"    height:15px;\n"
"    width:15px;\n"
"\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:20px;\n"
"    padding-left:15px;\n"
"    height:42px;\n"
"    border-radius:15px;\n"
"    border-color: #303030;\n"
"    background: transparent;\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background: #354152;\n"
"    border: 1px solid gray;\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.text_AdSoyad = QtWidgets.QLineEdit(self.frame)
        self.text_AdSoyad.setEnabled(False)
        self.text_AdSoyad.setGeometry(QtCore.QRect(250, 30, 241, 44))
        self.text_AdSoyad.setObjectName("text_AdSoyad")
        self.text_Vardiyasi = QtWidgets.QLineEdit(self.frame)
        self.text_Vardiyasi.setEnabled(False)
        self.text_Vardiyasi.setGeometry(QtCore.QRect(250, 90, 241, 44))
        self.text_Vardiyasi.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.text_Vardiyasi.setObjectName("text_Vardiyasi")
        self.cmb_Model = QtWidgets.QComboBox(self.frame)
        self.cmb_Model.setGeometry(QtCore.QRect(250, 160, 241, 44))
        self.cmb_Model.setObjectName("cmb_Model")
        self.cmb_Model.addItem("")
        self.cmb_Model.addItem("")
        self.cmb_Model.addItem("")
        self.cmb_Model.addItem("")
        self.cmb_Metrik = QtWidgets.QComboBox(self.frame)
        self.cmb_Metrik.setGeometry(QtCore.QRect(250, 230, 241, 44))
        self.cmb_Metrik.setObjectName("cmb_Metrik")
        self.cmb_Metrik.addItem("")
        self.cmb_Metrik.addItem("")
        self.cmb_Metrik.addItem("")
        self.cmb_Vardiyalar = QtWidgets.QComboBox(self.frame)
        self.cmb_Vardiyalar.setGeometry(QtCore.QRect(12, 326, 471, 44))
        self.cmb_Vardiyalar.setObjectName("cmb_Vardiyalar")
        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(110, 400, 257, 40))
        self.btn_login.setStyleSheet("")
        self.btn_login.setObjectName("btn_login")
        self.image_vardiyaSorumlusu = QtWidgets.QLabel(self.frame)
        self.image_vardiyaSorumlusu.setGeometry(QtCore.QRect(19, 34, 211, 231))
        self.image_vardiyaSorumlusu.setStyleSheet("")
        self.image_vardiyaSorumlusu.setObjectName("image_vardiyaSorumlusu")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        VardiyaSorumlusuMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VardiyaSorumlusuMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menuEkle = QtWidgets.QMenu(self.menubar)
        self.menuEkle.setObjectName("menuEkle")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuExit_2 = QtWidgets.QMenu(self.menubar)
        self.menuExit_2.setObjectName("menuExit_2")
        VardiyaSorumlusuMainWindow.setMenuBar(self.menubar)
        self.action_VardiyaEkle = QtWidgets.QAction(VardiyaSorumlusuMainWindow)
        self.action_VardiyaEkle.setObjectName("action_VardiyaEkle")
        self.action_isciDuzenle = QtWidgets.QAction(VardiyaSorumlusuMainWindow)
        self.action_isciDuzenle.setObjectName("action_isciDuzenle")
        self.action_isciEkle = QtWidgets.QAction(VardiyaSorumlusuMainWindow)
        self.action_isciEkle.setObjectName("action_isciEkle")
        self.action_VardiyayaisciEkle = QtWidgets.QAction(VardiyaSorumlusuMainWindow)
        self.action_VardiyayaisciEkle.setObjectName("action_VardiyayaisciEkle")
        self.action_vardiyasorumlusuDuzenle = QtWidgets.QAction(VardiyaSorumlusuMainWindow)
        self.action_vardiyasorumlusuDuzenle.setObjectName("action_vardiyasorumlusuDuzenle")
        self.actionExit_2 = QtWidgets.QAction(VardiyaSorumlusuMainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit = QtWidgets.QAction(VardiyaSorumlusuMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_SayfayiYenile = QtWidgets.QAction(VardiyaSorumlusuMainWindow)
        self.action_SayfayiYenile.setObjectName("action_SayfayiYenile")
        self.menuEkle.addAction(self.action_VardiyaEkle)
        self.menuEkle.addAction(self.action_isciEkle)
        self.menuEkle.addAction(self.action_VardiyayaisciEkle)
        self.menuExit.addAction(self.action_isciDuzenle)
        self.menuExit.addAction(self.action_vardiyasorumlusuDuzenle)
        self.menuExit.addAction(self.action_SayfayiYenile)
        self.menuExit_2.addAction(self.actionExit)
        self.menubar.addAction(self.menuEkle.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuExit_2.menuAction())

        self.retranslateUi(VardiyaSorumlusuMainWindow)
        QtCore.QMetaObject.connectSlotsByName(VardiyaSorumlusuMainWindow)

    def retranslateUi(self, VardiyaSorumlusuMainWindow):
        _translate = QtCore.QCoreApplication.translate
        VardiyaSorumlusuMainWindow.setWindowTitle(_translate("VardiyaSorumlusuMainWindow", "MainWindow"))
        self.text_AdSoyad.setPlaceholderText(_translate("VardiyaSorumlusuMainWindow", "Adı ve Soyadı"))
        self.text_Vardiyasi.setPlaceholderText(_translate("VardiyaSorumlusuMainWindow", "Vardiyası"))
        self.cmb_Model.setItemText(0, _translate("VardiyaSorumlusuMainWindow", "VGG-Face"))
        self.cmb_Model.setItemText(1, _translate("VardiyaSorumlusuMainWindow", "OpenFace"))
        self.cmb_Model.setItemText(2, _translate("VardiyaSorumlusuMainWindow", "Facenet"))
        self.cmb_Model.setItemText(3, _translate("VardiyaSorumlusuMainWindow", "DeepFace"))
        self.cmb_Metrik.setItemText(0, _translate("VardiyaSorumlusuMainWindow", "cosine"))
        self.cmb_Metrik.setItemText(1, _translate("VardiyaSorumlusuMainWindow", "euclidean"))
        self.cmb_Metrik.setItemText(2, _translate("VardiyaSorumlusuMainWindow", "euclidean_l2"))
        self.btn_login.setText(_translate("VardiyaSorumlusuMainWindow", "Vardiyayı YÜKLE"))
        self.image_vardiyaSorumlusu.setText(_translate("VardiyaSorumlusuMainWindow", "TextLabel"))
        self.menuEkle.setTitle(_translate("VardiyaSorumlusuMainWindow", "Ekle"))
        self.menuExit.setTitle(_translate("VardiyaSorumlusuMainWindow", "Düzenle"))
        self.menuExit_2.setTitle(_translate("VardiyaSorumlusuMainWindow", "Exit"))
        self.action_VardiyaEkle.setText(_translate("VardiyaSorumlusuMainWindow", "Ders Ekle"))
        self.action_isciDuzenle.setText(_translate("VardiyaSorumlusuMainWindow", "Öğrenci Düzenle"))
        self.action_isciEkle.setText(_translate("VardiyaSorumlusuMainWindow", "Öğrenci Ekle"))
        self.action_VardiyayaisciEkle.setText(_translate("VardiyaSorumlusuMainWindow", "Öğrenciyi Derse Ekle"))
        self.action_vardiyasorumlusuDuzenle.setText(_translate("VardiyaSorumlusuMainWindow", "Öğretmen Düzenle"))
        self.actionExit_2.setText(_translate("VardiyaSorumlusuMainWindow", "Exit"))
        self.actionExit.setText(_translate("VardiyaSorumlusuMainWindow", "Exit"))
        self.action_SayfayiYenile.setText(_translate("VardiyaSorumlusuMainWindow", "Sayfayı Yenile"))