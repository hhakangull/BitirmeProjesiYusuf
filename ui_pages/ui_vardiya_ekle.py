# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\vardiyaekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vardiyekle(object):
    def setupUi(self, vardiyekle):
        vardiyekle.setObjectName("vardiyekle")
        vardiyekle.resize(490, 400)
        vardiyekle.setMinimumSize(QtCore.QSize(490, 400))
        vardiyekle.setMaximumSize(QtCore.QSize(490, 400))
        self.gridLayout = QtWidgets.QGridLayout(vardiyekle)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(vardiyekle)
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
"height:42px;\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"\n"
"}\n"
"QGroupBox{\n"
"border:none;\n"
"\n"
"}\n"
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
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 311, 61))
        self.label_2.setStyleSheet("color: white;\n"
"font: 44px \"Helvetica Neue\", sans-serif;\n"
"margin: 0px 0px 16px;")
        self.label_2.setObjectName("label_2")
        self.spin_Kontenjan = QtWidgets.QSpinBox(self.frame)
        self.spin_Kontenjan.setGeometry(QtCore.QRect(240, 260, 224, 42))
        self.spin_Kontenjan.setObjectName("spin_Kontenjan")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 100, 201, 44))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(20, 210, 126, 44))
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 260, 126, 42))
        self.label_8.setObjectName("label_8")
        self.cmb_vardiya = QtWidgets.QComboBox(self.frame)
        self.cmb_vardiya.setGeometry(QtCore.QRect(240, 210, 224, 44))
        self.cmb_vardiya.setObjectName("cmb_vardiya")
        self.cmb_vardiya.addItem("")
        self.cmb_vardiya.addItem("")
        self.cmb_vardiya.addItem("")
        self.cmb_vardiya.addItem("")
        self.btn_vardiyaEkle = QtWidgets.QPushButton(self.frame)
        self.btn_vardiyaEkle.setGeometry(QtCore.QRect(60, 330, 357, 58))
        self.btn_vardiyaEkle.setStyleSheet("")
        self.btn_vardiyaEkle.setObjectName("btn_vardiyaEkle")
        self.cmb_sorumlu = QtWidgets.QComboBox(self.frame)
        self.cmb_sorumlu.setGeometry(QtCore.QRect(240, 100, 224, 44))
        self.cmb_sorumlu.setObjectName("cmb_sorumlu")
        self.cmb_sorumlu.addItem("")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(20, 150, 201, 44))
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(240, 155, 221, 44))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(vardiyekle)
        QtCore.QMetaObject.connectSlotsByName(vardiyekle)
        vardiyekle.setTabOrder(self.cmb_sorumlu, self.cmb_vardiya)
        vardiyekle.setTabOrder(self.cmb_vardiya, self.spin_Kontenjan)
        vardiyekle.setTabOrder(self.spin_Kontenjan, self.btn_vardiyaEkle)

    def retranslateUi(self, vardiyekle):
        _translate = QtCore.QCoreApplication.translate
        vardiyekle.setWindowTitle(_translate("vardiyekle", "Form"))
        self.label_2.setText(_translate("vardiyekle", "VARDİYA EKLE"))
        self.label.setText(_translate("vardiyekle", "Vardiya Sorumlusu"))
        self.label_10.setText(_translate("vardiyekle", "Vardiya"))
        self.label_8.setText(_translate("vardiyekle", "Kontenjan"))
        self.cmb_vardiya.setCurrentText(_translate("vardiyekle", "Sabah"))
        self.cmb_vardiya.setItemText(0, _translate("vardiyekle", "Sabah"))
        self.cmb_vardiya.setItemText(1, _translate("vardiyekle", "Akşam"))
        self.cmb_vardiya.setItemText(2, _translate("vardiyekle", "Gece"))
        self.btn_vardiyaEkle.setText(_translate("vardiyekle", "VARDİYA EKLE"))
        self.cmb_sorumlu.setCurrentText(_translate("vardiyekle", "Sorumlu Seçiniz"))
        self.cmb_sorumlu.setItemText(0, _translate("vardiyekle", "Sorumlu Seçiniz"))
        self.label_11.setText(_translate("vardiyekle", "Sorumlu Vardiyası"))
import resoruces_rc
