import sys

from led_matrix_maker.LedMatrixMakerInterface import LedMatrixMakerCtrl, LedMatrixMakerView
from led_matrix_maker.LedMatrixMakerApp import LedMatrixMakerApp

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QTextEdit


__version__ = "0.1"
__author__ = "Audrey Cigolotti"


def main():
    led_maker = QApplication(sys.argv)

    view = LedMatrixMakerView()
    model = LedMatrixMakerApp()

    LedMatrixMakerCtrl(model=model, view=view)

    sys.exit(led_maker.exec_())


if __name__ == "__main__":
    main()
