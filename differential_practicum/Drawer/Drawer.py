from differential_practicum.NumericMethods.EulerMethod import EulerMethod
from differential_practicum.NumericMethods.ImporvedEuler import ImprovedEuler
from differential_practicum.NumericMethods.RungeKutta import RungeKutta


class Drawer:
    def __init__(self, x0, y0, X, h, N):
        self.x0 = x0
        self.y0 = y0
        self.X = X
        self.h = h
        self.N = 0
        self.graphics = [EulerMethod(), ImprovedEuler(), RungeKutta()]
        self.draw()
        self.draw_lte()
        self.draw_gte()

    def change_ranges(self, x0, y0, X, h, gte=False):
        self.x0 = x0
        self.X = X
        self.y0 = y0
        if gte:
            self.N = h
            self.h = (X - x0)/h
        else:
            self.h = h
        self.draw()
        self.draw_lte()
        self.draw_gte()

    def add_aproximate_funct(self, function):
        self.graphics.append(function)

    def draw(self):
        for graphic in self.graphics:
            print(graphic)
            massive = [[self.x0], [self.y0]]
            graphic.aproximate_point(massive.copy(), self.x0, self.X, self.h)

    def draw_lte(self):
        for graph in self.graphics:
            massive = [graph.aprox[0], []]
            graph.exact_calc(massive, self.x0, self.y0, self.X, self.h)
            print('massive: ', massive)
            massive = [[self.x0], []]
            graph.calc_lte(massive, graph.solution, graph.aprox)

    def draw_gte(self):
        for graph in self.graphics:
            massive = [[], []]
            graph.calc_gte(massive, self.x0, self.y0, self.X, self.N, graph.solution, graph.aproximate_point)