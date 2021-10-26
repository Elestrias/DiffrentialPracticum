from abc import ABC
from differential_practicum.NumericMethods.Numeric_Methods import NumericMethods, Function


class EulerMethod(NumericMethods):
    def __init__(self):
        self.aprox = []
        self.lte = []
        self.gte = []
        self.solution = []

    def aproximate_point(self, massive, x0, X, h):
        if X - h >= x0:
            massive[0].append(x0 + h)
            massive[1].append(massive[1][-1] + h * Function.differential(x0, massive[1][-1]))
            self.aproximate_point(massive, x0+h, X, h)
        else:
            self.aprox = massive.copy()
            return massive

    def get_massive(self):
        return self.aprox

    def get_lte(self):
        return self.lte

    def get_gte(self):
        return self.gte