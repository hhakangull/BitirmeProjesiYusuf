# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\vardiya_duzenle.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vardiyaduzenFrom(object):
    def setupUi(self, vardiyaduzenFrom):
        vardiyaduzenFrom.setObjectName("vardiyaduzenFrom")
        vardiyaduzenFrom.resize(585, 667)
        self.gridLayout = QtWidgets.QGridLayout(vardiyaduzenFrom)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(vardiyaduzenFrom)
        self.frame.setStyleSheet("QFrame{\n"
"background: #354152;\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit{\n"
"height: 45px;\n"
"border-radius:15px;\n"
"padding-left: 18px;\n"
"font-size: 20px;\n"
"background:white;\n"
"}\n"
"QPushButton{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:20px;\n"
"    padding-left:15px;\n"
"    height:42px;\n"
"    border-radius:15px;\n"
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
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_resim = QtWidgets.QLabel(self.frame)
        self.lbl_resim.setGeometry(QtCore.QRect(50, 50, 201, 191))
        self.lbl_resim.setStyleSheet("background: white;\n"
"border-radius:15px;\n"
"")
        self.lbl_resim.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_resim.setObjectName("lbl_resim")
        self.list_verilenVardiyalar = QtWidgets.QListWidget(self.frame)
        self.list_verilenVardiyalar.setGeometry(QtCore.QRect(50, 360, 201, 181))
        self.list_verilenVardiyalar.setStyleSheet("background: white;\n"
"border-radius:15px;\n"
"font-size:16px;\n"
"padding-left:10px;\n"
"padding-top:10px;\n"
"")
        self.list_verilenVardiyalar.setObjectName("list_verilenVardiyalar")
        self.btn_update = QtWidgets.QPushButton(self.frame)
        self.btn_update.setGeometry(QtCore.QRect(50, 590, 511, 51))
        self.btn_update.setObjectName("btn_update")
        self.btn_resimCek = QtWidgets.QPushButton(self.frame)
        self.btn_resimCek.setGeometry(QtCore.QRect(50, 260, 201, 41))
        self.btn_resimCek.setObjectName("btn_resimCek")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(270, 40, 281, 521))
        self.frame_2.setStyleSheet("border:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txt_id = QtWidgets.QLineEdit(self.frame_2)
        self.txt_id.setEnabled(False)
        self.txt_id.setObjectName("txt_id")
        self.gridLayout_2.addWidget(self.txt_id, 0, 0, 1, 1)
        self.txt_adi = QtWidgets.QLineEdit(self.frame_2)
        self.txt_adi.setObjectName("txt_adi")
        self.gridLayout_2.addWidget(self.txt_adi, 1, 0, 1, 1)
        self.txt_soyadi = QtWidgets.QLineEdit(self.frame_2)
        self.txt_soyadi.setObjectName("txt_soyadi")
        self.gridLayout_2.addWidget(self.txt_soyadi, 2, 0, 1, 1)
        self.txt_kadi = QtWidgets.QLineEdit(self.frame_2)
        self.txt_kadi.setEnabled(True)
        self.txt_kadi.setObjectName("txt_kadi")
        self.gridLayout_2.addWidget(self.txt_kadi, 3, 0, 1, 1)
        self.txt_sifre = QtWidgets.QLineEdit(self.frame_2)
        self.txt_sifre.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.txt_sifre.setObjectName("txt_sifre")
        self.gridLayout_2.addWidget(self.txt_sifre, 4, 0, 1, 1)
        self.txt_mail = QtWidgets.QLineEdit(self.frame_2)
        self.txt_mail.setObjectName("txt_mail")
        self.gridLayout_2.addWidget(self.txt_mail, 5, 0, 1, 1)
        self.txt_vardiyasi = QtWidgets.QLineEdit(self.frame_2)
        self.txt_vardiyasi.setText("")
        self.txt_vardiyasi.setObjectName("txt_vardiyasi")
        self.gridLayout_2.addWidget(self.txt_vardiyasi, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 320, 181, 31))
        self.label.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(vardiyaduzenFrom)
        QtCore.QMetaObject.connectSlotsByName(vardiyaduzenFrom)
        vardiyaduzenFrom.setTabOrder(self.btn_update, self.list_verilenVardiyalar)
        vardiyaduzenFrom.setTabOrder(self.list_verilenVardiyalar, self.btn_resimCek)

    def retranslateUi(self, vardiyaduzenFrom):
        _translate = QtCore.QCoreApplication.translate
        vardiyaduzenFrom.setWindowTitle(_translate("vardiyaduzenFrom", "Form"))
        self.lbl_resim.setText(_translate("vardiyaduzenFrom", "Resim"))
        self.btn_update.setText(_translate("vardiyaduzenFrom", "Güncelle"))
        self.btn_resimCek.setText(_translate("vardiyaduzenFrom", "Resim Çek"))
        self.txt_id.setPlaceholderText(_translate("vardiyaduzenFrom", "Id"))
        self.txt_adi.setPlaceholderText(_translate("vardiyaduzenFrom", "Adı"))
        self.txt_soyadi.setPlaceholderText(_translate("vardiyaduzenFrom", "Soyadı"))
        self.txt_kadi.setPlaceholderText(_translate("vardiyaduzenFrom", "Kullanıcı Adı"))
        self.txt_sifre.setPlaceholderText(_translate("vardiyaduzenFrom", "Şifre"))
        self.txt_mail.setPlaceholderText(_translate("vardiyaduzenFrom", "E-mail"))
        self.txt_vardiyasi.setPlaceholderText(_translate("vardiyaduzenFrom", "Vardiya"))
        self.label.setText(_translate("vardiyaduzenFrom", "Variyası"))