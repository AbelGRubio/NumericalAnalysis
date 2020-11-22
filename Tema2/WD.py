from .PowerMethod import InversePowerMethod, PowerMethod
import numpy as np


def WielandtDeflaction(*args, TOL: float = 1e-9, M: int = 5000):
    """

    :parameter args:
    :parameter TOL: `float` valor de la tolerancia
    :parameter M: `int` número máximo de iteraciones

    :return: Devuelve el segundo autovalor y autovector predominante
    """
    assert len(args) == 4, "Has introducido mal los argumentos, matriz A, eigenvalue, eigenvector"

    if len(args) == 4:
        A = args[0]
        assert type(A) == np.ndarray, "No es un matrix del tipo " + str(np.ndarray)
        n, m = A.shape
        assert n == m, "No es una matriz cuadrada"
        print("La matriz introducida es: ")
        print(A)
        eigenvalue = args[1]
        eigenvector = args[2]
        x0 = args[3]
    else:
        A = []
        eigenvalue = []
        eigenvector = []
        assert False, "Error en las variables introducidas"

    # ########### STEP 1: ########################################
    norminf = max(abs(eigenvector))
    i = min(np.where(abs(eigenvector) == norminf)[0])

    # ########### STEP 2: ########################################
    b = np.zeros((n - 1, n - 1))
    if i != 0:
        for k in range(i):
            for j in range(i):
                if k==0 and j ==0:
                    print("entr")
                print(k, j)
                b[k, j] = A[k, j] - eigenvector[k] / eigenvector[i] * A[i, j]

    # ########### STEP 3: ########################################
    if i != 0 and i != (n-1):
        for k in range(i, n-1):
            for j in range(i):

                b[k, j] = A[k + 1, j] - eigenvector[k + 1] / eigenvector[i] * A[i, j]
                b[j, k] = A[j, k + 1] - eigenvector[j] / eigenvector[i] * A[i, k + 1]

    # ########### STEP 4: ########################################
    if i != (n-1):
        for k in range(i, n - 1):
            for j in range(i, n - 1):
                b[k, j] = A[k + 1, j + 1] - eigenvector[k + 1] / eigenvector[i] * A[i, j + 1]

    # ########### STEP 5: ########################################
    res = InversePowerMethod(b, x0, TOL=TOL, M=M)

    # ########### STEP 6: ########################################
    if len(res) == 2:
        [mu, wt] = res
    else:
        return ["Method fails"]

    # ########### STEP 7: ########################################
    w = np.zeros(n)
    if i != 0:
        w[range(i)] = wt[range(i)]

    # ########### STEP 8: ########################################
    w[i] = 0

    # ########### STEP 9: ########################################
    if i != (n - 1):
        w[range(i + 1, n)] = wt[range(i, n-1)]

    # ########### STEP 10: ########################################
    u = np.zeros(n)
    for k in range(n):
        u[k] = (mu - eigenvalue) * w[k] + eigenvector[k] / eigenvector[i] * sum(A[i, :] * w)

    # ########### STEP 11: ########################################
    return [mu, u, b]

