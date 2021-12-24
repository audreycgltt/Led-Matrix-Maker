from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTextEdit


class DisplayWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Result")
        self.general_layout = QVBoxLayout()

        self.text_body = QTextEdit("")

        self._create_display()

    def _create_display(self):
        self.general_layout.addWidget(self.text_body)
        self.setLayout(self.general_layout)

    def get_text(self, result_display):
        self.text_body.setText(result_display)

