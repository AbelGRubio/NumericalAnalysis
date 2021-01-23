import matplotlib.pyplot as plt
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


def ejercicio(L: int = 1, mx: int = 20, mt: int = 100, D: int = 1, C: int = 0):
    A = getMatrix(L, mx, mt, D, C)
    deltat = (L/2) / mt
    t = np.linspace(0, L/2, mt + 1)
    deltax = L / mx

    condicion = 4 * D * deltat / (deltax ** 2) - C * deltat
    estable = 2 >= condicion >= 0
    print("Los resultados son estables? respuesta {} value {}".format(estable, condicion))

    x = np.linspace(-L/2, L/2, mx + 1)
    xvals = np.array([delta(deltax, xval) for xval in x])

    dnmedio = []
    i = 0
    for tv in t:
        print('Para el tiempo {:.2f} - {} con el valor es {:.4f} '.format(tv, i, sum(xvals) * deltax))
        xvals = A @ xvals
        xvals[0] = 0
        xvals[len(xvals)-1] = 0
        dnmedio.append(sum(xvals) * deltax)
        i += 1
    print(xvals)
    plt.figure(1)
    plt.plot(t, dnmedio)
    plt.ylabel("Densidad promedio de neutrones [m^-1]")
    plt.xlabel("Tiempo [s]")
    plt.show()
    plt.figure(2)
    plt.plot(x, xvals)
    plt.ylabel("Densidad de neutrones [m^-1]")
    plt.xlabel("Distancia [m]")
    plt.show()


def cambio(L: int = 1, D: int = 1):

    nbar = lambda C, t: np.exp((C - D*np.pi**2/(L**2))*t)
    t = np.arange(0, L/2, 0.01)
    cambio = D * (np.pi ** 2) / (L ** 2)
    Cvalues = [cambio * 1.001, cambio, cambio * 0.999]
    res = []
    plt.figure(1)
    for cval in Cvalues:
        nbarvals = nbar(cval, t)
        res.append(nbarvals)
        plt.plot(t, nbarvals)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Densidad promedio [m^-1]")
    names = ['Explota', 'Limite de cambio', 'Acotada']
    labels = ['{} {:.3f}'.format(nm, cval) for cval, nm in zip(Cvalues, names)]
    plt.legend(labels)
    plt.show()

    pctg = 0.4
    Cvalues = [cambio * (1+pctg), cambio, cambio * (1-pctg)]
    res = []
    plt.figure(2)
    for cval in Cvalues:
        nbarvals = nbar(cval, t)
        res.append(nbarvals)
        plt.plot(t, nbarvals)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Densidad promedio [m^-1]")
    names = ['Explota', 'Limite de cambio', 'Acotada']
    labels = ['{} {:.3f}'.format(nm, cval) for cval, nm in zip(Cvalues, names)]
    plt.legend(labels)
    plt.show()


def solucionAnalitica(L: int = 1, mx: int = 10, mt: int = 1000, D: int = 1, C: int = 0):
    """

    :param L:
    :param mx:
    :param mt:
    :param D:
    :param C:
    :return:
    """
    Tn = lambda n, t: np.exp((C - D * ((2*n+1) * np.pi / L) ** 2) * t)
    Xn = lambda n, x: np.cos(((2*n+1) * np.pi / L) * x)
    Nn = lambda n, x, t: Tn(n, t) * Xn(n, x)

    nvalues = np.array(range(1, 1000))
    Tiempo = np.linspace(0, L / 2, mt + 1)
    x = np.linspace(-L/2, L/2, mx + 1)

    ave = []
    for t in Tiempo:
        solucion = [sum(Nn(nvalues, xval, t))/len(nvalues) for xval in x]
        ave.append(sum(solucion))
    ave = np.array(ave)
    plt.plot(ave)


if __name__ == '__main__':
    ejercicio()
    # cambio(1, 1)
    # solucionAnalitica()
