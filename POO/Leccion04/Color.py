class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        return self._color

    def __str__(self):
        return f'COlor [color: {self._color}]'