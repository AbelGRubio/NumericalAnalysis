import numpy as np


def val1(deltat, deltax, D: int = 1):
    return deltat * D / (deltax ** 2)


def val2(deltat, deltax, D: int = 1, C: int = 0):
    return C * deltat + 1 - 2 * val1(deltat, deltax, D)


def getMatrix(L: int = 1, mx: int = 5, mt: int = 5, D: int = 1, C: int = 0):
    deltat = (L/2) / mt
    deltax = L / mx
    diag = [val2(deltat, deltax, D, C) for _ in range(mx+1)]
    diag1 = [val1(deltat, deltax, D) for _ in range(mx)]
    return np.diag(diag) + np.diag(diag1, 1) + np.diag(diag1, -1)


def delta(deltax, x):
    val = 1 / deltax if x == 0 else (deltax + x) / (deltax ** 2) if -deltax < x < 0 else (deltax - x) / (deltax ** 2)
    return val if -deltax < x < deltax else 0


# h es el espacio 0.1 ---  k es el tiempo  0.0005
def ejercicio(L: int = 1, mx: int = 10, mt: int = 1000, D: int = 1, C: int = 0):
    A = getMatrix(L, mx, mt, D, C)
    deltat = (L/2) / mt
    t = np.linspace(0, L/2, mt + 1)
    deltax = L / mx
    x = np.linspace(-L/2, L/2, mx + 1)
    xvals = np.array([delta(deltax, xval) for xval in x])
    # xvals = np.array([np.sin(np.pi * xval) for xval in x])
    print(xvals)
    print(sum(xvals * deltax))
    import matplotlib.pyplot as plt
    # plt.plot(xvals)

    dnmedio = []
    i = 0
    for tv in t:
        print('Para el tiempo {:.2f} - {} con el valor es {:.4f} '.format(tv, i, sum(xvals) * deltax))
        xvals = A @ xvals
        xvals[0] = 0
        xvals[len(xvals)-1] = 0
        dnmedio.append(sum(xvals) * deltax)
        # plt.plot(xvals)
        i += 1
    print(xvals)
    # plt.show()
    plt.figure(1)
    plt.plot(t, dnmedio)
    plt.ylabel("Densidad promedio de neutrones")
    plt.xlabel("Tiempo ")


if __name__ == '__main__':
    ejercicio()
