from Tema3.GS import GaussSeidelIterative
from Tema3.J import JacobiIterative
from Tema3.SOR import SOR
import numpy as np


def sumFact(T1: int, T0: int, k, rho: float, theta: float):
    """

    :param T1:
    :param T0:
    :param k:
    :param rho:
    :param theta: tiene que estar en radianes

    :return:
    """
    return (T1 - T0)/((2*k+1)*np.pi)*rho**(2*k+1)*np.sin((2*k+1)*theta)


def sumatorio(T1: int, T0: int, theta: float, rho: float, npoints: int = 1500):
    """

    :param T1:
    :param T0:
    :param theta:
    :param rho:
    :param npoints:
    :return:
    """
    return sum([sumFact(T1, T0, val, rho, theta) for val in range(npoints)])


def solAnalitica(T1: int, T0: int, deltaRho: int = 3, deltaTheta: int = 6):
    rhos = [rh/deltaRho for rh in range(deltaRho-1, 0, -1)]

    deltatheta = 1 / deltaTheta
    thetas = [deltatheta * factor for factor in range(1, int(deltaTheta/2) +1)]

    us = []
    idx = 1
    for theta in thetas:
        for rho in rhos:
            point = T0 + 4 * sumatorio(T1=T1, T0=T0, theta=np.pi * theta, rho=rho)
            us.append(point)
            # print("Punto {} en ({:.3f},{:.3f}\u03C0):\t {:.3f}º".format(idx, rho, theta, point))
            idx += 1
    return us


def solAnaliticaCarte(T1: int, T0: int, deltaRho: int = 3):
    rhosy = [rh/deltaRho for rh in range(deltaRho-1, 0, -1)]
    rhosx = [rh/deltaRho for rh in range(deltaRho)]

    us = []
    idx = 1
    for y in rhosy:
        for x in rhosx:
            try:
                theta = np.arctan(y/x)
            except ZeroDivisionError:
                theta = np.pi/2
            rho = np.sqrt(x**2+y**2)
            point = T0 + 4 * sumatorio(T1=T1, T0=T0, theta=theta, rho=rho)
            us.append(point)
            print("Punto {} en ({:.3f},{:.3f}):\t {:.3f}º".format(idx, rho, theta, point))
            idx += 1
    return us


def fracPi2(number):
    """
    Esta funcion devuelve el valor de
    ..math:
        number/pi^2

    :parameter number:
    :return:
    """
    return number/np.pi**2


def diagonalVal(number):
    """
    Esta funcion devuelve el valor de la diagonal
    ..math:
        -2 * (1 + number/pi^2)

    :param number:
    :return:
    """
    return -2 * (1 + fracPi2(number))


def generaDiagonal(caso):
    """
    Genera los elementos de la diagonal
    :parameter caso
    :return:
    """
    numbers = [9, 36]
    values = numbers * caso
    return [diagonalVal(number) for number in values]


def generaDiagonalSup1(caso):
    """
    Genera los elementos de la diagonal superior n=1
    :parameter caso
    :return:
    """
    vals = [1, 0]
    values = vals * caso
    values = values[:-1]
    return [3/4*val for val in values]


def generaDiagonalInf1(caso):
    """
    Genera los elementos de la diagonal inferior n=1
    :parameter caso:
    :return:
    """
    vals = [1, 0]
    values = vals * caso
    values = values[:-1]
    return [3/2*val for val in values]


def generaDiagonalSup2(caso):
    """
    Genera los elementos de la diagonal superior n=1
    :parameter caso
    :return:
    """
    vals = [9, 36]
    values = vals * (caso - 1)
    return [fracPi2(val) for val in values]


def generaDiagonalInf2(caso):
    """
    Genera los elementos de la diagonal inferior n=1
    :parameter caso:
    :return:
    """
    vals = [9, 36]
    values = vals * (caso - 1)
    vals2 = [fracPi2(val) for val in values]
    mults = [1, 1] * (caso - 1)
    if caso == 3:
        mults = [1, 1, 2, 2]
    return [val * mult for val, mult in zip(vals2, mults)]


def generaMatrix(caso):
    """
    Genera la matriz del problema
    :parameter caso:
    :return:
    """
    return np.diag(generaDiagonal(caso)) + np.diag(generaDiagonalSup1(caso), 1) + \
           np.diag(generaDiagonalInf1(caso), -1) + \
           np.diag(generaDiagonalSup2(caso), 2) + np.diag(generaDiagonalInf2(caso), -2)


