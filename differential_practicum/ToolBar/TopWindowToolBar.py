from differential_practicum.ToolBar.WindowToolBar import WindowToolBar


class TopWindowToolBar(WindowToolBar):
    def __init__(self, window, title):
        super().__init__(window, title)

    def create_window(self, window, title_text, titles=["x0", "y0", "X", "h"], args=["1", "1", "6", "0.6"]):
        self.configure_label([title_text])
        self.inputs.append(window)
        for i in range(len(titles)):
            self.configure_label([titles[i]])
            self.configure_input(self.inputs, args[i])
        self.configure_button(["apply change", window.change_ranges, self.inputs])
        print("inputs", self.inputs)

