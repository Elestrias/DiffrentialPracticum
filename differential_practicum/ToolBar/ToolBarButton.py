from functools import partial

from PyQt5.QtWidgets import QPushButton
from differential_practicum.ToolBar.ToolBarComponent import ToolBarComponent


class ToolBarButton(ToolBarComponent):
    def __init__(self, button_name, connect_function, input):
        args = input.copy()
        self._button = QPushButton(text=button_name)
        self._button.clicked.connect(partial(connect_function, *args[1:]))

    def get_object(self):
        return self._button

    def change_title(self, text):
        self._button.setText(text)
