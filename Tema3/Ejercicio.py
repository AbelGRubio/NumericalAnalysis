from Tema3.GS import GaussSeidelIterative
from Tema3.J import JacobiIterative
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


def sumatorio(T1: int, T0: int, theta: float, rho: float, npoints: int = 800):
    """

    :param T1:
    :param T0:
    :param theta:
    :param rho:
    :param npoints:
    :return:
    """
    return sum([sumFact(T1, T0, val, rho, theta) for val in range(npoints)])


def solAnalitica(T1: int, T0: int):
    rhos = [1/3, 2/3]
    deltatheta = np.pi / 6
    thetas = [deltatheta * factor for factor in range(1, 6)]

    us = []
    for theta in thetas:
        for rho in rhos:
            point = T0 + 4 * sumatorio(T1=T1, T0=T0, theta=theta, rho=rho)
            us.append(point)
            print("{:.3f}".format(point))
    # print(us)


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


# def generaDiagonal():
#     """
#     Genera los elementos de la diagonal
#     :return:
#     """
#     numbers = [9, 36, 9, 36, 9, 36]
#     return [diagonalVal(number) for number in numbers]
#
#
# def generaDiagonalSup1():
#     """
#     Genera los elementos de la diagonal superior n=1
#     :return:
#     """
#     vals = [1, 0, 1, 0, 1]
#     return [3/4*val for val in vals]
#
# def generaDiagonalInf1():
#     """
#     Genera los elementos de la diagonal inferior n=1
#     :return:
#     """
#     vals = [1, 0, 1, 0, 1]
#     return [3/2*val for val in vals]
# def generaDiagonalSup2():
#     """
#     Genera los elementos de la diagonal superior n=1
#     :return:
#     """
#     vals = [9, 36, 9, 36]
#     return [fracPi2(val) for val in vals]
# def generaDiagonalInf2():
#     """
#     Genera los elementos de la diagonal inferior n=1
#     :return:
#     """
#     vals = [9, 36, 9, 36]
#     vals2 = [fracPi2(val) for val in vals]
#     mults = [1, 1, 2, 2]
#     return [val * mult for val, mult in zip(vals2, mults)]
#
# def generaMatrix():
#     """
#     Genera la matriz del problema
#     :return:
#     """
#     return np.diag(generaDiagonal()) + np.diag(generaDiagonalSup1(), 1) + np.diag(generaDiagonalInf1(), -1) + \
#            np.diag(generaDiagonalSup2(), 2) + np.diag(generaDiagonalInf2(), -2)
#
# def generab(T1: int, T0: int):
#     """
#
#     :parameter T1:
#     :parameter T0:
#     :return:
#     """
#     factor = 5/4 * (T0 - T1)
#     vect = [1, 0, 1, 0, 1, 0]
#     return [factor * val for val in vect]
def generaDiagonalv2(caso):
    """
    Genera los elementos de la diagonal
    :parameter caso
    :return:
    """
    numbers = [9, 36]
    values = numbers * caso
    return [diagonalVal(number) for number in values]


def generaDiagonalSup1v2(caso):
    """
    Genera los elementos de la diagonal superior n=1
    :parameter caso
    :return:
    """
    vals = [1, 0]
    values = vals * caso
    values = values[:-1]
    return [3/4*val for val in values]


def generaDiagonalInf1v2(caso):
    """
    Genera los elementos de la diagonal inferior n=1
    :parameter caso:
    :return:
    """
    vals = [1, 0]
    values = vals * caso
    values = values[:-1]
    return [3/2*val for val in values]


def generaDiagonalSup2v2(caso):
    """
    Genera los elementos de la diagonal superior n=1
    :parameter caso
    :return:
    """
    vals = [9, 36]
    values = vals * (caso - 1)
    return [fracPi2(val) for val in values]


def generaDiagonalInf2v2(caso):
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


def generaMatrixv2(caso):
    """
    Genera la matriz del problema
    :parameter caso:
    :return:
    """
    return np.diag(generaDiagonalv2(caso)) + np.diag(generaDiagonalSup1v2(caso), 1) + \
           np.diag(generaDiagonalInf1v2(caso), -1) + \
           np.diag(generaDiagonalSup2v2(caso), 2) + np.diag(generaDiagonalInf2v2(caso), -2)


def generabv2(T1: int, T0: int, caso: int):
    """

    :parameter T1:
    :parameter T0:
    :parameter caso:
    :return:
    """
    factor = 5/4 * (T0 - T1)
    vect = [1, 0] * caso
    return [factor * val for val in vect]


def apartadoC():
    print("\n\nAsumiendo la simetria de los puntos ")
    Matrixv2 = generaMatrixv2(3)
    Bv2 = generabv2(100, 50, 3)
    # print("\n\nMediante el método Jacobi")
    # TempJacobi = JacobiIterative(Matrixv2, Bv2)
    # for num, val in enumerate(TempJacobi[0]):
    #     print("Punto {} Temp {}".format(num + 1, val + 50))
    print("Mediante el método Gauss-Seidel")
    TempGauss = GaussSeidelIterative(Matrixv2, Bv2)
    for num, val in enumerate(TempGauss[0]):
        print("Punto {} Temp {:.3f}".format(num + 1, val + 50))

    # print("\n\nSin asumir la simetria de los puntos")
    # Matrixv2 = generaMatrixv2(5)
    # Bv2 = generabv2(100, 50, 5)
    # # print("\n\nMediante el método Jacobi")
    # # TempJacobi = JacobiIterative(Matrixv2, Bv2)
    # # for num, val in enumerate(TempJacobi[0]):
    # #     print("Punto {} Temp {}".format(num + 1, val + 50))
    # print("Mediante el método Gauss-Seidel")
    # TempGauss = GaussSeidelIterative(Matrixv2, Bv2)
    # for num, val in enumerate(TempGauss[0]):
    #     print("Punto {} Temp {:.3f}".format(num + 1, val + 50))


if __name__ == '__main__':
    apartadoC()
    print("La solucion analitica del problema es: ")
    solAnalitica(100, 50)


