from PyQt5.QtWidgets import *
from view import Ui_MainWindow

from lab07 import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(338, 418)
        self.setupUi(self)
        self.run_button.clicked.connect(lambda : self.submit())
        self.clear_button.clicked.connect(lambda : self.clear())
        self.radioButton_one.clicked.connect(lambda : self.pow_disable())
        self.radioButton_two.clicked.connect(lambda : self.pow_enable())
        self.radioButton_three.clicked.connect(lambda : self.pow_disable())

    def pow_enable(self):
        self.label_power.setEnabled(True)
        self.power_input_spinbox.setEnabled(True)
    def pow_disable(self):
        self.label_power.setEnabled(False)
        self.power_input_spinbox.setEnabled(False)

    def clear(self):
        self.output_textbrowser.setText('')

    def submit(self):
        number = int(self.number_input_spinbox.text())

        power = int(self.power_input_spinbox.text())

        if self.radioButton_one.isChecked():
            outputstring = one(number)
            self.output_textbrowser.append(str(outputstring))
        elif self.radioButton_two.isChecked():
            outputstring = two(number, power)
            self.output_textbrowser.append(str(outputstring))
        elif self.radioButton_three.isChecked():
            outputstring = three(number)
            print(outputstring)
            print(outputstring.strip())
            self.output_textbrowser.append(outputstring)

