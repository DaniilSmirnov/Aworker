from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

db_login = ""
db_pass = ""
db_host = ""


class Ui_adminis(object):
    def setupadminisUi(self, adminis):
        adminis.setObjectName("adminis")
        adminis.resize(741, 380)
        self.centralwidget = QtWidgets.QWidget(adminis)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 4)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 3, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 5, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 721, 253))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 5, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 8)
        adminis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 20))
        self.menubar.setObjectName("menubar")
        adminis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminis)
        self.statusbar.setObjectName("statusbar")
        adminis.setStatusBar(self.statusbar)

        self.retranslateadminisUi(adminis)
        QtCore.QMetaObject.connectSlotsByName(adminis)

    def retranslateadminisUi(self, adminis):
        _translate = QtCore.QCoreApplication.translate
        adminis.setWindowTitle(_translate("adminis", "MainWindow"))
        self.label.setText(_translate("adminis", "Вы авторизованы как:"))
        self.label_2.setText(_translate("adminis", "администратор"))
        self.pushButton_9.setText(_translate("adminis", "Сформировать отчет"))
        self.label_3.setText(_translate("adminis",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">Список заказов:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("adminis", "Закрыть"))
        self.label_6.setText(_translate("adminis", "Дата заказа"))
        self.pushButton_6.setText(_translate("adminis", "Добавить "))
        self.label_5.setText(_translate("adminis", "Кол-во товара"))
        self.label_4.setText(_translate("adminis", "Номер заказа"))
        self.label_7.setText(_translate("adminis", "Стоимость"))
        self.pushButton.setText(_translate("adminis", "Открыть"))
        self.pushButton_2.setText(_translate("adminis", "Удалить"))

        self.pushButton_9.clicked.connect(self.openotchet)

    def openotchet(self):
        Authorization = QtWidgets.QDialog()
        ui = Ui_adminis()
        ui.setupUi(Authorization)
        Authorization.exec_()

    def setupadministartorUi(self, administrator):
        administrator.setObjectName("administrator")
        administrator.resize(260, 211)
        self.centralwidget = QtWidgets.QWidget(administrator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        administrator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(administrator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 20))
        self.menubar.setObjectName("menubar")
        administrator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(administrator)
        self.statusbar.setObjectName("statusbar")
        administrator.setStatusBar(self.statusbar)

        self.retranslateadministratorUi(administrator)
        QtCore.QMetaObject.connectSlotsByName(administrator)

    def retranslateadministratorUi(self, administrator):
        _translate = QtCore.QCoreApplication.translate
        administrator.setWindowTitle(_translate("administrator", "Dialog"))
        self.label.setText(_translate("administrator", "Отчет успешно загружен"))
        self.pushButton.setText(_translate("administrator", "Ок"))

    def setupUi(self, Authorization):
        Authorization.setObjectName("Authorization")
        Authorization.resize(282, 219)
        self.gridLayout = QtWidgets.QGridLayout(Authorization)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Authorization)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(Authorization)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(Authorization)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Authorization)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(Authorization)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Authorization)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(Authorization)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Authorization)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Authorization)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Authorization)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 2, 1, 1)

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)

    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "Отчет"))
        self.label_3.setText(_translate("Authorization", "Формирование отчета"))
        self.label_4.setText(_translate("Authorization", "Статистика за период"))
        self.label.setText(_translate("Authorization", "С:"))
        self.lineEdit_2.setText(_translate("Authorization", "12.04.1996"))
        self.label_2.setText(_translate("Authorization", "По:"))
        self.lineEdit.setText(_translate("Authorization", "13.05.1997"))
        self.label_5.setText(_translate("Authorization", "Магазин:"))
        self.lineEdit_3.setText(_translate("Authorization", "Контрольная точка №2"))
        self.pushButton.setText(_translate("Authorization", "Товары"))
        self.pushButton_2.setText(_translate("Authorization", "Продавцы"))

    def setupLoginUi(self, oshibka):
        oshibka.setObjectName("oshibka")
        oshibka.resize(290, 233)
        self.verticalLayout = QtWidgets.QVBoxLayout(oshibka)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(oshibka)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(oshibka)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(oshibka)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(oshibka)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(oshibka)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(oshibka)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(oshibka)
        self.lineEdit_2.setMouseTracking(False)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_2.setToolTip("")
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_8 = QtWidgets.QLabel(oshibka)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(oshibka)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit_3 = QtWidgets.QLineEdit(oshibka)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(oshibka)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_6 = QtWidgets.QLabel(oshibka)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.retranslateLoginUi(oshibka)
        QtCore.QMetaObject.connectSlotsByName(oshibka)

    def retranslateLoginUi(self, oshibka):
        _translate = QtCore.QCoreApplication.translate
        oshibka.setWindowTitle(_translate("oshibka", "Авторизация"))
        self.label_3.setText(_translate("oshibka", "АИС для БД ООО \"Компьютер\""))
        self.label.setText(_translate("oshibka", "Логин:"))
        self.label_4.setText(_translate("oshibka", "<html><head/><body><p><span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.label_2.setText(_translate("oshibka", "Пароль:"))
        self.label_5.setText(_translate("oshibka", "<html><head/><body><p><span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.label_8.setText(_translate("oshibka", "<html><head/><body><p><span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.label_7.setText(_translate("oshibka", "Адрес:"))
        self.pushButton.setText(_translate("oshibka", "Войти"))
        self.label_6.setToolTip(_translate("oshibka", "<html><head/><body><p><span style=\" color:#aa0000;\">Rkfcc</span></p></body></html>"))
        self.label_6.setText(_translate("oshibka", ""))

        self.pushButton.clicked.connect(self.login)

    def login(self):

        global db_host, db_password

        if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.lineEdit_3.text() != "" and self.lineEdit_3.text().find(":") != -1:
            adress = self.lineEdit_3.text().split(":")
            password = adress[1]
            adress = adress[0]

            try:

                cnx = mysql.connector.connect(user='root', password=password,
                                          host=adress,
                                          database='aiskom')
                cursor = cnx.cursor()

                db_host = adress
                db_password = password

            except BaseException:
                self.label_6.setText("<html><head/><body><p><span style=\" color:#ff0000;\">Проверьте правильность введеных данных</span></p></body></html>")

            try:
                query = "select password from uspas where login= %s"
                data = (self.lineEdit_2.text())
                cursor.execute(query, data)
                for item in cursor:
                    if item[0] == data:
                        if self.lineEdit.text() == "admin":
                            self.setupadminisUi()

            except BaseException:
                self.label_6.setText("<html><head/><body><p><span style=\" color:#ff0000;\">Проверьте правильность введеных данных</span></p></body></html>")



        else:
            self.label_6.setText(
                "<html><head/><body><p><span style=\" color:#ff0000;\">Проверьте правильность введеных данных</span></p></body></html>")

    def setupsostavdogUi(self, sostavdog):
        sostavdog.setObjectName("sostavdog")
        sostavdog.resize(333, 417)
        self.gridLayout = QtWidgets.QGridLayout(sostavdog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(sostavdog)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(sostavdog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(sostavdog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(sostavdog)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(sostavdog)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.textEdit_3 = QtWidgets.QTextEdit(sostavdog)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout.addWidget(self.textEdit_3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(sostavdog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(sostavdog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(sostavdog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 2)

        self.retranslatesostavdogUi(sostavdog)
        QtCore.QMetaObject.connectSlotsByName(sostavdog)

    def retranslatesostavdogUi(self, sostavdog):
        _translate = QtCore.QCoreApplication.translate
        sostavdog.setWindowTitle(_translate("sostavdog", "Dialog"))
        self.pushButton_5.setText(_translate("sostavdog", "Добавить"))
        self.pushButton_4.setText(_translate("sostavdog", "Закрыть"))
        self.label.setText(_translate("sostavdog", "Штрафы и премии (дата, объем)"))
        self.textEdit.setHtml(_translate("sostavdog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12.04.2017</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-1299</p></body></html>"))
        self.textEdit_2.setHtml(_translate("sostavdog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13.05.2017</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23000</p></body></html>"))
        self.textEdit_3.setHtml(_translate("sostavdog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24.09.2017</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12000</p></body></html>"))
        self.pushButton.setText(_translate("sostavdog", "Убрать"))
        self.pushButton_2.setText(_translate("sostavdog", "Убрать"))
        self.pushButton_3.setText(_translate("sostavdog", "Убрать"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Authorization = QtWidgets.QMainWindow()
    ui = Ui_adminis()
    ui.setupLoginUi(Authorization)
    Authorization.show()
    sys.exit(app.exec_())

