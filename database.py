from PyQt5 import QtWidgets

import mysql.connector
from pymsgbox import alert


def get_cnx_and_cursor():
    try:
        cnx = mysql.connector.connect(user='root', password='i130813',
                                      host='127.0.0.1',
                                      database='photostation')

        return cnx, cnx.cursor(buffered=True)

    except BaseException as e:
        import sys

        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("Fusion")
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Ошибка соединения с базой данных")
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/x.png')))
        msgbox.setText('Проверьте подключение к Базе Данных')
        msgbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        msgbox.setDetailedText(str(e))
        msgbox.exec()


def parse_cursor_to_array(keys, cursor):
    keys = list(keys)
    response = []

    data = cursor.fetchone()
    while data is not None:
        response.append(dict(zip(keys, data)))
        data = cursor.fetchone()

    return response


def parse_cursor_to_dict(keys, cursor):
    response = parse_cursor_to_array(keys, cursor)

    return response[0]
