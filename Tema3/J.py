"""
    Este modulo define el proceso iteratio de Jacobi para la resulucion de
    sistemas de ecuaciones

"""
import numpy as np


def JacobiIterative(*argvs, TOL: float = 1e-9, N: int = 500) -> list:
    """

    :parameter argvs: argumentos variables donde indicaremos, como mínimo, la matrix A y la matriz b del sistema a resolver
        .. mat::
            A x = b
        Adicionalmente podemos introducir un vector inicial para comenzar el algoritmo
    :parameter TOL: Tolerancia de la solucion
    :parameter N: Número máximo de iteraciones
    :return: devuelve la solucion al sistema propuesto.
    """

    assert len(argvs) < 3, "Numero de variables de entrada  incorrecto"

    A = argvs[0]
    assert type(A) == np.ndarray, "La variable no es del tipo " + str(np.ndarray)
    b = argvs[1]

    if len(argvs) == 3:
        XO = argvs[2].astype(float)
    else:
        XO = np.zeros_like(b).astype(float)

    n = A.shape[1]
    x = XO.copy()

    # @@@@@@@@@@@@@@@@@@@@@@@@@@ STEP 1 @@@@@@@@@@@@@@@@@@
    k = 1

    # @@@@@@@@@@@@@@@@@@@@@@@@@@ STEP 2 @@@@@@@@@@@@@@@@@@
    while k < N:
        # @@@@@@@@@@@@@@@@@@@@@@@@@@ STEP 3 @@@@@@@@@@@@@@@@@@
        for i in range(n):
            x[i] = 1 / A[i, i] * (-sum(A[i, range(i)] * XO[range(i)]) -
                                  sum(A[i, range(i+1, n)] * XO[range(i+1, n)]) + b[i])

        # @@@@@@@@@@@@@@@@@@@@@@@@@@ STEP 4 @@@@@@@@@@@@@@@@@@
        if sum(abs(x-XO)) < TOL:
            return [x]

        # @@@@@@@@@@@@@@@@@@@@@@@@@@ STEP 5 @@@@@@@@@@@@@@@@@@
        k += 1

        # @@@@@@@@@@@@@@@@@@@@@@@@@@ STEP 6 @@@@@@@@@@@@@@@@@@
        XO = x.copy()

    # @@@@@@@@@@@@@@@@@@@@@@@@@@ STEP 7 @@@@@@@@@@@@@@@@@@
    return ["Maximum number of iterations exceeded"]


# if __name__ == '__main__':
#     A = [[10, -1, 2, 0],
#          [-1, 11, -1, 3],
#          [2, -1, 10, -1],
#          [0, 3, -1, 8]]
#     A = np.array(A).astype(float)
#     b = [6, 25, -11, 15]
#     b = np.array(b)
#     res = JacobiIterative(A, b)
#     print(res)