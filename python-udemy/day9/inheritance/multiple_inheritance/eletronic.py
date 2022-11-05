class Eletronic:
    def __init__(self, name):
        self._name = name
        self._on = False

    def turn_on(self):
        if self._on:
            return
        self._on = True

    def turn_off(self):
        if not self._on:
            return
        self._on = False
