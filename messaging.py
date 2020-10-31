from PyQt5 import QtCore, QtGui, QtWidgets


class Message(object):
    def show(self, Title, Text):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle(Title)
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/i.png')))
        msgbox.setText(Text)
        msgbox.exec()


def wrong_values_in_inputs():
    Message.show(Message, "Ошибка", "Проверьте правильность введеных данных")
