import sys

from differential_practicum.MainWindows.Application import *
from differential_practicum.MainWindows.lteWindow import *
from differential_practicum.MainWindows.gteWindow import *


def window_switch(A, B, C):
    A.setup_first(B)
    A.setup_second(C)
    B.setup_first(A)
    B.setup_second(C)
    C.setup_first(A)
    C.setup_second(B)


if __name__ == "__main__":
    sys.setrecursionlimit(6000)
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    aprox = Application()
    lte = lteWindow()
    gte = gteWindow()
    window_switch(aprox, lte, gte)
    aprox.show()
    aprox.activateWindow()
    aprox.raise_()
    qapp.exec_()