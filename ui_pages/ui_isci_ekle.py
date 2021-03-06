# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\IsciEkle.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Isci_ekleWindow(object):
    def setupUi(self, Isci_ekleWindow):
        Isci_ekleWindow.setObjectName("Isci_ekleWindow")
        Isci_ekleWindow.resize(542, 873)
        Isci_ekleWindow.setStyleSheet("")
        self.ana_widget = QtWidgets.QWidget(Isci_ekleWindow)
        self.ana_widget.setObjectName("ana_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.ana_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.ana_widget)
        self.frame.setStyleSheet("QFrame{\n"
"background: #354152;\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size:24px;\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"padding-left: 15px;\n"
"font-size:16px;\n"
"\n"
"}\n"
"QPushButton{\n"
"height:32px;\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:16px;\n"
"    padding-left:15px;\n"
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
"    background: white;\n"
"    border: 1px solid gray;\n"
"    box-shadow: transparent;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"QSpinBox{\n"
"height:42px;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    /*text-align: center;*/\n"
"    padding-right: 15px;\n"
"    border-width: 5px;\n"
"    border-radius:10px;\n"
"    padding-left:15px;\n"
"    font-size:20px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"     subcontrol-origin: border;\n"
"     padding-left: 10px;\n"
"     padding-right: 40px;\n"
"     width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"     /*height: 14px;*/\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"     background-color: #eeeeee;\n"
"\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"    height:42px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #bbbb;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, QSpinBox::down-arrow:disabled {\n"
"    image: none;\n"
"}\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"     border: 1px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"padding-left:20px;\n"
"    image: url(:/resimler/icons/chevron-up.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-position: bottom left; /* position at bottom right corner */\n"
"    height:42px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"image: url(:/resimler/icons/chevron-down.png);\n"
"padding-left:20px;\n"
"}\n"
"\n"
"QGroupBox{\n"
"border: none;\n"
"}\n"
"\n"
"QToolButton{\n"
"margin-left:10px;\n"
"height:42px;\n"
"width:500px;\n"
" border-width: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setStyleSheet("QLineEdit{\n"
"height:42px;\n"
"}\n"
"QComboBox{\n"
"height:42px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)
        self.cmb_Vardiyas = QtWidgets.QComboBox(self.groupBox)
        self.cmb_Vardiyas.setObjectName("cmb_Vardiyas")
        self.cmb_Vardiyas.addItem("")
        self.cmb_Vardiyas.addItem("")
        self.cmb_Vardiyas.addItem("")
        self.gridLayout_2.addWidget(self.cmb_Vardiyas, 5, 2, 1, 1)
        self.txt_Soyadi = QtWidgets.QLineEdit(self.groupBox)
        self.txt_Soyadi.setText("")
        self.txt_Soyadi.setObjectName("txt_Soyadi")
        self.gridLayout_2.addWidget(self.txt_Soyadi, 4, 2, 1, 1)
        self.btn_kayit = QtWidgets.QPushButton(self.groupBox)
        self.btn_kayit.setObjectName("btn_kayit")
        self.gridLayout_2.addWidget(self.btn_kayit, 8, 0, 1, 3)
        self.txt_Adi = QtWidgets.QLineEdit(self.groupBox)
        self.txt_Adi.setText("")
        self.txt_Adi.setObjectName("txt_Adi")
        self.gridLayout_2.addWidget(self.txt_Adi, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.txt_TcNo = QtWidgets.QLineEdit(self.groupBox)
        self.txt_TcNo.setText("")
        self.txt_TcNo.setMaxLength(11)
        self.txt_TcNo.setObjectName("txt_TcNo")
        self.gridLayout_2.addWidget(self.txt_TcNo, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.btn_resimCek = QtWidgets.QToolButton(self.frame)
        self.btn_resimCek.setObjectName("btn_resimCek")
        self.gridLayout_3.addWidget(self.btn_resimCek, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        Isci_ekleWindow.setCentralWidget(self.ana_widget)
        self.menubar = QtWidgets.QMenuBar(Isci_ekleWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        Isci_ekleWindow.setMenuBar(self.menubar)
        self.actionStart_Camera = QtWidgets.QAction(Isci_ekleWindow)
        self.actionStart_Camera.setObjectName("actionStart_Camera")
        self.actionStop_Camera = QtWidgets.QAction(Isci_ekleWindow)
        self.actionStop_Camera.setObjectName("actionStop_Camera")
        self.actionExit = QtWidgets.QAction(Isci_ekleWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionStart_Camera)
        self.menuMenu.addAction(self.actionStop_Camera)
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(Isci_ekleWindow)
        QtCore.QMetaObject.connectSlotsByName(Isci_ekleWindow)
        Isci_ekleWindow.setTabOrder(self.txt_TcNo, self.txt_Adi)
        Isci_ekleWindow.setTabOrder(self.txt_Adi, self.txt_Soyadi)
        Isci_ekleWindow.setTabOrder(self.txt_Soyadi, self.cmb_Vardiyas)
        Isci_ekleWindow.setTabOrder(self.cmb_Vardiyas, self.btn_kayit)

    def retranslateUi(self, Isci_ekleWindow):
        _translate = QtCore.QCoreApplication.translate
        Isci_ekleWindow.setWindowTitle(_translate("Isci_ekleWindow", "MainWindow"))
        self.label.setText(_translate("Isci_ekleWindow", "KAMERA EKRANI"))
        self.label_10.setText(_translate("Isci_ekleWindow", "Vardiyası"))
        self.cmb_Vardiyas.setItemText(0, _translate("Isci_ekleWindow", "Sabah"))
        self.cmb_Vardiyas.setItemText(1, _translate("Isci_ekleWindow", "Akşam"))
        self.cmb_Vardiyas.setItemText(2, _translate("Isci_ekleWindow", "Gece"))
        self.txt_Soyadi.setPlaceholderText(_translate("Isci_ekleWindow", "soyadı"))
        self.btn_kayit.setText(_translate("Isci_ekleWindow", "İsci Ekle"))
        self.txt_Adi.setPlaceholderText(_translate("Isci_ekleWindow", "adı"))
        self.label_5.setText(_translate("Isci_ekleWindow", "Soyadı"))
        self.label_3.setText(_translate("Isci_ekleWindow", "Adı"))
        self.txt_TcNo.setPlaceholderText(_translate("Isci_ekleWindow", "TcNo"))
        self.label_2.setText(_translate("Isci_ekleWindow", "TcNo"))
        self.btn_resimCek.setText(_translate("Isci_ekleWindow", "Resim Çek"))
        self.menuMenu.setTitle(_translate("Isci_ekleWindow", "Menu"))
        self.menuExit.setTitle(_translate("Isci_ekleWindow", "Exit"))
        self.actionStart_Camera.setText(_translate("Isci_ekleWindow", "Start Camera"))
        self.actionStop_Camera.setText(_translate("Isci_ekleWindow", "Stop Camera"))
        self.actionExit.setText(_translate("Isci_ekleWindow", "Exit"))
