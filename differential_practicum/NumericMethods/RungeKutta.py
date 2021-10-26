from differential_practicum.NumericMethods.Numeric_Methods import NumericMethods, Function


class RungeKutta(NumericMethods):
    def __init__(self):
        self.aprox = []
        self.lte = []
        self.gte = []
        self.solution = []


    def aproximate_point(self, massive, x0, X, h):
        if X - h >= x0:
            k1 = Function.differential(x0, massive[1][-1])
            k2 = Function.differential(x0 + (h/2), massive[1][-1] + (h/2)*k1)
            k3 = Function.differential(x0 + (h/2), massive[1][-1] + (h/2)*k2)
            k4 = Function.differential(x0 + h, massive[1][-1] + h*k3)
            massive[1].append(massive[1][-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4))
            massive[0].append(x0 + h)
            self.aproximate_point(massive, x0 + h, X, h)
        else:
            self.aprox = massive.copy()


    def get_massive(self):
        return self.aprox

    def get_lte(self):
        return self.lte

    def get_gte(self):
        return self.gte
