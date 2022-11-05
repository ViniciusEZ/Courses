from eletronic import *
from log import *


class Smarthphone(Eletronic, LogMixin):
    def __init__(self, name):
        super().__init__(name)
        self._connected = False

    def connect(self):
        if not self._on:
            error = f'{self._name} is not on.'
            print(error)
            self.log_critical(error)
            return

        if self._connected:
            error = f'{self._name} is already connected.'
            print(error)
            self.log_critical(error)
            return

        info = f'{self._name} is now connected.'
        print(info)
        self.log_info(info)
        self._connected = True

    def disconnect(self):
        if not self._connected:
            error = f'{self._name} is not connected.'
            print(error)
            self.log_critical(error)
            return

        info = f'{self._name} was sucessfully disconnected.'
        print(info)
        self.log_info(info)
        self._connected = False
