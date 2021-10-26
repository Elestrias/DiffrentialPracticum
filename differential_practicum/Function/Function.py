from math import exp, sqrt


class Function:

    @staticmethod
    def differential(x, y):
        calc = lambda x, y: (2 - y ** 2) / (2 * (x ** 2) * y)
        return calc(x, y)

    @staticmethod
    def function(x, y):
        calc = lambda x, y: (2 - y ** 2) / (2 * x ** 2 * y)
        return calc(x, y)  # TODO normal function

    @staticmethod
    def solution(x, y):
        sol = lambda x, c: sqrt(c * exp(1 / x) + 2)
        return sol(x, y)

    @staticmethod
    def CFinder(x, y):
        findC = lambda x, y: (y ** 2 - 2) / exp(1 / x)
        return findC(x, y)