from differential_practicum.MainWindows.MainWindow import *


class Application(MainWindow):
    def reload_widjet(self):
        self.layout.addWidget(self.static_canvas)
        self._static_ax = self.static_canvas.figure.subplots()

    def plot_graphs(self):
        i = 0
        colors = ['red', 'blue', 'black']
        after_burn = []
        for graph in self.drawer.graphics:
            massive = graph.get_massive()
            if self.checkboxes[i][0].isChecked():
                after_burn.append([graph, colors[i]])

            else:
                self._static_ax.plot(massive[0], massive[1], "white")
            i += 1

        for info in after_burn:
            massive = info[0].get_massive()
            self._static_ax.plot(massive[0], massive[1], info[1])

    def __init__(self):
        super().__init__()
        self.tool_bar.create_window(self, "APROX GRAPHS:")

        self.side.configure_button(["go to lte", self.go_first, [self.first]])
        self.side.configure_button(["go to gte", self.go_second, [self.second]])

        self.plot_graphs()






