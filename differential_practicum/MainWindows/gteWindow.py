from PyQt5.QtWidgets import QLineEdit

from differential_practicum.MainWindows.MainWindow import *


class gteWindow(MainWindow):
    def __init__(self):
        super().__init__()
        side = SideWindowToolBar(self, "SidePannel")
        self.tool_bar.create_window(self, "GTE:  ", ["x0", "y0", "X", "N"], ["1", "1", "6", "10"])

        self.side.configure_button(["go to aproximation", self.go_first, [self.first]])
        self.side.configure_button(["go to lte", self.go_second, [self.second]])

        self.plot_graphs()


    def change_ranges(self, new_x, new_y, new_X, new_h):
        self.drawer.change_ranges(float(new_x.text()), float(new_y.text()), float(new_X.text()), float(new_h.text()), True)
        self.static_canvas.close()
        self.static_canvas = FigureCanvas(Figure(figsize=(2, 1)))
        self.reload_widjet()
        self.plot_graphs()

    def plot_graphs(self):
        i = 0
        colors = ['red', 'blue', 'black']
        after_burn = []
        for graph in self.drawer.graphics:
            massive = graph.get_gte()
            if self.checkboxes[i][0].isChecked():
                after_burn.append([graph, colors[i]])

            else:
                self._static_ax.plot(massive[0], massive[1], "white")
            i += 1

        for info in after_burn:
            massive = info[0].get_gte()
            self._static_ax.plot(massive[0], massive[1], info[1])
