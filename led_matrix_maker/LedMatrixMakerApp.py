class LedMatrixMakerApp:

    def __init__(self):

        self.current_matrix_pos = 0
        self.led_matrix_data = []
        self.frames_list = []

        self._init_frames_list()

    def _init_frames_list(self):
        self.frames_list.append(self._init_matrix_data())

    def _init_matrix_data(self):
        matrix_data = [0] * 8
        for i in range(8):
            matrix_data[i] = [0] * 8

        return matrix_data

    def move_matrix_up(self):
        self.frames_list[self.current_matrix_pos].pop(0)
        self.frames_list[self.current_matrix_pos].append([0, 0, 0, 0, 0, 0 ,0, 0])

    def move_matrix_down(self):
        self.frames_list[self.current_matrix_pos].pop()
        self.frames_list[self.current_matrix_pos].insert(0, [0, 0, 0, 0, 0, 0 ,0, 0])

    def move_matrix_right(self):
        for line in self.frames_list[self.current_matrix_pos]:
            line.pop()
            line.insert(0, 0)

    def move_matrix_left(self):
        for line in self.frames_list[self.current_matrix_pos]:
            line.pop(0)
            line.append(0)

    def append_new_frame(self):
        self.frames_list.append(self._init_matrix_data())
        self.current_matrix_pos += 1

    def get_current_data_pos(self):
        return self.current_matrix_pos

    def get_current_matrix_data(self):
        return self.frames_list[self.current_matrix_pos]

    def set_current_matrix_data(self, row, column, new_state):
        self.frames_list[self.current_matrix_pos][row][column] = new_state

    def get_nb_frames(self):
        return len(self.frames_list)

    def move_to_previous(self):
        if self.current_matrix_pos >= 1:
            self.current_matrix_pos -= 1

    def move_to_next(self):
        if self.current_matrix_pos < len(self.frames_list) - 1:
            self.current_matrix_pos += 1

    def generate_bytes_array(self):
        matrix_data = self.convert(self.frames_list)
        print(matrix_data)
        str_bytes_array = "[{}]".format(",".join(matrix_data))
        return str_bytes_array

    @staticmethod
    def convert(data):
        res = []
        for anim in data:
            res.append("[")
            for raw_byte in anim:
                bin_str_byte = "".join(map(str, raw_byte))
                res.append(str(int("0b{}".format(bin_str_byte), 2)))
            res.append("]")

        return res 