from PyQt5 import QtWidgets
import main

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.a = 0
        self.ui.pushButton.clicked.connect(self.startTest)
        self.ui.pushButton_2.clicked.connect(self.vopros1)
        self.ui.pushButton_9.clicked.connect(self.nazad1)
        self.ui.pushButton_3.clicked.connect(self.vopros2)
        self.ui.pushButton_10.clicked.connect(self.nazad2)
        self.ui.pushButton_4.clicked.connect(self.vopros3)
        self.ui.pushButton_11.clicked.connect(self.nazad3)
        self.ui.pushButton_5.clicked.connect(self.vopros4)
        self.ui.pushButton_12.clicked.connect(self.nazad4)
        self.ui.pushButton_6.clicked.connect(self.vopros5)
        self.ui.pushButton_13.clicked.connect(self.nazad5)
        self.ui.pushButton_7.clicked.connect(self.vopros6)
        self.ui.pushButton_14.clicked.connect(self.nazad6)
        self.ui.pushButton_8.clicked.connect(self.domoi)

    def startTest(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def vopros1(self):
        if self.ui.radioButton.isChecked():
            self.a += 1
            self.ui.stackedWidget.setCurrentIndex(2)
    def nazad1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def vopros2(self):
        if self.ui.radioButton_7.isChecked():
            self.a += 1
            self.ui.stackedWidget.setCurrentIndex(3)
    def nazad2(self):        
            self.ui.stackedWidget.setCurrentIndex(0)

    def vopros3(self):
        if self.ui.radioButton_10.isChecked():
            self.a += 1
            self.ui.stackedWidget.setCurrentIndex(4)
    def nazad3(self):        
            self.ui.stackedWidget.setCurrentIndex(0)        
    
    def vopros4(self):
        if self.ui.radioButton_15.isChecked():
            self.a += 1
            self.ui.stackedWidget.setCurrentIndex(5)
    def nazad4(self):        
            self.ui.stackedWidget.setCurrentIndex(0)
            
    def vopros5(self):
        if self.ui.radioButton_19.isChecked():
            self.a += 1
            self.ui.stackedWidget.setCurrentIndex(6)
    def nazad5(self):        
            self.ui.stackedWidget.setCurrentIndex(0)

    def vopros6(self):
        if self.ui.radioButton_22.isChecked():
            self.a += 1
            self.ui.stackedWidget.setCurrentIndex(7)
    def nazad6(self):        
        self.ui.stackedWidget.setCurrentIndex(0)

        ocenka = {
            0 : 2,
            4 : 3, 
            5 : 4,
            6 : 5,
        }
        self.ui.label_17.setText(f"Баллы: {self.a}")
        self.ui.label_18.setText(f"Оценка: {ocenka[self.a]}")

    def domoi(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.a = 0
        for i in range(1, 10):
            btn = getattr(self.ui, "radioButton_{}".format(i))
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()
            btn.setAutoExclusive(True)
            btn.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())