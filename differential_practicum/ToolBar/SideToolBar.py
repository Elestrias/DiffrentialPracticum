from differential_practicum.ToolBar.WindowToolBar import WindowToolBar


class SideWindowToolBar(WindowToolBar):
    def __init__(self, window, title):
        super().__init__(window, title)

    def create_side_pannel(self, lte_function, gte_function):
        self.configure_button(["LTE", lte_function, []])
        self.configure_button(["GTE", gte_function, []])
