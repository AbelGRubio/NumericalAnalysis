import numpy as np


def PowerMethod(*args, TOL: float = 1e-9, M: int = 5000):
    """
    Calcula el autovector del autovalor predominante.

    :parameter args: Acepta argumentos variables.
        * Si introducimos solo un argumento, éste tiene que ser la matriz. El vector X_0 tomará uno sencillo
        * Si introducimos dos argumentos, uno tiene que ser la matriz y el otro el vector
        ambos del tipo np.ndarray. O simplemente dos vectores que indican la diagonal y la diagonal inferior
        y/o superior respectivamente
        * Si introducimos tres argumentos, el primero tiene que ser el vector de la diagonal, el segundo el vector
        de la diagonal inferior y el ultimo el vector X_0
    :parameter TOL: `float` valor de la tolerancia
    :parameter M: `int` número máximo de iteraciones

    :return: Devuelve el autovectores de A con el autovalor de mayor magnitud,
    o un mensaje de número de iteraciones excedida
    """
    assert 4 > len(args) > 0, "Has introducido mal los argumentos"

    if len(args) == 1:
        A = args[0]
        assert type(A) == np.ndarray, "No es un matrix del tipo " + str(np.ndarray)
        n, m = A.shape
        assert n == m, "No es una matriz cuadrada"
        print("La matriz introducida es: ")
        print(A)
        x0 = np.zeros(n)
        x0[0] = 1
        del n, m
    elif len(args) == 2:
        res = args[0]
        try:
            n, m = res.shape
        except ValueError:
            n = res.shape
            m = 0
        if n == m:
            A = args[0]
            x0 = args[1]
            assert type(A) == np.ndarray, "No es un matrix del tipo " + str(np.ndarray)
            n, m = A.shape
            assert n == m, "No es una matriz cuadrada"
            assert len(x0) == n, "Las longitudes de los vectores son incorrectas"
            del n, m
        else:
            a = args[0]
            b = args[1]
            A = np.diag(a) + np.diag(b, 1) + np.diag(b, -1)
            n, m = A.shape
            assert n == m, "No es una matriz cuadrada"
            x0 = np.zeros(len(a))
            x0[0] = 1
            del n, m
    elif len(args) == 3:
        a = args[0]
        b = args[1]
        assert (len(a) - 1) == len(b), "Las longitudes de los vectores son incorrectas"
        A = np.diag(a) + np.diag(b, 1) + np.diag(b, -1)
        x0 = args[2]
    else:
        A = []
        x0 = []
        assert False, "Error en las variables introducidas"

    print("La matriz introducida en el método de la potencia es: ")
    print(A)
    # ########### STEP 1: ########################################
    k = 1

    # ########### STEP 2: ########################################
    norminf = max(abs(x0))
    p = min(np.where(abs(x0) == norminf)[0])

    # ########### STEP 3: ########################################
    x = x0 / x0[p]
    print("El vector inicial es normalizado a norma infinita es:")
    print(x)

    # ########### STEP 4: ########################################
    while k <= M:
        # ########### STEP 5: ########################################
        y = A @ x
        # y = A.dot(x)
        # y = np.squeeze(np.asarray(y))  # para transformalo en un array
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


def InversePowerMethod(*args, TOL: float = 1e-6, M: int = 5000) -> list:
    """
    Este método esta implementado para poder utilizar el método de WielandtDeflaction y poder determinar el
    segundo autovalor predominante de una matriz. Este método tiene una mejor convergencia respecto al método
    de la potencial
    :parameter args: Acepta argumentos variables.
        * Si introducimos solo un argumento, éste tiene que ser la matriz. El vector X_0 tomará uno sencillo
        * Si introducimos dos argumentos, uno tiene que ser la matriz y el otro el vector
        ambos del tipo np.ndarray. O simplemente dos vectores que indican la diagonal y la diagonal inferior
        y/o superior respectivamente
        * Si introducimos tres argumentos, el primero tiene que ser el vector de la diagonal, el segundo el vector
        de la diagonal inferior y el ultimo el vector X_0
    :parameter TOL: `float` valor de la tolerancia
    :parameter M: `int` número máximo de iteraciones

    :return: Devuelve el autovector de A con el autovalor proximo a p, o un mensaje de número de iteraciones excedida
    """
    assert 4 > len(args) > 0, "Has introducido mal los argumentos"

    if len(args) == 1:
        A = args[0]
        assert type(A) == np.ndarray, "No es un matrix del tipo " + str(np.ndarray)
        n, m = A.shape
        assert n == m, "No es una matriz cuadrada"
        print("La matriz introducida es: ")
        print(A)
        x0 = np.zeros(n)
        x0[0] = 1
        del n, m
    elif len(args) == 2:
        res = args[0]
        try:
            n, m = res.shape
        except ValueError:
            n = res.shape
            m = 0
        if n == m:
            A = args[0]
            x0 = args[1]
            assert type(A) == np.ndarray, "No es un matrix del tipo " + str(np.ndarray)
            n, m = A.shape
            assert n == m, "No es una matriz cuadrada"
            print("La matriz introducida es: ")
            print(A)
            assert len(x0) == n, "Las longitudes de los vectores son incorrectas"
            del n, m
        else:
            a = args[0]
            b = args[1]
            A = np.diag(a) + np.diag(b, 1) + np.diag(b, -1)
            n, m = A.shape
            assert n == m, "No es una matriz cuadrada"
            x0 = np.zeros(len(a))
            x0[0] = 1
            del n, m
    elif len(args) == 3:
        a = args[0]
        b = args[1]
        assert (len(a) - 1) == len(b), "Las longitudes de los vectores son incorrectas"
        A = np.diag(a) + np.diag(b, 1) + np.diag(b, -1)
        x0 = args[2]
    else:
        A = []
        x0 = []
        assert False, "Error en las variables introducidas"

    # ########### STEP 1: ########################################
    q = (x0.transpose() @ A @ x0) / (x0.transpose() @ x0)

    # ########### STEP 2: ########################################
    k = 1

    # ########### STEP 3: ########################################
    norminf = max(abs(x0))
    p = min(np.where(abs(x0) == norminf)[0])

    # ########### STEP 4: ########################################
    x = x0 / x0[p]
    print("El vector inical es:")
    print(x)

    # ########### STEP 5: ########################################
    while k <= M:
        # ########### STEP 6: ########################################
        Als = A - q * np.eye(len(x0))
        y = np.linalg.solve(Als, x0)

        # ########### STEP 7: ########################################


        # ########### STEP 8: ########################################
        mu = y[p]

        # ########### STEP 9: ########################################
        norminf = max(abs(y))
        p = min(np.where(abs(y) == norminf)[0])

        # ########### STEP 10: ########################################
        ERR = max(abs(x - (y / y[p])))
        x = y / y[p]

        # ########### STEP 11: ########################################
        if ERR < TOL:
            mu = 1 / mu + q
            return [mu, x]

        # ########### STEP 12: ########################################
        k = k + 1
    # ########### STEP 13: ########################################
    return ["The maximum number of iterations exceeded"]


# if __name__ == '__main__':
#     from Tema2.QR import QRMethod
#     from Tema2.HH import HouseHolderMethod
#     np.random.seed(5)
#     Asys = np.random.random((5, 5))
#     Asys = (Asys + Asys.transpose()) / 2
#     print(InversePowerMethod(Asys))
#     print(QRMethod(HouseHolderMethod(Asys)))