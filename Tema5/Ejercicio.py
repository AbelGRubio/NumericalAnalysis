from Tema5.SOR import SOR, getomega
import pandas as pd
import numpy as np

def setk1(h: float):
    # return 1 / h + h / 3
    return 1 / h - h / 3


def setk2(h: float):
    # return - 1 / h + h / 6
    return -(1 / h + h / 6)


def setk3(h: float):
    return 2 * setk1(h)


def setf1(h: float):
    return - h ** 2 / 6


def setf2(h: float):
    return - h ** 2 / 3


def setf3(h):
    return setf1(h) + setf2(h)


def setsystem(E: int, range: float = 1):
    h = 1 / E * range
    dia1 = np.ones((E, )) * setk2(h)
    dia = np.ones((E + 1, )) * setk3(h)
    dia[0] = setk1(h)
    dia[E] = setk1(h)
    A = np.diag(dia) + np.diag(dia1, 1) + np.diag(dia1, -1)
    # b = np.ones((E+1, )) * setf3(h)
    # b[0] = setf1(h)
    # b[E] = setf2(h)
    if E == 4:
        b = h ** 2 * np.array([1/6, 1, 2, 3, 11/6])
    else:
        b = h ** 2 * np.array([1 / 6, 1, 2, 3, 4, 5, 6, 7, 23 / 6])
    return [A, b]


def funanal(x):
    return np.sin(x) / np.cos(1) - x


def pltsolanal(E: int=4, range=1):
    import matplotlib.pyplot as plt
    xvals = np.linspace(0, range, E + 1)
    yvals = [funanal(value) for value in xvals]
    E=8
    xvals8 = np.linspace(0, range, E + 1)
    yvals8 = [funanal(value) for value in xvals8]

    plt.plot(xvals, yvals, label='E=4')
    plt.plot(xvals8, yvals8, label='E=8')
    plt.xlabel('X Range')
    plt.ylabel('Y Range')
    plt.legend()
    plt.show()


def phi1(x, h):
    return 1 - x/h


def phiE(x, h):
    return x / h


def phivect(E, x):
    h = 1 / E
    b = np.ones((E+1, ))
    b[0] = phi1(x, h)
    b[E] = phiE(x, h)
    return b


def apartadoA():
    E = 4
    [Matrix, b] = setsystem(E)
    print(np.round(Matrix, 2))
    print(np.round(b, 4))

    subMatrix = Matrix[1:, 1:]
    # subb = np.array([-5/6, 1/2, 1/2, 1/2, 4/3])
    subb = b
    subb = subb[1:]
    values = getomega(subMatrix)
    solucionsis = SOR(subMatrix, subb, values[0])
    resGauss = [0]  # [0]
    for element in solucionsis[0]:
        resGauss.append(element)
    print(resGauss)
    xvals = np.linspace(0, 1, E + 1)
    yvals = [funanal(value) for value in xvals]
    errors = [abs(yanal-ysim) for yanal, ysim in zip(yvals, resGauss)]
    df = pd.DataFrame({'xvalues': xvals, 'Y sim': resGauss, 'Y real': yvals, 'Error': errors})
    print(df)
    foo= 1


def apartadoB():
    E = 8
    [Matrix, b] = setsystem(E)
    print(np.round(Matrix, 2))
    print(np.round(b, 4))

    subMatrix = Matrix[1:, 1:]
    subb = b[1:]
    values = getomega(subMatrix)
    solucionsis = SOR(subMatrix, subb, values[0])
    resGauss = [0]  # [0]
    for element in solucionsis[0]:
        resGauss.append(element)
    xvals = np.linspace(0, 1, E + 1)
    yvals = [funanal(value) for value in xvals]
    errors = [abs(yanal-ysim) for yanal, ysim in zip(yvals, resGauss)]
    df = pd.DataFrame({'xvalues': xvals, 'Y sim': resGauss, 'Y real': yvals, 'Error': errors})
    print(df)


def setsystenCD(E: int=2, intervalo: int=1):

    h = 1 / E * intervalo

    k1 = 7/(3*h) - (2*h)/15
    k3 = k1
    k2 = - 8*(h**2-10)/(15*h)
    k4 = - (h**2+40)/(15*h)
    k6 = k4
    k5 = (h**2+10)/(30*h)

    Anm = np.array([[k1, k4, k5], [k4, k2, k6], [k5, k6, k3]])

    if E == 2:
        b = h**2 * np.array([0, 1/3, 1/3, 1, 1/3])
    else:
        b = h**2 * np.array([0, 1/3, 1/3, 1, 2/3, 5/3, 1, 7/3, 2/3])

    A = np.zeros((2*E+1, 2*E+1))

    positions = np.array(range(3))
    vects = [(positions + val) for val in range(0, 2*E, 2)]

    for vector in vects:
        mina = min(vector)
        maxa = max(vector) + 1
        A[mina:maxa, mina:maxa] += Anm

    return [A, b]


def phi1c(x, h):
    return 1 - x/h


def phiEc(x, h):
    return x / h


def phivectc(E, x):
    h = 1 / E
    b = np.ones((E+1, ))
    b[0] = phi1(x, h)
    b[E] = phiE(x, h)
    return b


def apartadoC():
    E = 2
    [Matrix, b] = setsystenCD(E)
    print(np.round(Matrix, 2))
    print(np.round(b, 4))

    subMatrix = Matrix[1:, 1:]
    subb = b[1:]
    # values = getomega(subMatrix)
    # solucionsis = SOR(subMatrix, subb, values[0])
    solucionsis = np.linalg.solve(subMatrix, subb)
    resGauss = [0]  # [0]
    for element in solucionsis:
        resGauss.append(element)
    xvals = np.linspace(0, 1, 2 * E + 1)
    yvals = [funanal(value) for value in xvals]
    errors = [abs(yanal-ysim) for yanal, ysim in zip(yvals, resGauss)]
    df = pd.DataFrame({'xvalues': xvals, 'Y sim': resGauss, 'Y real': yvals, 'Error': errors})
    print(df)


def apartadoD():
    E = 4
    [Matrix, b] = setsystenCD(E)
    print(np.round(Matrix, 2))
    print(np.round(b, 4))

    subMatrix = Matrix[1:, 1:]
    subb = b[1:]
    # values = getomega(subMatrix)
    # solucionsis = SOR(subMatrix, subb, values[0])
    solucionsis = np.linalg.solve(subMatrix, subb)
    resGauss = [0]  # [0]
    for element in solucionsis:
        resGauss.append(element)
    xvals = np.linspace(0, 1, 2 * E + 1)
    yvals = [funanal(value) for value in xvals]
    errors = [abs(yanal-ysim) for yanal, ysim in zip(yvals, resGauss)]
    df = pd.DataFrame({'xvalues': xvals, 'Y sim': resGauss, 'Y real': yvals, 'Error': errors})
    print(df)


if __name__ == '__main__':
    apartadoA()
    # apartadoB()
    # apartadoC()
    # apartadoD()
    f=1






