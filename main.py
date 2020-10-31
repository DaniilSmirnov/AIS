# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from pymsgbox import alert

from database import get_cnx_and_cursor, parse_cursor_to_array, parse_cursor_to_dict
from messaging import Message, wrong_values_in_inputs

import sys

order_number = 0


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_4.setStyleSheet("selection-background-color: rgb(255, 170, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("selection-background-color: rgb(255, 170, 127);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("selection-background-color: rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("selection-background-color: rgb(255, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setStyleSheet("selection-background-color: rgb(255, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_5.setStyleSheet("selection-background-color: rgb(255, 170, 127);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фотоателье"))
        self.pushButton_4.setText(_translate("MainWindow", "Выйти из аккаунта"))
        self.pushButton_6.setText(_translate("MainWindow", "Закрыть смену"))
        self.pushButton.setText(_translate("MainWindow", "Создать заказ"))
        self.pushButton_2.setText(_translate("MainWindow", "Неоплаченные заказы"))
        self.pushButton_3.setText(_translate("MainWindow", "X отчет"))
        self.label.setText(_translate("MainWindow", " "))

        pixmap = QtGui.QPixmap("logo.png")
        self.label.setPixmap(pixmap)

        self.pushButton_5.setText(_translate("MainWindow", "Архив"))

        self.pushButton_6.clicked.connect(self.closeday)
        self.pushButton.clicked.connect(self.setupNewUi)
        self.pushButton_2.clicked.connect(self.setupOrdersUi)
        self.pushButton_3.clicked.connect(self.xdata)
        self.pushButton_4.clicked.connect(self.setupLoginUi)
        self.pushButton_5.clicked.connect(self.setupOldOrdersUi)

    def xdata(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Чековый принтер не подключен")
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/x.png')))
        msgbox.setText('Проверьте подключение к чековому принтеру')
        msgbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        # msgbox.setDetailedText(str(e))
        msgbox.exec()

    def closeday(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Чековый принтер не подключен")
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/x.png')))
        msgbox.setText('Проверьте подключение к чековому принтеру')
        msgbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        # msgbox.setDetailedText(str(e))
        msgbox.exec()

    def setupNewUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.orderlayout = QtWidgets.QGridLayout(self.groupBox_2)

        self.retranslateNewUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateNewUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фотоателье"))
        self.groupBox.setTitle(_translate("MainWindow", "Ассортимент"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Содержимое заказа"))
        self.pushButton.setText(_translate("MainWindow", "Отмена"))
        self.pushButton_2.setText(_translate("MainWindow", "Создать заказ"))

        self.pushButton.clicked.connect(self.setupUi)

        order = []

        def draw_categories():

            cnx, cursor = get_cnx_and_cursor()
            query = "SELECT * from categories;"
            cursor.execute(query)

            for i in reversed(range(self.verticalLayout.count())):
                self.verticalLayout.itemAt(i).widget().deleteLater()

            categories = parse_cursor_to_array(cursor.column_names, cursor)
            for category in categories:
                category = category.get('category')
                button = QtWidgets.QPushButton(str(category.get('name')))
                self.verticalLayout.addWidget(button)
                button.clicked.connect(lambda state, pos=category.get('id_category'): draw_items(pos))

        def draw_items(item):

            for i in reversed(range(self.verticalLayout.count())):
                self.verticalLayout.itemAt(i).widget().deleteLater()

            cnx, cursor = get_cnx_and_cursor()

            query = "select product from product where id_category = %s;"
            data = (item,)
            cursor.execute(query, data)

            products = parse_cursor_to_array()
            for product in products:
                button = QtWidgets.QPushButton(str(product))
                self.verticalLayout.addWidget(button)
                button.clicked.connect(lambda state, pos=str(product): add(pos))

            back_button = QtWidgets.QPushButton("Назад")
            back_button.clicked.connect(draw_categories)
            self.verticalLayout.addWidget(back_button)

        def add(item):
            order.append(item)
            draw_order()

        def draw_order():
            i = 0
            total = 0

            for i in reversed(range(self.orderlayout.count())):
                self.orderlayout.itemAt(i).widget().deleteLater()

            for pos in order:
                button = QtWidgets.QPushButton(pos)
                self.orderlayout.addWidget(button, i, 0, 1, 1)
                query = "select price from product where product = %s"
                data = (pos,)
                cnx, cursor = get_cnx_and_cursor()

                cursor.execute(query, data)

                price = cursor.fetchone()[0]
                total += price
                self.orderlayout.addWidget(QtWidgets.QLabel(str(price) + " Р"), i, 1, 1, 1)

                self.orderlayout.addWidget(QtWidgets.QLabel("Итого " + str(total) + " Р"), i, 0, 1, 1)

        draw_categories()

        def create():
            cnx, cursor = get_cnx_and_cursor()

            query = "insert into orders values (default, 1, null, now(), null)"
            cursor.execute(query)
            cnx.commit()

            query = "select idorder from orders order by idorder desc limit 1;"
            cursor.execute(query)

            for item in cursor:
                for value in item:
                    number = str(value)

            for item in order:
                query = "insert into order_content values (%s, %s)"
                data = (number, item)
                cursor.execute(query, data)

            cnx.commit()

            alert("Заказ создан", "Информация")

            self.setupUi()

        self.pushButton_2.clicked.connect(create)

    def setupOrdersUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateOrdersUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateOrdersUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фотоателье"))
        self.label.setText(_translate("MainWindow", ""))

        cnx, cursor = get_cnx_and_cursor()

        query = "select id_order,open_date from orders where closed_date is null;"
        cursor.execute(query)

        i = 1
        j = 0

        for item in cursor:
            item_group = QtWidgets.QGroupBox("Заказ: " + str(item[0]))
            categorieslayout = QtWidgets.QVBoxLayout(item_group)
            self.gridLayout.addWidget(item_group, i, j, 1, 2)
            item_group.clicked.connect(lambda: print(1))
            for value in item:
                if j == 0:
                    j += 1
                    id = value
                    continue
                categorieslayout.addWidget(QtWidgets.QLabel("Время открытия заказа " + str(value)))
            button = QtWidgets.QPushButton("Рассчет")
            categorieslayout.addWidget(button)
            button.clicked.connect(lambda state, line=id: pay(line))
            i += 1
            j = 0

        def pay(id):
            global order_number
            order_number = id
            self.setupPayUi()

        back_button = QtWidgets.QPushButton("Назад")
        back_button.clicked.connect(self.setupUi)
        self.gridLayout.addWidget(back_button, i, j, 1, 1)

    def setupPayUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslatePayUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslatePayUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фотоателье"))
        self.label.setText(_translate("MainWindow", "Сумма"))
        self.pushButton.setText(_translate("MainWindow", "Оплатить"))

        global order_number
        cnx, cursor = get_cnx_and_cursor()

        query = "select sum(price) from product,order_content where product.product=order_content.id_product && id_order = %s;"
        data = (str(order_number),)

        cursor.execute(query, data)

        for item in cursor:
            for value in item:
                value = int(value)

        self.label.setText("К оплате " + str(int(value)))

        self.comboBox.addItem("Наличные")
        self.comboBox.addItem("Карта")

        back_button = QtWidgets.QPushButton("Назад")
        back_button.clicked.connect(self.setupOrdersUi)
        self.gridLayout.addWidget(back_button, 3, 0, 1, 1)

        def close():
            global order_number
            if self.comboBox.currentIndex() == 0:
                data = ("Cash", order_number)
            if self.comboBox.currentIndex() == 1:
                data = ("Card", order_number)

            # query = "update order set pay_type = %s, closed_date = now() where idorder = %s"
            # cursor.execute(query, data)

            alert("Заказ оплачен. Не забудьте выдать сдачу", "Инфо")

            self.setupUi()

        self.pushButton.clicked.connect(close)

    def setupLoginUi(self):
        MainWindow.setObjectName("Main")
        MainWindow.resize(679, 357)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateLoginUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateLoginUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Фотоателье"))
        self.label_2.setText(_translate("Main", "Логин"))
        self.label_3.setText(_translate("Main", "Пароль"))
        self.pushButton.setText(_translate("Main", "Войти"))
        self.label.setText(_translate("Main", "Вход"))

        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton.clicked.connect(self.login)

    def login(self):
        if self.lineEdit.text().isspace() or self.lineEdit_2.text().isspace():
            card = self.lineEdit.text()
            password = self.lineEdit_2.text()

            cnx, cursor = get_cnx_and_cursor()

            query = "select password from worker where login = %s;"
            data = (card,)
            cursor.execute(query, data)

            try:
                if cursor.rowcount == 0 and cursor.fetchone()[0] == password:
                    wrong_values_in_inputs()
                else:
                    self.setupUi()

            except TypeError:
                wrong_values_in_inputs()

        else:
            wrong_values_in_inputs()

    def setupOldOrdersUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateOldOrdersUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateOldOrdersUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фотоателье"))
        self.label.setText(_translate("MainWindow", ""))

        cnx, cursor = get_cnx_and_cursor()

        query = "select * from orders where closed_date is not null;"
        cursor.execute(query)

        i = 1
        j = 0

        def worker(id):
            query = 'select name from worker where idworker = %s'
            data = (id,)
            cursor.execute(query, data)
            for item in cursor:
                for value in item:
                    return value

        for item in cursor:
            item_group = QtWidgets.QGroupBox("Заказ: " + str(item[0]))
            categorieslayout = QtWidgets.QVBoxLayout(item_group)
            self.gridLayout.addWidget(item_group, i, j, 1, 2)
            item_group.clicked.connect(lambda: print(1))
            for value in item:
                if j == 0:
                    j += 1
                    id = value
                    continue
                if j == 1:
                    categorieslayout.addWidget(QtWidgets.QLabel("Сотрудник " + str(worker(id))))
                if j == 2:
                    categorieslayout.addWidget(QtWidgets.QLabel("Тип оплаты " + str(value)))
                if j == 3:
                    categorieslayout.addWidget(QtWidgets.QLabel("Дата открытия " + str(value)))
                if j == 4:
                    categorieslayout.addWidget(QtWidgets.QLabel("Дата закрытия " + str(value)))
                j += 1
            i += 1
            j = 0

        back_button = QtWidgets.QPushButton("Назад")
        back_button.clicked.connect(self.setupUi)
        self.gridLayout.addWidget(back_button, i, j, 1, 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupLoginUi()
    MainWindow.show()
    sys.exit(app.exec_())
