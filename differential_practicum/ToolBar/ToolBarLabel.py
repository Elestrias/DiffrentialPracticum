from PyQt5.QtWidgets import QLabel
from differential_practicum.ToolBar.ToolBarComponent import ToolBarComponent


class ToolBarLabel(ToolBarComponent):
    def __init__(self, title_text):
        self._label = QLabel(text=title_text)

    def get_object(self):
        return self._label

