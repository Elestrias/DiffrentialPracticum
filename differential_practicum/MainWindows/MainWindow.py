from abc import abstractmethod

from differential_practicum.ToolBar.TopWindowToolBar import TopWindowToolBar
from differential_practicum.ToolBar.SideToolBar import SideWindowToolBar
from differential_practicum.Drawer.Drawer import Drawer

from matplotlib.figure import Figure
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from differential_practicum.NumericMethods.EulerMethod import EulerMethod
from differential_practicum.NumericMethods.ImporvedEuler import ImprovedEuler
from differential_practicum.NumericMethods.RungeKutta import RungeKutta

import numpy


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setFixedSize(1000, 700)
        self.setCentralWidget(self._main)

        self.first = None
        self.second = None

        self.toolbars = []
        self.checkboxes = []

        self.layout = QtWidgets.QVBoxLayout(self._main)

        self.tool_bar = TopWindowToolBar(self, "WindowToolBar")

        self.drawer = Drawer(1, 1, 6, 0.6, 10)

        self.static_canvas = FigureCanvas(Figure(figsize=(2, 1)))
        self.reload_widjet()

        self.side = SideWindowToolBar(self, "SidePannel")
        self.layout.addWidget(self.addToolBar(QtCore.Qt.RightToolBarArea,
                                              self.side.get_tool_bar()))

        self.set_info(['Euler', 'ImprovedEuler', "Runge-Kutta"])

    def change_ranges(self, new_x, new_y, new_X, new_h):
        self.drawer.change_ranges(float(new_x.text()), float(new_y.text()), float(new_X.text()), float(new_h.text()))
        windows = [self, self.first]
        for window in windows:
            window.drawer = self.drawer
            if window == self.first:
                window.tool_bar.inputs[1].setText(new_x.text())
                window.tool_bar.inputs[2].setText(new_y.text())
                window.tool_bar.inputs[3].setText(new_X.text())
                window.tool_bar.inputs[4].setText(new_h.text())

            window.static_canvas.close()
            window.static_canvas = FigureCanvas(Figure(figsize=(2, 1)))
            window.reload_widjet()
            window.plot_graphs()




    def plot_graphs(self):
        pass

    @abstractmethod
    def reload_widjet(self):
        self.layout.addWidget(self.static_canvas)
        self._static_ax = self.static_canvas.figure.add_subplot(111)

    def setup_first(self, first):
        self.first = first

    def setup_second(self, second):
        self.second = second

    def go_first(self):
        self.close()
        self.first.show()

    def go_second(self):
        self.close()
        self.second.show()

    def set_info(self, titles):
        color = ['red', 'blue', 'black']
        for i in range(3):
            tool_bar = SideWindowToolBar(self, "Checker {}".format(i))
            tool_bar.configure_colored_label([color[i]])
            tool_bar.configure_checkbox([titles[i], self.checked, []])
            self.checkboxes.append(tool_bar.get_check_boxes())
            self.side.get_tool_bar().addWidget(tool_bar.get_tool_bar())

    def checked(self):
        self.static_canvas.close()
        self.static_canvas = FigureCanvas(Figure(figsize=(2, 1)))
        self.reload_widjet()
        self.plot_graphs()


