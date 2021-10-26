from abc import abstractmethod
from differential_practicum.Function.Function import Function


class NumericMethods:
    @abstractmethod
    def aproximate_point(self, massive, x0, X, h):
        pass

    def get_massive(self):
        pass

    def exact_calc(self, massive, x0, y0, X, h):
        i = x0
        j = 0
        while X >= i:
            print(j)
            massive[1].append(Function.solution(massive[0][j], Function.CFinder(x0, y0)))
            i += h
            j += 1
        self.solution = massive.copy()
        print("solution", self.solution[0])

    def calc_lte(self, result, massive_exact, massive_aprox):
        print("!!!!!!!!!!!!!!!!!")
        print(massive_exact[1])
        print(massive_aprox[1])
        for i in range(len(massive_aprox[0])):
            result[1].append(abs(massive_exact[1][i] - massive_aprox[1][i]))
        result[0] = massive_exact[0].copy()
        self.lte = result.copy()
        return result

    def calc_gte(self, massive, x0, y, X, N, solution, aproximate_func):
        for j in range(1, 1 + int(N)):
            massive[0].append(j)
            massiveer = [[x0], [y]]
            aproximate_func(massiveer, x0, X, (X-x0)/j)
            print(massiveer)
            massive[1].append(max(self.calc_lte([[x0], []], solution, massiveer)[1]))
        self.gte = massive.copy()

