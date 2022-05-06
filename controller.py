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

    def pow_enable(self) -> None:
        self.label_power.setEnabled(True)
        self.power_input_spinbox.setEnabled(True)
    def pow_disable(self) -> None:
        self.label_power.setEnabled(False)
        self.power_input_spinbox.setEnabled(False)
        self.power_input_spinbox.setValue(0)

    def clear(self) -> None:
        self.output_textbrowser.setText('')
        self.reset_inputs()

    def reset_inputs(self) -> None:
        self.number_input_spinbox.setValue(0)
        self.power_input_spinbox.setValue(0)

        self.radioButton_group_selector.setExclusive(False)
        self.radioButton_one.setChecked(False)
        self.radioButton_two.setChecked(False)
        self.radioButton_three.setChecked(False)
        self.radioButton_group_selector.setExclusive(True)

        self.pow_disable()


    def submit(self) -> None:
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
            self.output_textbrowser.append(outputstring)

        self.reset_inputs()