def generab(T1: int, T0: int, caso: int):
    """

    :parameter T1:
    :parameter T0:
    :parameter caso:
    :return:
    """
    factor = 5/4 * (T0 - T1)
    vect = [1, 0] * caso
    return [factor * val for val in vect]


def fracPi2v2(number, i):
    """
    Esta funcion devuelve el valor de
    ..math:
        number/pi^2

    :parameter number:
    :return:
    """
    return 1/(i*np.pi/number)**2


def diagonalValv2(number, i):
    """
    Esta funcion devuelve el valor de la diagonal
    ..math:
        -2 * (1 + number/pi^2)

    :param number:
    :return:
    """
    return -2 * (1 + fracPi2v2(number, i))


def fracIzq(i):
    return 1 - 1 / (2*i)


def fracDech(i):
    return 1 + 1 / (2*i)


def generaMatrixAConvergencia(deltaTheta: int, deltaRho: int):
    """

    :parameter deltaTheta: numero entero que indica en cuantas partes hay que dividir pi
    :parameter deltaRho: numero entero que indica en cuantas partes hay que dividir rho

    :return:
    """
    rhosfrac = range(deltaRho-1, 0, -1)
    rep2Theta = int(deltaTheta/2)
    diag = [diagonalValv2(deltaTheta, num) for num in rhosfrac] * rep2Theta
    diag1 = ([fracIzq(num) if num % 2 == 0 else 0 for num in rhosfrac] * rep2Theta)[:-1]
    diagminus1 = ([fracDech(num) if num % 2 != 0 else 0 for num in rhosfrac] * rep2Theta)[1:]
    diag2 = [fracPi2v2(deltaTheta, num) for num in rhosfrac] * (rep2Theta-1)
    mult = [1 if num < (len(diag2)-len(rhosfrac)) else 2 for num in range(len(diag2))]
    diagminus2 = [num1 * num2 for num1, num2 in zip(diag2, mult)]
    return np.diag(diag) + np.diag(diag1, 1) + np.diag(diag2, 2) + np.diag(diagminus1, -1) + np.diag(diagminus2, -2)


def generaMatrixbConvergencia(deltaTheta: int, deltaRho: int, T1, T0):
    rhosfrac = range(deltaRho-1, 0, -1)
    valTemp = fracDech(deltaRho - 1) * (T0 - T1)
    rep2Theta = int(deltaTheta/2)
    return [valTemp if num % 2 == 0 else 0 for num in rhosfrac] * rep2Theta


def getomega(Matrix: np.ndarray):
    """
    Obtiene el coeficiente de sobrerelajacion
    :param Matrix:
    :return:
    """
    Dinv = np.diag(1 / Matrix.diagonal())
    L = - np.tril(Matrix) + np.diag(Matrix.diagonal())
    U = - np.triu(Matrix) + np.diag(Matrix.diagonal())
    T = np.dot(Dinv, (L + U))
    eigenvalues, eigenvectors = np.linalg.eig(T)

    return [2 / (1+np.sqrt(1-abs(val)**2)) if val < 1 else 0 for val in eigenvalues]


