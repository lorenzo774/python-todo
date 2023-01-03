class Todo:
    def __init__(self, msg: str):
        self.__done = False
        self.__msg = msg

    def set_msg(self, new_msg: str):
        self.__msg = new_msg

    def get_msg(self):
        return self.__msg

    def is_done(self):
        return self.__done

    def toggle_check(self):
        self.__done = not self.__done