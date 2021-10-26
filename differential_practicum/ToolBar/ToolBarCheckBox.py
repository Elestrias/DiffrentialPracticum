from differential_practicum.ToolBar.ToolBarComponent import ToolBarComponent
from PyQt5.QtWidgets import QCheckBox
from functools import partial


class ToolBarCheckBox(ToolBarComponent):

    def __init__(self, title, function, args):
        self._checkbox = QCheckBox(title)
        self._checkbox.setChecked(True)
        self._checkbox.stateChanged.connect(partial(function, *args))

    def get_object(self):
        return self._checkbox

