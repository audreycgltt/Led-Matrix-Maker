from functools import partial

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from led_matrix_maker.UI.MainWindow import MainWindow
from led_matrix_maker.UI.DisplayWindow import DisplayWindow


class LedMatrixMakerView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = MainWindow()
        self.display_window = DisplayWindow()

        self.main_window.show()


class LedMatrixMakerCtrl:

    def __init__(self, model, view):
        """Controller initializer."""
        self._app = model
        self._view = view

        self._connect_signals()

    def _connect_signals(self):
        """Connect signals and slots."""
        for btn in self._view.main_window.grid_btn:
            btn.clicked.connect(partial(self.grid_btn_clicked, btn))

        self._view.main_window.control_btn["Generate"].clicked.connect(self._generate_result)
        self._view.main_window.control_btn["Exit"].clicked.connect(QApplication.instance().quit)

        self._view.main_window.control_btn["previous_frame"].clicked.connect(self._previous_frame)
        self._view.main_window.control_btn["next_frame"].clicked.connect(self._next_frame)

        self._view.main_window.control_btn["add_frame"].clicked.connect(self._add_frame)
        self._view.main_window.control_btn["duplicate_frame"].clicked.connect(self._duplicate_frame)
        self._view.main_window.control_btn["remove_frame"].clicked.connect(self._remove_frame)

        self._view.main_window.control_btn["up_button"].clicked.connect(self._move_up)  
        self._view.main_window.control_btn["down_button"].clicked.connect(self._move_down)  
        self._view.main_window.control_btn["right_button"].clicked.connect(self._move_right)  
        self._view.main_window.control_btn["left_button"].clicked.connect(self._move_left)  

    def grid_btn_clicked(self, btn):
        displayed_matrix_data = self._app.get_current_matrix_data()
        idx = self._view.main_window.led_layout.indexOf(btn)
        row, column, cols, rows = self._view.main_window.led_layout.getItemPosition(idx)
        current_state = displayed_matrix_data[row][column]

        if current_state == 0:
            btn.setStyleSheet("background-color: {};".format("red"))
            new_state = 1
        else:
            btn.setStyleSheet("background-color: {};".format("grey"))
            new_state = 0
            
        self._app.set_current_matrix_data(row, column, new_state)

    def _move_up(self):
        self._app.move_matrix_up()
        self._update_leds_grid()

    def _move_down(self):
        self._app.move_matrix_down()
        self._update_leds_grid()

    def _move_right(self):
        self._app.move_matrix_right()
        self._update_leds_grid()

    def _move_left(self):
        self._app.move_matrix_left()
        self._update_leds_grid()

    def _update_frame_player(self):

        nb_current = self._app.get_current_data_pos()
        total_frames = self._app.get_nb_frames()

        prev_btn = True if nb_current > 0 else False
        next_btn = True if nb_current < total_frames - 1 else False

        self._view.main_window.update_frame_player(prev_btn, next_btn)
        self._view.main_window.set_frames_nb(current=nb_current, total=total_frames)

    def _add_frame(self):
        self._app.append_new_frame()
        self._update_leds_grid()
        #self._view.main_window.set_frame_nb()

    def _duplicate_frame(self):
        self._app.append_new_frame(duplicate=True)
        self._update_leds_grid()

    def _remove_frame(self):
        self._app.remove_current_frame()
        self._update_leds_grid()

    def _previous_frame(self):
        self._app.move_to_previous()
        self._update_frame_player()
        self._update_leds_grid()

    def _next_frame(self):
        self._app.move_to_next()
        self._update_frame_player()
        self._update_leds_grid()

    def _update_leds_grid(self):
        self._update_frame_player()
        displayed_matrix_data = self._app.get_current_matrix_data()

        for led in self._view.main_window.grid_btn:
            idx = self._view.main_window.led_layout.indexOf(led)
            row, column, cols, rows = self._view.main_window.led_layout.getItemPosition(idx)
            new_state = displayed_matrix_data[row][column]
            if new_state == 0:
                led.setStyleSheet("background-color: {};".format("grey"))
            else:
                led.setStyleSheet("background-color: {};".format("red"))

    def _generate_result(self):
        result_display = self._app.generate_bytes_array()

        self._view.display_window.get_text(result_display)
        self._view.display_window.exec_()

