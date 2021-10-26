from PyQt5.QtWidgets import QLineEdit
from differential_practicum.ToolBar.ToolBarComponent import ToolBarComponent


class ToolBarInput(ToolBarComponent):
    def __init__(self, initial):
        self._input = QLineEdit()
        self._input.setText(initial)
        self._input.setFixedSize(60, 50)

    def get_object(self):
        return self._input
