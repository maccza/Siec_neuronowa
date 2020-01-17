from collections import namedtuple

class CustomTuple:

    def init_log_tuple(self):
        Log_Tuple = namedtuple("Log_Tuple",["type","message","return_value"])
        return Log_Tuple
