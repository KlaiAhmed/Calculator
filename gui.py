from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        button_width = 55  
        button_height = 55 
        button_spacing = 20 
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(311, 527)  
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setStyleSheet("background-color: #1E1E1E; color: #FFFFFF;")


        center_vertical = (Dialog.height() - 300) // 2  

        center_horizontal = 15

        self.seven = QtWidgets.QPushButton(Dialog)
        self.seven.setGeometry(QtCore.QRect(center_horizontal, center_vertical + 160, button_width, button_height))
        self.seven.setStyleSheet(self.button_style())
        self.seven.setObjectName("seven")

        self.eight = QtWidgets.QPushButton(Dialog)
        self.eight.setGeometry(QtCore.QRect(center_horizontal + button_width + button_spacing, center_vertical + 160, button_width, button_height))
        self.eight.setStyleSheet(self.button_style())
        self.eight.setObjectName("eight")

        self.nine = QtWidgets.QPushButton(Dialog)
        self.nine.setGeometry(QtCore.QRect(center_horizontal + 2 * (button_width + button_spacing), center_vertical + 160, button_width, button_height))
        self.nine.setStyleSheet(self.button_style())
        self.nine.setObjectName("nine")

        self.div = QtWidgets.QPushButton(Dialog)
        self.div.setGeometry(QtCore.QRect(center_horizontal + 3 * (button_width + button_spacing), center_vertical + 160, button_width, button_height))
        self.div.setStyleSheet(self.button_style())
        self.div.setObjectName("div")

        self.four = QtWidgets.QPushButton(Dialog)
        self.four.setGeometry(QtCore.QRect(center_horizontal, center_vertical + 220, button_width, button_height))
        self.four.setStyleSheet(self.button_style())
        self.four.setObjectName("four")

        self.five = QtWidgets.QPushButton(Dialog)
        self.five.setGeometry(QtCore.QRect(center_horizontal + button_width + button_spacing, center_vertical + 220, button_width, button_height))
        self.five.setStyleSheet(self.button_style())
        self.five.setObjectName("five")

        self.six = QtWidgets.QPushButton(Dialog)
        self.six.setGeometry(QtCore.QRect(center_horizontal + 2 * (button_width + button_spacing), center_vertical + 220, button_width, button_height))
        self.six.setStyleSheet(self.button_style())
        self.six.setObjectName("six")

        self.multi = QtWidgets.QPushButton(Dialog)
        self.multi.setGeometry(QtCore.QRect(center_horizontal + 3 * (button_width + button_spacing), center_vertical + 220, button_width, button_height))
        self.multi.setStyleSheet(self.button_style())
        self.multi.setObjectName("multi")

        self.one = QtWidgets.QPushButton(Dialog)
        self.one.setGeometry(QtCore.QRect(center_horizontal, center_vertical + 280, button_width, button_height))
        self.one.setStyleSheet(self.button_style())
        self.one.setObjectName("one")

        self.two = QtWidgets.QPushButton(Dialog)
        self.two.setGeometry(QtCore.QRect(center_horizontal + button_width + button_spacing, center_vertical + 280, button_width, button_height))
        self.two.setStyleSheet(self.button_style())
        self.two.setObjectName("two")

        self.three = QtWidgets.QPushButton(Dialog)
        self.three.setGeometry(QtCore.QRect(center_horizontal + 2 * (button_width + button_spacing), center_vertical + 280, button_width, button_height))
        self.three.setStyleSheet(self.button_style())
        self.three.setObjectName("three")

        self.minus = QtWidgets.QPushButton(Dialog)
        self.minus.setGeometry(QtCore.QRect(center_horizontal + 3 * (button_width + button_spacing), center_vertical + 280, button_width, button_height))
        self.minus.setStyleSheet(self.button_style())
        self.minus.setObjectName("minus")

        self.neg = QtWidgets.QPushButton(Dialog)
        self.neg.setGeometry(QtCore.QRect(center_horizontal, center_vertical + 340, button_width, button_height))
        self.neg.setStyleSheet(self.button_style())
        self.neg.setObjectName("neg")

        self.zero = QtWidgets.QPushButton(Dialog)
        self.zero.setGeometry(QtCore.QRect(center_horizontal + button_width + button_spacing, center_vertical + 340, button_width, button_height))
        self.zero.setStyleSheet(self.button_style())
        self.zero.setObjectName("zero")

        self.virg = QtWidgets.QPushButton(Dialog)
        self.virg.setGeometry(QtCore.QRect(center_horizontal + 2 * (button_width + button_spacing), center_vertical + 340, button_width, button_height))
        self.virg.setStyleSheet(self.button_style())
        self.virg.setObjectName("virg")

        self.plus = QtWidgets.QPushButton(Dialog)
        self.plus.setGeometry(QtCore.QRect(center_horizontal + 3 * (button_width + button_spacing), center_vertical + 340, button_width, button_height))
        self.plus.setStyleSheet(self.button_style())
        self.plus.setObjectName("plus")

        self.egale = QtWidgets.QPushButton(Dialog)
        self.egale.setGeometry(QtCore.QRect(center_horizontal, center_vertical + 100, button_width, button_height))
        self.egale.setStyleSheet(self.button_style())
        self.egale.setObjectName("egale")

        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(center_horizontal + 2 * (button_width + button_spacing), center_vertical + 100, button_width, button_height))
        self.clear.setStyleSheet(self.button_style())
        self.clear.setObjectName("clear")


        self.mod = QtWidgets.QPushButton(Dialog)
        self.mod.setGeometry(QtCore.QRect(center_horizontal + button_width + button_spacing, center_vertical + 100, button_width, button_height))
        self.mod.setStyleSheet(self.button_style())
        self.mod.setObjectName("mod")
        
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(center_horizontal + 3 * (button_width + button_spacing), center_vertical + 100, button_width, button_height))
        self.back.setStyleSheet(self.button_style())
        self.back.setObjectName("back")

        self.affichage = QtWidgets.QLabel(Dialog)
        self.affichage.setGeometry(QtCore.QRect(center_horizontal, center_vertical + 0, 290, (50)))
        self.affichage.setStyleSheet("background-color: #1E1E1E; color: #FFFFFF; font-size: 24px; padding: 10px;")
        self.affichage.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.affichage.setObjectName("affichage")

        self.title_bar = QtWidgets.QFrame(Dialog)
        self.title_bar.setGeometry(QtCore.QRect(0, 0, 311, 30))
        self.title_bar.setStyleSheet("background-color: #1E1E1E; color: #FFFFFF;")

        self.title_icon = QtWidgets.QLabel(self.title_bar)
        self.title_icon.setGeometry(QtCore.QRect(5, 5, 20, 20))
        self.title_icon.setPixmap(QtGui.QPixmap("D:/work/Projects/calculator/calculator.png"))
        self.title_icon.setScaledContents(True)
        self.title_icon.setObjectName("title_icon")

        self.title_label = QtWidgets.QLabel(self.title_bar)
        self.title_label.setGeometry(QtCore.QRect(30, 0, 200, 30))
        self.title_label.setStyleSheet("font-size: 14px;")
        self.title_label.setObjectName("title_label")
        self.title_label.setText("Calculator")

        self.close_button = QtWidgets.QPushButton(self.title_bar)
        self.close_button.setGeometry(QtCore.QRect(281, 0, 30, 30))
        self.close_button.setStyleSheet(
            "QPushButton {"
            "    background-color: transparent;"
            "    border: none;"
            "    font-size: 20px;"
            "    color: #FFFFFF;"
            "}"
            "QPushButton:hover {"
            "    color: #FF0000;"
            "}"
        )
        self.close_button.setObjectName("close_button")
        self.close_button.setText("×")
        self.close_button.clicked.connect(Dialog.close)

        self.minimize_button = QtWidgets.QPushButton(self.title_bar)
        self.minimize_button.setGeometry(QtCore.QRect(251, 0, 30, 30))
        self.minimize_button.setStyleSheet(
            "QPushButton {"
            "    background-color: transparent;"
            "    border: none;"
            "    font-size: 20px;"
            "    color: #FFFFFF;"
            "}"
            "QPushButton:hover {"
            "    color: #00FFFF;" 
            "}"
        )
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setText("–") 
        self.minimize_button.clicked.connect(Dialog.showMinimized)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.seven.setText(_translate("Dialog", "7"))
        self.eight.setText(_translate("Dialog", "8"))
        self.nine.setText(_translate("Dialog", "9"))
        self.div.setText(_translate("Dialog", "÷"))
        self.three.setText(_translate("Dialog", "3"))
        self.two.setText(_translate("Dialog", "2"))
        self.one.setText(_translate("Dialog", "1"))
        self.minus.setText(_translate("Dialog", "-"))
        self.virg.setText(_translate("Dialog", "."))
        self.zero.setText(_translate("Dialog", "0"))
        self.neg.setText(_translate("Dialog", "±"))
        self.plus.setText(_translate("Dialog", "+"))
        self.six.setText(_translate("Dialog", "6"))
        self.five.setText(_translate("Dialog", "5"))
        self.four.setText(_translate("Dialog", "4"))
        self.multi.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Google Sans,arial,sans-serif\'; font-size:32px; color:#e8e8e8; background-color:#1f1f1f;\">÷</span></p></body></html>"))
        self.multi.setText(_translate("Dialog", "×"))
        self.clear.setText(_translate("Dialog", "C"))
        self.mod.setText(_translate("Dialog", "%"))
        self.egale.setText(_translate("Dialog", "="))
        self.back.setText(_translate("Dialog", "←"))

    def button_style(self):
        return (
            "QPushButton {"
            "    background-color: #333;"
            "    border: 1px solid #555;"
            "    color: #FFF;"
            "    padding: 10px;"
            "    border-radius: 5px;"
            "    font-size: 18px;"
            "}"
            "QPushButton:hover {"
            "    background-color: #555;"
            "}"
            "QPushButton:pressed {"
            "    background-color: #777;"
            "}"
        )