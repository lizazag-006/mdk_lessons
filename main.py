# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unt.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 584)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 30, 511, 511))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(70, 280, 401, 211))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(200, 60, 131, 41))
        self.label.setObjectName("label")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(170, 110, 241, 31))
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 321, 41))
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.page_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 170, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.page_2)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 210, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.page_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 250, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.page_2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 280, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 430, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 430, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(210, 40, 141, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(50, 110, 131, 41))
        self.label_5.setObjectName("label_5")
        self.radioButton_5 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 160, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 190, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_7.setGeometry(QtCore.QRect(30, 220, 82, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_8.setGeometry(QtCore.QRect(30, 250, 82, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 440, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_10.setGeometry(QtCore.QRect(60, 440, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(200, 10, 211, 111))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 460, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        self.label_7.setGeometry(QtCore.QRect(60, 120, 141, 51))
        self.label_7.setObjectName("label_7")
        self.radioButton_9 = QtWidgets.QRadioButton(self.page_4)
        self.radioButton_9.setGeometry(QtCore.QRect(40, 180, 82, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.page_4)
        self.radioButton_10.setGeometry(QtCore.QRect(40, 220, 82, 17))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(self.page_4)
        self.radioButton_11.setGeometry(QtCore.QRect(40, 250, 82, 17))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.page_4)
        self.radioButton_12.setGeometry(QtCore.QRect(40, 280, 82, 17))
        self.radioButton_12.setObjectName("radioButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_11.setGeometry(QtCore.QRect(90, 460, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_8 = QtWidgets.QLabel(self.page_5)
        self.label_8.setGeometry(QtCore.QRect(200, 40, 191, 81))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_5)
        self.label_9.setGeometry(QtCore.QRect(50, 120, 171, 61))
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 460, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.radioButton_13 = QtWidgets.QRadioButton(self.page_5)
        self.radioButton_13.setGeometry(QtCore.QRect(40, 180, 82, 17))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(self.page_5)
        self.radioButton_14.setGeometry(QtCore.QRect(40, 210, 82, 17))
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_15 = QtWidgets.QRadioButton(self.page_5)
        self.radioButton_15.setGeometry(QtCore.QRect(40, 250, 82, 17))
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_16 = QtWidgets.QRadioButton(self.page_5)
        self.radioButton_16.setGeometry(QtCore.QRect(40, 290, 82, 17))
        self.radioButton_16.setObjectName("radioButton_16")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_12.setGeometry(QtCore.QRect(70, 460, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_10 = QtWidgets.QLabel(self.page_6)
        self.label_10.setGeometry(QtCore.QRect(210, 43, 121, 20))
        self.label_10.setObjectName("label_10")
        self.radioButton_17 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_17.setGeometry(QtCore.QRect(70, 170, 82, 17))
        self.radioButton_17.setObjectName("radioButton_17")
        self.radioButton_18 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_18.setGeometry(QtCore.QRect(70, 200, 82, 17))
        self.radioButton_18.setObjectName("radioButton_18")
        self.radioButton_19 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_19.setGeometry(QtCore.QRect(70, 230, 82, 17))
        self.radioButton_19.setObjectName("radioButton_19")
        self.label_11 = QtWidgets.QLabel(self.page_6)
        self.label_11.setGeometry(QtCore.QRect(100, 100, 261, 16))
        self.label_11.setObjectName("label_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 370, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_13.setGeometry(QtCore.QRect(100, 370, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_12 = QtWidgets.QLabel(self.page_7)
        self.label_12.setGeometry(QtCore.QRect(220, 40, 111, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_7)
        self.label_13.setGeometry(QtCore.QRect(70, 100, 251, 16))
        self.label_13.setObjectName("label_13")
        self.radioButton_20 = QtWidgets.QRadioButton(self.page_7)
        self.radioButton_20.setGeometry(QtCore.QRect(60, 150, 82, 17))
        self.radioButton_20.setObjectName("radioButton_20")
        self.radioButton_21 = QtWidgets.QRadioButton(self.page_7)
        self.radioButton_21.setGeometry(QtCore.QRect(60, 190, 82, 17))
        self.radioButton_21.setObjectName("radioButton_21")
        self.radioButton_22 = QtWidgets.QRadioButton(self.page_7)
        self.radioButton_22.setGeometry(QtCore.QRect(60, 230, 82, 17))
        self.radioButton_22.setObjectName("radioButton_22")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_7.setGeometry(QtCore.QRect(354, 420, 101, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_14.setGeometry(QtCore.QRect(80, 420, 75, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_14 = QtWidgets.QLabel(self.page_8)
        self.label_14.setGeometry(QtCore.QRect(50, 70, 141, 61))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_8)
        self.label_15.setGeometry(QtCore.QRect(50, 180, 161, 41))
        self.label_15.setObjectName("label_15")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 400, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_17 = QtWidgets.QLabel(self.page_8)
        self.label_17.setGeometry(QtCore.QRect(320, 70, 111, 81))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page_8)
        self.label_18.setGeometry(QtCore.QRect(300, 170, 111, 51))
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.page_8)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "НАЧАТЬ"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Тест</span></p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">На сколько ты гений!</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Вопрос 1"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">3*15=?</span></p></body></html>"))
        self.radioButton.setText(_translate("Form", "45"))
        self.radioButton_2.setText(_translate("Form", "50"))
        self.radioButton_3.setText(_translate("Form", "18"))
        self.radioButton_4.setText(_translate("Form", "-12"))
        self.pushButton_2.setText(_translate("Form", "дальше>"))
        self.pushButton_9.setText(_translate("Form", "<назад"))
        self.label_4.setText(_translate("Form", "Вопрос 2"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">10-2=?</span></p></body></html>"))
        self.radioButton_5.setText(_translate("Form", "10"))
        self.radioButton_6.setText(_translate("Form", "20"))
        self.radioButton_7.setText(_translate("Form", "8"))
        self.radioButton_8.setText(_translate("Form", "50"))
        self.pushButton_3.setText(_translate("Form", "дальше>"))
        self.pushButton_10.setText(_translate("Form", "<назад"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Вопрос 3</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "дальше>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">50-20=?</span></p></body></html>"))
        self.radioButton_9.setText(_translate("Form", "50"))
        self.radioButton_10.setText(_translate("Form", "30"))
        self.radioButton_11.setText(_translate("Form", "20"))
        self.radioButton_12.setText(_translate("Form", "15"))
        self.pushButton_11.setText(_translate("Form", "<назад"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Задание 4</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">30*30=?</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "дальше>"))
        self.radioButton_13.setText(_translate("Form", "60"))
        self.radioButton_14.setText(_translate("Form", "120"))
        self.radioButton_15.setText(_translate("Form", "900"))
        self.radioButton_16.setText(_translate("Form", "1200"))
        self.pushButton_12.setText(_translate("Form", "<назад"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Задание 5</span></p></body></html>"))
        self.radioButton_17.setText(_translate("Form", "Иван"))
        self.radioButton_18.setText(_translate("Form", "Сергей"))
        self.radioButton_19.setText(_translate("Form", "Александр"))
        self.label_11.setText(_translate("Form", "Как звали Александра Сергеевича Пушкина?"))
        self.pushButton_6.setText(_translate("Form", "дальше>"))
        self.pushButton_13.setText(_translate("Form", "<назад"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Вопрос 6</span></p></body></html>"))
        self.label_13.setText(_translate("Form", "Сколько фей в Клубе Винкс?"))
        self.radioButton_20.setText(_translate("Form", "3"))
        self.radioButton_21.setText(_translate("Form", "10"))
        self.radioButton_22.setText(_translate("Form", "6"))
        self.pushButton_7.setText(_translate("Form", "завершить тест"))
        self.pushButton_14.setText(_translate("Form", "<назад"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Баллы:</span></p></body></html>"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Оценка:</span></p></body></html>"))
        self.pushButton_8.setText(_translate("Form", "домой"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
