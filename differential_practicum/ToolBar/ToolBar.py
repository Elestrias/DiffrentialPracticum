from abc import abstractmethod

from differential_practicum.ToolBar.ToolBarButton import *
from differential_practicum.ToolBar.ToolBarLabel import *
from differential_practicum.ToolBar.ToolBarInput import *
from differential_practicum.ToolBar.ToolBarColoredLabel import *
from differential_practicum.ToolBar.ToolBarCheckBox import *


class ToolBar:
    @abstractmethod
    def configure_button(self, args):
        pass

    @abstractmethod
    def configure_label(self, args):
        pass

    @abstractmethod
    def configure_input(self):
        pass

