from differential_practicum.ToolBar.ToolBarLabel import *


class ColoredToolBar(ToolBarLabel):
    def __init__(self, color):
        self._label = QLabel()
        self._label.setFixedSize(40, 40)
        self._label.setAutoFillBackground(True)
        self._label.setStyleSheet("background-color : {};".format(color))


