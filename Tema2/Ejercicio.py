
from Tema2 import *
from Tema2.WD import *
# from .QR import QRMethod
# from .PowerMethod import PowerMethod
from Tema2.HH import HouseHolderMethod, GeneralizedHouseHolderMethod
import pandas as pd
import numpy as np


def apartadoC():
    """
    :return:
    """
    n = 10
    a = -2 * np.ones(n)
    b = np.ones(n-1)
    res = QRMethod(a, b)
    print(r"Los modos normales en términos de \omega_0 son: ")
    # res2 = [element for element in res]
    res2 = np.sort(res)
    res3 = ((np.sqrt(-res2)).transpose())
    print("Autovalores \t Modos normales en términos de \omega_0")
    for e1, e2 in zip(res2, res3):
        print(e1, "\t\t\t", e2 * 1j)


def apartadoD():
    """
    :return:
    """
    np.random.seed(10)
    n = 10
    a = -2 * np.ones(n)
    b = np.ones(n - 1)
    A = np.diag(a) + np.diag(b, 1) + np.diag(b, -1)
    for i in range(0, n):
        print("Componente no nula en posicion ", str(i))
        # x0 = np.zeros_like(a)
        # x0[i] = 1
        x0 = np.random.random(10)
        x0 /= max(x0)
        res = PowerMethod(a, b, x0)
        print("Autovalor y autovector predominante")
        print(res)
        print("Modo normal en términos de omega_0")
        print(np.sqrt(-res[0]))
        print("\n\n")
    print("-----")
    # i = 1
    # x0 = np.zeros_like(a)
    # x0[i] = 1
    # res = PowerMethod(a, b, x0)
    # print("El autovalor y autovector predominante es:")
    # print(res)

    # np.random.seed(45)
    # Awd = A.copy()
    # eigenvaluewd = res[0]
    # eigenvectorwd = res[1]
    # for dp in range(1, n-1):
    #     x0 = np.random.random(n-1)
    #     x0 /= max(x0)
    #     reswd = (WielandtDeflaction(Awd, eigenvaluewd, eigenvectorwd, x0))
    #     eigenvalues.append(reswd[0])
    #     # Awd = reswd[2].copy()
    #     eigenvaluewd = reswd[0]
    #     eigenvectorwd = reswd[1]
    # print(eigenvalues)
    # modes = [np.sqrt(-md) for md in eigenvalues]
    # print(modes)
    # print(np.sqrt(-reswd[0]))


def apartadoE():
    """
    :return:
    """
    N = 10
    a = -2 * np.ones(N)
    bu = np.ones(N - 1)
    bd = np.ones(N-1)
    for i in range(1, N, 2):
        a[i] = a[i] / 10
        if i == 9:
            bd[i-1] = bd[i-1] / 10
            break
        bu[i] = bu[i] / 10
        bd[i - 1] = bd[i - 1] / 10
    A = np.diag(a) + np.diag(bu, 1) + np.diag(bd, -1)
    np.random.seed(10)
    x0 = np.random.random(10)
    x0 /= max(x0)
    resp = PowerMethod(A, x0)
    print("Autovalor y autovector predominante")
    print(resp)
    print("Modo normal en términos de omega_0")
    print(np.sqrt(-resp[0]))

    print("La matriz de entrada es")
    print(A)
    res = (np.round(GeneralizedQRMethod(A), 2))
    print("La matriz de salida es")
    print(res)


def apartadoF():
    """
    :return:
    """
    N = 10
    np.random.seed(50)
    A = np.random.randint(-20, 20, size=(N, N))
    Asym = ((A + A.T) / 2).astype(int)
    # print("La matriz simétrica introducida es: ")
    # print(Asym)
    res = GeneralizedQRMethod(Asym)
    print("Los autovalores de la matriz simétrica: ")
    print(np.sort(res))

    # x0 = np.zeros((N,))
    # x0[1] = 1
    # print("----------------------------")
    # print("Maximo autovalor utilizando el método de la potencia")
    # res = PowerMethod(Asym, x0)
    # print("El autovalor y autovector son")
    # print(res)

    # for i in range(1, N):
    #     print("Componente no nula en posicion ", str(i))
    #     x0 = np.zeros((10, ))
    #     x0[i] = 1
    #     print(PowerMethod(Asym, x0))
    #     print("\n\n")
    print("-----")


def realw():
    import math
    N = 10
    for i in range(1, N+1):
        print(2*math.sin((i*math.pi/(2*(N+1)))))
    print("------------")


if __name__ == '__main__':
    print("-------------  Apartado C")
    # apartadoC()
    print("-------------  Apartado D")
    # apartadoD()
    print("-------------  Apartado E")
    # apartadoE()
    print("-------------  Apartado F")
    # apartadoF()
    print("------------- ")
    N = 10
    a = -2 * np.ones(N)
    bu = np.ones(N - 1)
    bd = np.ones(N-1)
    for i in range(1, N, 2):
        a[i] = a[i] / 10
        if i == 9:
            bd[i-1] = bd[i-1] / 10
            break
        bu[i] = bu[i] / 10
        bd[i - 1] = bd[i - 1] / 10
    A = np.diag(a) + np.diag(bu, 1) + np.diag(bd, -1)

    print("La matriz de inicial es")
    print(A)
    res = (np.round(GeneralizedHouseHolderMethod(A), 2))
    print("La matriz de salida es")
    print(res)
