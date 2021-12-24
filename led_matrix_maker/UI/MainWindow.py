from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Led Matrix Maker")

        self.current_frame_nb = 1
        self.nb_frames = 1
        self.frame_label = QLabel(f"Frame: {self.current_frame_nb}/{self.nb_frames}")

        self.grid_btn = []
        self.control_btn = {}

        self.general_layout = QVBoxLayout()
        self.upper_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()
        self.led_layout = QGridLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.general_layout)
        
        self._create_leds_grid_btn()
        self._create_right_menu_display()
        self._create_bottom_btn()
        self._create_general_display()

    def _create_general_display(self):

        self.general_layout.addLayout(self.upper_layout)
        self.general_layout.addLayout(self.bottom_layout)

        self.setLayout(self.general_layout)  

    def _create_bottom_btn(self):
        bottom_button_layout = QHBoxLayout()

        self.control_btn["Generate"] = QPushButton('&Generate')
        self.control_btn["Exit"] = QPushButton('&Exit')
        bottom_button_layout.addWidget(self.control_btn["Generate"])
        bottom_button_layout.addWidget(self.control_btn["Exit"])

        self.bottom_layout.addLayout(bottom_button_layout)   

    def _create_right_menu_display(self):


        move_box = QGroupBox("Movements")

        self.control_btn["up_button"] = QToolButton()
        self.control_btn["up_button"].setArrowType(Qt.UpArrow)
        self.control_btn["down_button"] = QToolButton()
        self.control_btn["down_button"].setArrowType(Qt.DownArrow)
        self.control_btn["right_button"] = QToolButton()
        self.control_btn["right_button"].setArrowType(Qt.RightArrow)
        self.control_btn["left_button"] = QToolButton()
        self.control_btn["left_button"].setArrowType(Qt.LeftArrow)

        joystick_layout = QGridLayout()
        joystick_layout.addWidget(self.control_btn["up_button"], 0, 1)
        joystick_layout.addWidget(self.control_btn["down_button"], 2, 1)
        joystick_layout.addWidget(self.control_btn["right_button"], 1, 3)
        joystick_layout.addWidget(self.control_btn["left_button"], 1, 0)

        move_box.setLayout(joystick_layout)

        frames_box = QGroupBox("Frames")
        frames_control = QVBoxLayout()

        frame_player = QHBoxLayout()
        self.control_btn["previous_frame"] = QToolButton()
        self.control_btn["previous_frame"].setArrowType(Qt.LeftArrow)
        self.control_btn["previous_frame"].setEnabled(False)
        self.control_btn["next_frame"] = QToolButton()
        self.control_btn["next_frame"].setArrowType(Qt.RightArrow)
        self.control_btn["next_frame"].setEnabled(False)
        frame_player.addWidget(self.control_btn["previous_frame"])
        frame_player.addWidget(self.control_btn["next_frame"])
        frames_control.addLayout(frame_player)

        frames_control_layout = QVBoxLayout()
        self.control_btn["add_frame"] = QPushButton("Add New")
        self.control_btn["duplicate_frame"] = QPushButton("Duplicate")
        self.control_btn["remove_frame"] = QPushButton("Remove Current")
        self.control_btn["remove_frame"].setEnabled(False)
        frames_control_layout.addWidget(self.control_btn["add_frame"])
        frames_control_layout.addWidget(self.control_btn["duplicate_frame"])
        frames_control_layout.addWidget(self.control_btn["remove_frame"])

        frames_control.addLayout(frames_control_layout)
        frames_box.setLayout(frames_control)

        menu_layout = QVBoxLayout()
        menu_layout.addWidget(move_box)
        menu_layout.addWidget(frames_box)
        menu_layout.addStretch()
        menu_layout.addWidget(self.frame_label)

        self.upper_layout.addLayout(menu_layout)

    def _create_leds_grid_btn(self):

        led_pos = [
                    (0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7),
                    (1, 0),(1, 1),(1, 2),(1, 3),(1, 4),(1, 5),(1, 6),(1, 7),
                    (2, 0),(2, 1),(2, 2),(2, 3),(2, 4),(2, 5),(2, 6),(2, 7),
                    (3, 0),(3, 1),(3, 2),(3, 3),(3, 4),(3, 5),(3, 6),(3, 7),
                    (4, 0),(4, 1),(4, 2),(4, 3),(4, 4),(4, 5),(4, 6),(4, 7),
                    (5, 0),(5, 1),(5, 2),(5, 3),(5, 4),(5, 5),(5, 6),(5, 7),
                    (6, 0),(6, 1),(6, 2),(6, 3),(6, 4),(6, 5),(6, 6),(6, 7),
                    (7, 0),(7, 1),(7, 2),(7, 3),(7, 4),(7, 5),(7, 6),(7, 7),
                ]

        for pos in led_pos:
            led = QPushButton()
            led.setStyleSheet("background-color: gray;")
            led.setFixedSize(40, 40)
            self.grid_btn.append(led)
            self.led_layout.addWidget(led, pos[0], pos[1])
            #led.clicked.connect(partial(change, led))

        self.upper_layout.addLayout(self.led_layout)

    def update_frame_player(self, previous_btn_state=False, next_btn_state=False, remove_btn_state=False):
        self.control_btn["previous_frame"].setEnabled(previous_btn_state)
        self.control_btn["next_frame"].setEnabled(next_btn_state)
        self.control_btn["remove_frame"].setEnabled(remove_btn_state)

    def set_frames_nb(self, current, total):
        self.current_frame_nb = current
        self.nb_frames = total

        self.frame_label.setText(f"Frame: {self.current_frame_nb + 1}/{self.nb_frames}")

