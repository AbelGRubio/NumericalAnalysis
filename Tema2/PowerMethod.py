import numpy as np


def PowerMethod(*var, TOL: float = 1e-6, M: int = 5000):
    """

    :parameter var:
    :parameter TOL: `float` valor de la tolerancia
    :parameter M: `int` número máximo de iteraciones

    :return: Devuelve los autovectores de A, el recomendado split de A, o un mensaje de número de iteraciones excedida
    """
    assert 3 > len(var) > 0, "Has introducido mal los argumentos"

    if len(var) == 1:
        A = var[0]
        assert type(A) == np.ndarray, "No es un matrix del tipo " + str(np.ndarray)
        n, m = A.shape
        assert n == m, "No es una matriz cuadrada"
        print("La matriz introducida es: ")
        print(A)
        x0 = np.zeros(n)
        x0[0] = 1
        del n, m
    elif len(var) == 2:
        A = var[0]
        x0 = var[1]
        assert type(A) == np.ndarray, "No es un matrix del tipo " + str(np.ndarray)
        n, m = A.shape
        assert n == m, "No es una matriz cuadrada"
        print("La matriz introducida es: ")
        print(A)
        assert len(x0) == n, "Las longitudes de los vectores son incorrectas"
        del n, m
    else:
        A = []
        x0 = []
        assert False, "Error en las variables introducidas"

    # ########### STEP 1: ########################################
    k = 1

    # ########### STEP 2: ########################################
    norminf = max(abs(x0))
    p = min(np.where(abs(x0) == norminf)[0])

    # ########### STEP 3: ########################################
    x = x0 / x0[p]

    # ########### STEP 4: ########################################
    while k <= M:
        # ########### STEP 5: ########################################
        y = A.dot(x)
        y = np.squeeze(np.asarray(y))  # para transformalo en un array
        # ########### STEP 6: ########################################
        mu = y[p]

        # ########### STEP 7: ########################################
        norminf = max(abs(y))
        p = min(np.where(abs(y) == norminf)[0])

        # ########### STEP 8: ########################################
        if y[p] == 0:
            return ["Eigenvector", x0, "A has a eigenvalue 0, select a new vector x and restart"]

        # ########### STEP 9: ########################################
        ERR = max(abs(x - (y / y[p])))
        x = y / y[p]

        # ########### STEP 10: ########################################
        if ERR < TOL:
            return [mu, x]

        # ########### STEP 11: ########################################
        k = k + 1
    # ########### STEP 12: ########################################
    return ["The maximum number of iterations exceeded"]



