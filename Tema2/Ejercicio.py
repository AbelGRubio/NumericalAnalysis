
from Tema2 import *
# from .QR import QRMethod
# from .PowerMethod import PowerMethod
from Tema2.HH import HouseHolderMethod
import numpy as np


def apartadoC():
    """
    :return:
    """
    n = 10
    a = -2 * np.ones(n)
    b = np.ones(n-1)
    res = QRMethod(a, b)
    print("Los modos normales en términos de \omega son: ")
    print(np.sort(res))


def apartadoD():
    """
    :return:
    """
    n = 10
    a = -2 * np.ones(n)
    b = np.ones(n - 1)
    print(PowerMethod(a, b))

    for i in range(1, n):
        print("Componente no nula en posicion ", str(i))
        x0 = np.zeros_like(a)
        x0[i] = 1
        print(PowerMethod(a, b, x0))
        print("\n\n")
    print("-----")


def apartadoE():
    """
    :return:
    """
    P = np.eye(n)
    for j in range(1, n, 2):
        P[j, j] = 10

    print("La matriz de transfomraciones es: ")
    print(P)

    print("Matrix tranformada")
    print(np.round(np.dot(P, A), 2))


def apartadoF():
    """
    :return:
    """
    pass


if __name__ == '__main__':
    apartadoD()
    n = 10
    a = -2 * np.ones(n)
    bu = np.ones(n - 1)
    bd = np.ones(n-1)
    for i in range(1, n, 2):
        a[i] = a[i] / 10
        if i == 9:
            bd[i-1] = bd[i-1] / 10
            break
        bu[i] = bu[i] / 10
        bd[i - 1] = bd[i - 1] / 10
    A = np.diag(a) + np.diag(bu, 1) + np.diag(bd, -1)
    print(A)
    P = np.eye(n)
    for j in range(1, n, 2):
        P[j, j] = 10

    print("La matriz de transfomraciones es: ")
    print(P)

    print("Matrix tranformada")
    print(np.round(np.dot(P, A), 2))

    # apartadoD()
    # # A = [[1, 2, 3], [2, 8, 9], [3, 9, 5]]
    # # A = [[1, 7, 3], [7, 4, -5], [3, -5, 6]]
    # A = [[4, 1, -2, 2], [1, 2, 0, 1], [-2, 0, 3, -2], [2, 1, -2, -1]]
    # Anp = np.array(A)
    # print("la matriz original es: ")
    # print(Anp)
    #
    # print("la matriz reducida es")
    # HouseHolderMethod(Anp)
    # print("Final")