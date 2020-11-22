"""
    En este modulo utilizaremos las funciones necesarias para realizar las operaciones de semejanza y
    de este modo obtenemos una matriz simétrica tridiagonal

    Dos matrices son semejantes si el cambio se puede expresar de la siguiente forma matricial

    .. math::
        B = P^-1*A*P

    donde P es la matriz de cambio.

    Para obtener la matriz de cambio debemos proceder del siguiente modo. Como sabemos que ambas matrices,
    al ser semejantes, poseen los mismos autovalores. Por tanto diagonalizando tenemos:

    .. math::
        D = S*A*S^-1            D = T*B*T^-1       -->     S*A*S^-1 = T*B*T^-1
        A*S^-1*T = S^-1*T*B -- > A*P = P*B  --> P = S^-1*T

    de este modo llegamos a la forma matricial ya mostrada anteriormente. Ahora tenemos que definir como queremos
    que sea B, como andamos buscando una matriz simétrica tridiagonal tendremos bastará con definirla como
    B = (A+A.T)/2

"""
import scipy.linalg as la
import numpy as np


def SimilarityTransformations():
    N = 10
    a = -2 * np.ones(N)
    bu = np.ones(N - 1)
    bd = np.ones(N - 1)
    A0 = np.diag(a) + np.diag(bu, 1) + np.diag(bd, -1)
    for i in range(1, N, 2):
        a[i] = a[i] / 10
        if i == 9:
            bd[i - 1] = bd[i - 1] / 10
            break
        bu[i] = bu[i] / 10
        bd[i - 1] = bd[i - 1] / 10
    A = np.diag(a) + np.diag(bu, 1) + np.diag(bd, -1)
    B = (A + A.T) / 2

    # print(A0)
    # eigvalsA0, eigvecsA0 = la.eig(A0)
    # print(np.round(eigvalsA0, 2))

    # print(A)
    eigvalsA, eigvecsA = la.eig(A)
    DA = np.diag(eigvalsA)
    # print(np.round(DA, 2))
    # print(np.round(eigvalsA, 2))
    # print(np.round(eigvecsA @ DA @ la.inv(eigvecsA), 2).real)

    print(B)
    eigvalsB, eigvecsB = la.eig(B)
    Br = eigvecsB @ np.diag(eigvalsB) @ la.inv(eigvecsB)
    print(np.round(Br, 2).real)
    P = la.inv(eigvecsA) @ eigvecsB

    Brp = la.inv(P) @ A @ P
    # print(np.round(Brp, 2))
    # print(np.round(eigvecsA, 2))
    # print(np.round(eigvecsA[:, 1], 2))


if __name__ == '__main__':
    SimilarityTransformations()