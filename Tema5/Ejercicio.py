from Tema5.SOR import SOR, getomega
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def setk1(h: float):
    return 1 / h - h / 3


def setk2(h: float):
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
    if E == 4:
        b = h ** 2 * np.array([1/6, 1, 2, 3, 11/6])
    else:
        b = h ** 2 * np.array([1 / 6, 1, 2, 3, 4, 5, 6, 7, 23 / 6])
    return [A, b]


def funanal(x):
    return np.sin(x) / np.cos(1) - x


def pltsolanal(E: int=4, range=1):
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


def apartadoA():
    E = 4
    [Matrix, b] = setsystem(E)
    print(np.round(Matrix, 2))
    print(np.round(b, 4))

    subMatrix = Matrix[1:, 1:]
    subb = b
    subb = subb[1:]
    values = getomega(subMatrix)
    values = [value for value in values if not np.isnan(value)]
    solucionsis = SOR(subMatrix, subb, values[0])[0]
    resGauss = [0]  # [0]
    for element in solucionsis:
        resGauss.append(element)
    xvals = np.linspace(0, 1, E + 1)
    yvals = [funanal(value) for value in xvals]
    errors = [abs(yanal-ysim) for yanal, ysim in zip(yvals, resGauss)]
    df = pd.DataFrame({'xvalues': xvals, 'Y sim': resGauss, 'Y real': yvals, 'Error': errors})
    print(df)
    df.to_csv('apartadoA.txt', sep='\t', index=False)
    print('Error apartado A: {}'.format(sum(errors)))
    plt.plot(xvals, yvals, label='Sol. Anal')
    plt.plot(xvals, resGauss, '--', label='Sol. Sim')
    plt.title('Interpolación lineal con 4 elementos finitos')
    plt.xlabel('X Range')
    plt.ylabel('Y Range')
    plt.legend()
    plt.text(0.75, 0.05, 'Error {:.2e}'.format(sum(errors)/len(errors)), bbox=dict(facecolor='red', alpha=0.5))
    plt.savefig('apartadoA.jpeg')
    plt.show()


def apartadoB():
    E = 8
    [Matrix, b] = setsystem(E)
    print(np.round(Matrix, 2))
    print(np.round(b, 4))

    subMatrix = Matrix[1:, 1:]
    subb = b[1:]
    values = getomega(subMatrix)
    values = [value for value in values if not np.isnan(value)]
    solucionsis = SOR(subMatrix, subb, values[0])[0]
    resGauss = [0]  # [0]
    for element in solucionsis:
        resGauss.append(element)
    xvals = np.linspace(0, 1, E + 1)
    yvals = [funanal(value) for value in xvals]
    errors = [abs(yanal-ysim) for yanal, ysim in zip(yvals, resGauss)]
    df = pd.DataFrame({'xvalues': xvals, 'Y sim': resGauss, 'Y real': yvals, 'Error': errors})
    print(df)
    df.to_csv('apartadoB.txt', sep='\t', index=False)
    print('Error apartado B: {}'.format(sum(errors)))
    plt.plot(xvals, yvals, label='Sol. Anal')
    plt.plot(xvals, resGauss, '--', label='Sol. Sim')
    plt.title('Interpolación lineal con 8 elementos finitos')
    plt.xlabel('X Range')
    plt.ylabel('Y Range')
    plt.legend()
    plt.text(0.75, 0.05, 'Error {:.2e}'.format(sum(errors)/len(errors)), bbox=dict(facecolor='red', alpha=0.5))
    plt.savefig('apartadoB.jpeg')
    plt.show()


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


def apartadoC():
    E = 2
    [Matrix, b] = setsystenCD(E)
    print(np.round(Matrix, 2))
    print(np.round(b, 4))

    subMatrix = Matrix[1:, 1:]
    subb = b[1:]
    values = getomega(subMatrix)
    values = [value for value in values if not np.isnan(value)]
    solucionsis = SOR(subMatrix, subb, values[0])[0]
    resGauss = [0]
    for element in solucionsis:
        resGauss.append(element)
    xvals = np.linspace(0, 1, 2 * E + 1)
    yvals = [funanal(value) for value in xvals]
    errors = [abs(yanal-ysim) for yanal, ysim in zip(yvals, resGauss)]
    df = pd.DataFrame({'xvalues': xvals, 'Y sim': resGauss, 'Y real': yvals, 'Error': errors})
    print(df)
    df.to_csv('apartadoC.txt', sep='\t', index=False)
    print('Error apartado C: {}'.format(sum(errors)))
    plt.plot(xvals, yvals, label='Sol. Anal')
    plt.plot(xvals, resGauss, '--', label='Sol. Sim')
    plt.title('Interpolación cuadrática con 2 elementos finitos')
    plt.xlabel('X Range')
    plt.ylabel('Y Range')
    plt.legend()
    plt.text(0.75, 0.05, 'Error {:.2e}'.format(sum(errors)/len(errors)), bbox=dict(facecolor='red', alpha=0.5))
    plt.savefig('apartadoC.jpeg')
    plt.show()


def apartadoD():
    E = 4
    [Matrix, b] = setsystenCD(E)
    print(np.round(Matrix, 2))
    print(np.round(b, 4))

    subMatrix = Matrix[1:, 1:]
    subb = b[1:]
    values = getomega(subMatrix)
    values = [value for value in values if not np.isnan(value)]
    solucionsis = SOR(subMatrix, subb, values[0])[0]
    resGauss = [0]
    for element in solucionsis:
        resGauss.append(element)
    xvals = np.linspace(0, 1, 2 * E + 1)
    yvals = [funanal(value) for value in xvals]
    errors = [abs(yanal-ysim) for yanal, ysim in zip(yvals, resGauss)]
    df = pd.DataFrame({'xvalues': xvals, 'Y sim': resGauss, 'Y real': yvals, 'Error': errors})
    print(df)
    df.to_csv('apartadoD.txt', sep='\t', index=False)
    print('Error apartado D: {}'.format(sum(errors)))
    plt.plot(xvals, yvals, label='Sol. Anal')
    plt.plot(xvals, resGauss, '--', label='Sol. Sim')
    plt.title('Interpolación cuadrática con 4 elementos finitos')
    plt.xlabel('X Range')
    plt.ylabel('Y Range')
    plt.legend()
    plt.text(0.75, 0.05, 'Error {:.2e}'.format(sum(errors)/len(errors)), bbox=dict(facecolor='red', alpha=0.5))
    plt.savefig('apartadoD.jpeg')
    plt.show()


if __name__ == '__main__':

    print('Apartado A')
    apartadoA()
    print('\n\nApartado B')
    apartadoB()
    print('\n\nApartado C')
    apartadoC()
    print('\n\nApartado D')
    apartadoD()
    f=1






