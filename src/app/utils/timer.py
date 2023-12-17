"""Timer"""


import time


class Timer:
    """Timer"""
    __start = time.time()

    @property
    def end(self):
        """Get second passed from self.__START"""
        return time.time() - self.__start

    @property
    def start(self):
        """Get start value"""
        return self.__start

    def set_start_to_current(self):
        """Set start value to current time"""
        self.__start = time.time()
