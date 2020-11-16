"""
    Este módulo permite mostrar los resultados de los apartados del tema 2


"""

from Tema2.Ejercicio import *
import numpy as np


def main():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Anp = np.array(A)
    # print(QRMethod([3, 3, 3], [1, 1]))
    # a = [0.5, 0.8, 0.6, 1]
    # b = [0.25, 0.4, 0.1]
    # print(QRMethod(a, b))
    # a = [5, 4.5, 1, 3, 3]
    # b = [-1, 0.2, -0.4, 1]
    # print(QRMethod(a, b))
    print(PowerMethod(np.array([[-2, -3], [6, 7]])))

    # n = 10
    # a = (2 * np.ones(n)).tolist()
    # b = (-1 * np.ones(n-1)).tolist()
    # print(QRMethod(a, b))


if __name__ == '__main__':
    main()