def apartadoC():
    print("\n\nAsumiendo la simetria de los puntos ")
    Matrixv2 = generaMatrix(3)
    Bv2 = generab(100, 50, 3)
    print("Los valores de sobrerrelajación es: ")
    values = getomega(Matrixv2)
    print(values[0])
    print("\nResultado utilizando el método de \nsobrerelajación con omega= {:.3f}".format(values[0]))
    TempGauss = SOR(Matrixv2, Bv2, values[0])
    # for num, val in enumerate(TempGauss[0]):
    #     print("Punto {} Temp {:.3f}".format(num + 1, val + 50))
    rhos = [2/3, 1/3]
    deltatheta = 1 / 6
    thetas = [deltatheta * factor for factor in range(1, 4)]

    Temperaturas = TempGauss[0]
    idx = 1
    for theta in thetas:
        for rho in rhos:
            print("Punto {} en ({:.3f},{:.3f}\u03C0):\t {:.3f}º".format(idx, rho, theta, Temperaturas[idx-1]+50))
            idx += 1

    print("\n\nSolucion analitica es: ")
    temps = solAnalitica(100, 50)

    error = sum([abs(anal-(gaus+50)) for anal, gaus in zip(temps, Temperaturas)])
    print("\n\nEl error es de: {:.3f}".format(error/len(Temperaturas)))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\n\n\nSin asumir la simetria de los puntos")
    Matrixv2 = generaMatrix(5)
    Bv2 = generab(100, 50, 5)
    print("Los valores de sobrerrelajación es: ")
    values = getomega(Matrixv2)
    print(values)
    print("\nResultado utilizando el método de \nsobrerelajación con omega= {:.3f}".format(values[0]))
    TempGauss = SOR(Matrixv2, Bv2, values[0])
    Temperaturas = TempGauss[0]
    idx = 1
    thetas = [deltatheta * factor for factor in range(1, 6)]
    for theta in thetas:
        for rho in rhos:
            print("Punto {} en ({:.3f},{:.3f}\u03C0):\t {:.3f}º".format(idx, rho, theta, Temperaturas[idx-1]+50))
            idx += 1
    error = sum([abs(anal-(gaus+50)) for anal, gaus in zip(temps, Temperaturas)])
    print("\n\nEl error es de: {:.3f}".format(error/len(Temperaturas)))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    # convergencia del algoritmo
    ranges = [1, 2, 4, 6, 8]
    errors = []
    for n in ranges:
        AA = generaMatrixAConvergencia(n * 6, 3)
        bb = generaMatrixbConvergencia(n * 6, 3, 100, 50)
        omegas = getomega(AA)
        TempGauss = SOR(AA, bb, omegas[0])
        Temperaturas = TempGauss[0]
        temps = np.array(solAnalitica(100, 50, deltaRho=3, deltaTheta=n * 6))
        error = sum([abs(anal-(gaus+50)) for anal, gaus in zip(temps, Temperaturas)])
        errors.append(error/len(Temperaturas))
    print(errors)
    import matplotlib.pyplot as plt
    xvals = [6 * val for val in ranges]
    errors2 = errors
    xvals2 = xvals
    plt.figure(2)
    plt.plot((xvals2), (errors2))
    plt.xlabel("Número de puntos")
    plt.ylabel("Error medio absoluto")
    plt.show()


def GeneraMatrixD():
    diagonal = [-2, - (1 + 1/(2*(np.sqrt(2) - 1))), -2 / (np.sqrt(5) - 2),
                -2, -2, - (1 + 1/(2*(np.sqrt(2) - 1)))]
    diagonalsup1 = [1, 1/2, 0, 1, 1/2]
    diagonalsup3 = [1, 1 / (2 * np.sqrt(2) - 1), 1 / (np.sqrt(5) - 1)]
    diagonalinf1 = [1/2, 1 / (np.sqrt(5) - 1), 0, 1/2, 1 / (2 * np.sqrt(2) - 1)]
    diagonalinf3 = [1/2, 1/2, 1/2]
    return np.diag(diagonal) + np.diag(diagonalinf1, -1) + np.diag(diagonalsup1, 1) + \
           np.diag(diagonalinf3, -3) + np.diag(diagonalsup3, 3)


def generaBMatrixD(T1: int, T0: int):
    vals = [1/2, 1 / ((2 * np.sqrt(2) - 1) * 2 * (np.sqrt(2) - 1)), 2 / ((np.sqrt(5) - 1) * (np.sqrt(5) - 2)),
            0, 0, 1 / ((2 * np.sqrt(2) - 1) * 2 * (np.sqrt(2) - 1))]
    return (T0 - T1) * np.array(vals)


def apartadoD():
    matrixA = GeneraMatrixD()
    b = generaBMatrixD(100, 50)

    print("Los valores de sobrerrelajacion es: ")
    values = getomega(matrixA)
    print(values)
    print("\nResultado utilizando el método de \nsobrerelajación con omega= {:.3f}".format(values[0]))
    TempGauss = SOR(matrixA, b, values[0])
    for num, val in enumerate(TempGauss[0]):
        print("Punto {}: {:.3f}º".format(num + 1, val + 50))

    print("\n\bLa solución analitica al problema es: ")
    temps = solAnaliticaCarte(100, 50)
    Temperaturas = TempGauss[0]
    error = sum([abs(anal - (gaus + 50)) for anal, gaus in zip(temps, Temperaturas)])
    print("\n\nEl error es de: {:.3f}".format(error/len(Temperaturas)))


if __name__ == '__main__':
    apartadoC()
    # apartadoD()



