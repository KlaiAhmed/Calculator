import sys
from PyQt5 import QtGui, QtWidgets
from gui import Ui_Dialog

class CalculatorApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.res = ""
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.one.clicked.connect(lambda: self.append_to_res('1'))
        self.ui.two.clicked.connect(lambda: self.append_to_res('2'))
        self.ui.three.clicked.connect(lambda: self.append_to_res('3'))
        self.ui.four.clicked.connect(lambda: self.append_to_res('4'))
        self.ui.five.clicked.connect(lambda: self.append_to_res('5'))
        self.ui.six.clicked.connect(lambda: self.append_to_res('6'))
        self.ui.seven.clicked.connect(lambda: self.append_to_res('7'))
        self.ui.eight.clicked.connect(lambda: self.append_to_res('8'))
        self.ui.nine.clicked.connect(lambda: self.append_to_res('9'))
        self.ui.zero.clicked.connect(lambda: self.append_to_res('0'))
        self.ui.plus.clicked.connect(lambda: self.append_to_res('+'))
        self.ui.minus.clicked.connect(lambda: self.append_to_res('-'))
        self.ui.multi.clicked.connect(lambda: self.append_to_res('*'))
        self.ui.div.clicked.connect(lambda: self.append_to_res('/'))
        self.ui.mod.clicked.connect(lambda: self.append_to_res('%'))
        self.ui.virg.clicked.connect(lambda: self.append_to_res('.'))
        self.ui.neg.clicked.connect(self.on_neg_clicked)
        self.ui.clear.clicked.connect(self.on_clear_clicked)
        self.ui.back.clicked.connect(self.on_back_clicked)
        self.ui.egale.clicked.connect(self.on_egale_clicked)

    def update_display(self):
        self.ui.affichage.setText(self.res)

    def append_to_res(self, value):
        self.res += value
        self.update_display()

    def on_neg_clicked(self):
        if self.res:
            if self.res[0] == '-':
                self.res = self.res[1:]
            else:
                self.res = '-' + self.res
        self.update_display()

    def on_clear_clicked(self):
        self.res=''
        self.update_display()

    def on_back_clicked(self):
        self.res = self.res[:-1]
        self.update_display()

    def on_egale_clicked(self):
        try:
            self.res = str(eval(self.res))
        except Exception as e:
            self.res = 'Error'
        self.update_display()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = CalculatorApp()
    main_window.show()
    sys.exit(app.exec_())
