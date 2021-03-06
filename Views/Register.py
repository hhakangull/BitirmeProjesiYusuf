from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow
from PyQt5.QtCore import QCoreApplication
from ui_pages.ui_kayit import Ui_VardiyaSorumluKayit
from Database.DataBaseConnection import CreateConnection
from secrets import compare_digest


class RegisterWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_VardiyaSorumluKayit()
        self.ui.setupUi(self)
        self.ui_setting()
        self.initSlots()
        self.checkAdmin()
        self.show()

    def checkAdmin(self):
        db = CreateConnection()["users"]
        result = db.find_one({
            "user_role": {"$eq": "admin"}
        })
        if result:
            self.clearForm()
        else:
            return None

    def testButton(self):
        test = self.ui.cmb_vardiya.currentText()
        print(test)

    def ui_setting(self):
        self.ui.txt_kullaniciAdi.setText("deneme1")
        self.ui.txt_sifre.setText("123123")
        self.ui.txt_sifreTekrar.setText("123123")
        self.ui.txt_adi.setText("deneme ad")
        self.ui.txt_soyadi.setText("deneme soyad")
        self.ui.txt_mail.setText("deneme@gmail.com")

    def initSlots(self):
        self.ui.btn_signup.clicked.connect(self.getDataFromApp)

    def getDataFromApp(self):
        name = self.ui.txt_adi.text()
        lastname = self.ui.txt_soyadi.text()
        full_name = name + " " + lastname
        userType = self.ui.cmb_vardiya.currentText()
        username = self.ui.txt_kullaniciAdi.text()
        password = self.ui.txt_sifre.text()
        checkPassword = self.ui.txt_sifreTekrar.text()
        phone = "5317328099"
        email = self.ui.txt_mail.text()
        data = (full_name, userType, username, password, phone, email)
        if compare_digest(checkPassword, password):
            if userType == "Admin":
                self.registerAdminFromOperations(data)
            elif userType == "SuperVisor":
                self.registerSuperVisorFromOperation(data)
            else:
                QMessageBox.warning(self, "Hata", "Lütfen Kullanıcı Türünü Seçiniz")
        else:
            QMessageBox.warning(self, "Şifre", "Şifreler Uyuşmuyor")

    def registerSuperVisorFromOperation(self, data):
        from Controllers.SuperVisor import SuperVisor
        from Controllers.CommonMethods import CommonMethods
        newSupervisor = SuperVisor()
        checkParameters = CommonMethods()
        newSupervisor.full_name = data[0]
        newSupervisor.user_role = "supervisor"
        newSupervisor.username = data[2]
        newSupervisor.password = data[3]
        newSupervisor.phone = data[4]
        newSupervisor.email = data[5]
        checkUserName = checkParameters.checkUserName(newSupervisor.username)
        print(f'checkusername : {checkUserName}')
        checkEmail = checkParameters.checkEmail(newSupervisor.email)
        print(f'checkEmail : {checkEmail}')
        if checkUserName:
            QMessageBox.warning(self, "Username Kontrol", f'{newSupervisor.username} kullanılmaktadır.')
        elif checkEmail:
            QMessageBox.warning(self, "Email Kontrol", f'{newSupervisor.email} kullanılmaktadır.')
        else:
            result = newSupervisor.save()
            print(result)
            if result:
                QMessageBox.information(self, "Kayıt Durumu", "Kayıt Başarlı Oldu!")
                self.clearForm()
            else:
                QMessageBox.critical(self, "Kayıt Durumu", "Kayıt Başarısız Oldu!")

    def registerAdminFromOperations(self, data):
        from Controllers.Admin import Admin
        from Controllers.CommonMethods import CommonMethods
        newAdmin = Admin()
        checkParameters = CommonMethods()
        newAdmin.full_name = data[0]
        newAdmin.user_role = "admin"
        newAdmin.username = data[2]
        newAdmin.password = data[3]
        newAdmin.phone = data[4]
        newAdmin.email = data[5]
        checkUserName = checkParameters.checkUserName(newAdmin.username)
        checkEmail = checkParameters.checkEmail(newAdmin.email)
        if checkUserName:
            QMessageBox.warning(self, "Username Kontrol", f'{newAdmin.username} kullanılmaktadır.')

        elif checkEmail:
            QMessageBox.warning(self, "Email Kontrol", f'{newAdmin.email} kullanılmaktadır.')
        else:
            result = newAdmin.save()
            if result:
                QMessageBox.information(self, "Kayıt Durumu", "Kayıt Başarlı Oldu!")
                self.clearForm()
            else:
                QMessageBox.critical(self, "Kayıt Durumu", "Kayıt Başarısız Oldu!")

    def clearForm(self):
        self.ui.txt_sifre.clear()
        self.ui.txt_sifreTekrar.clear()
        self.ui.txt_kullaniciAdi.clear()
        self.ui.txt_mail.clear()
        self.ui.txt_adi.clear()
        self.ui.txt_soyadi.clear()
        self.ui.cmb_vardiya.removeItem(2)
        _translate = QCoreApplication.translate
        self.ui.cmb_vardiya.setItemText(0, _translate("VardiyaSorumluKayit", "Rol Seçiniz"))
        self.ui.cmb_vardiya.setItemText(1, _translate("VardiyaSorumluKayit", "SuperVisor"))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    VardiyaKayitWindow = RegisterWindow()
    VardiyaKayitWindow.show()
    sys.exit(app.exec_())
