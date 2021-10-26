from differential_practicum.ToolBar.ToolBar import *


class WindowToolBar(ToolBar):
    def __init__(self, window, title):
        self._toolbar = window.addToolBar(title)
        self.inputs = list()
        self.check_boxes = list()

    def configure_button(self, args):
        self._toolbar.addWidget(ToolBarButton(*args).get_object())

    def configure_input(self, saver, initial):
        x = ToolBarInput(initial)
        saver.append(x.get_object())
        self._toolbar.addWidget(x.get_object())
        return x.get_object()

    def configure_label(self, args):
        self._toolbar.addWidget(ToolBarLabel(*args).get_object())

    def configure_colored_label(self, args):
        self._toolbar.addWidget(ColoredToolBar(*args).get_object())

    def configure_checkbox(self, args):
        self.check_boxes.append(ToolBarCheckBox(*args).get_object())
        self._toolbar.addWidget(self.check_boxes[-1])

    def get_tool_bar(self):
        return self._toolbar

    def get_check_boxes(self):
        return self.check_boxes


