import numpy as np


def QRMethod(*args, TOL: float = 1e-9, M: int = 500):
    """
    Método que utiliza la descomposicion QR para calcular los autovectores de la matriz introducida

    :parameter var: puede contener los vectores a y b.
        Donde a es `List[float]` vector que representa la diagonal de A
        Donde b es `List[float]` vector que representa la diagonal superior e inferior de A
        O puede contener la matrix A
    :parameter TOL: `float` valor de la tolerancia
    :parameter M: `int` número máximo de iteraciones

    :return: Devuelve los autovectores de A, el recomendado split de A, o un mensaje de número de iteraciones excedida
    """
    assert 3 > len(args) > 0, "Has introducido mal los argumentos"

    if len(args) == 1:
        A = args[0]
        assert type(A) == np.ndarray, "No es un matrix del tipo " + str(np.ndarray)
        n, m = A.shape
        assert n == m, "No es una matriz cuadrada"
        del n, m
        print("La matriz introducida es: ")
        print(A)
        a = A.diagonal()
        B = A[:-1, 1:]
        b = B.diagonal()
        del B
        assert (len(a) - 1) == len(b), "Las longitudes de los vectores son incorrectas"
    elif len(args) == 2:
        a = args[0]
        b = args[1]
        assert (len(a) - 1) == len(b), "Las longitudes de los vectores son incorrectas"
    else:
        a = []
        b = []
        assert False, "Error en los vectores introducidos"

    print("El vector a es: ", a)
    print("El vector b es: ", b)

    # insertamos este elemento en b para que tenga la misma longitud de a y
    # por ende referirnos al mismo j en ambos vectores
    if type(b) == np.ndarray:
        b = np.insert(b, 0, 0)
    else:
        b.insert(0, -1)
    OUTPUT = []

    # ########### STEP 1: ########################################
    k = 1
    shift = 0
    n = len(a)-1

    # ########### STEP 2: ########################################
    while k <= M:

        # ########### STEP 3: ########################################
        if abs(b[n]) <= TOL:
            Lambda = a[n] + shift
            OUTPUT.append(Lambda)
            n = n - 1

        # ########### STEP 4: ########################################
        if abs(b[1]) <= TOL:
            Lambda = a[0] + shift
            OUTPUT.append(Lambda)
            n = n - 1
            a[0] = a[1]
            for j in range(1, n+1):  # añadimos +1 para incluir el set de j=n, sino terminaría en j = n-1
                a[j] = a[j+1]
                b[j] = b[j+1]

        # ########### STEP 5: ########################################
        if n == -1:
            return OUTPUT

        # ########### STEP 6: ########################################
        if n == 0:
            Lambda = a[0] + shift
            OUTPUT.append(Lambda)
            return OUTPUT

        # ########### STEP 7: ########################################
        for j in range(2, n+1):
            if abs(b[j]) <= TOL:
                M1 = [a[0:(j-1)], b[1:(j-1)]]
                M2 = [a[j:n], b[(j+1):n]]
                OUTPUT = ["Split into", M1, M2, shift]
                return OUTPUT

        # ########### STEP 8: ########################################
        bval = - (a[n-1] + a[n])
        cval = a[n] * a[n-1] - b[n]**2
        dval = (bval**2-4*cval)**0.5

        # ########### STEP 9: ########################################
        if bval > 0:
            mu1 = - 2 * cval / (bval + dval)
            mu2 = - (bval + dval) / 2
        else:
            mu1 = (dval - bval) / 2
            mu2 = 2 * cval / (dval - bval)

        # ########### STEP 10: ########################################
        if n == 1:
            Lambda1 = mu1 + shift
            Lambda2 = mu2 + shift
            OUTPUT.append(Lambda1)
            OUTPUT.append(Lambda2)
            return OUTPUT

        # ########### STEP 11: ########################################
        vector = [abs(mu1 - a[n]), abs(mu2 - a[n])]
        minimumval = min(vector)
        if minimumval == vector[0]:
            sigmaval = mu1
        else:
            sigmaval = mu2

        # ########### STEP 12: ########################################
        shift = shift + sigmaval

        # ########### STEP 13: ########################################
        d = []
        for j in range(n+1):
            d.append(a[j] - sigmaval)

        # ########### STEP 14: ########################################
        xVec = [d[0]]
        yVec = [b[1]]

        # ########### STEP 15: ########################################
        zVec = []
        cVec = [0]  # añadimos este valor para que tome los indices correctos
        sigmaVec = [0]
        qVec = []
        rVec = []
        for j in range(1, n+1):
            zVec.append((xVec[j-1]**2 + b[j]**2)**0.5)
            cVec.append(xVec[j-1] / zVec[j-1])
            sigmaVec.append(b[j] / zVec[j-1])
            qVec.append(cVec[j] * yVec[j-1] + sigmaVec[j] * d[j])
            xVec.append(-sigmaVec[j] * yVec[j-1] + cVec[j] * d[j])
            if j != n:
                rVec.append(sigmaVec[j] * b[j+1])
                yVec.append(cVec[j] * b[j+1])

        # ########### STEP 16: ########################################
        zVec.append(xVec[n])
        a[0] = sigmaVec[1] * qVec[0] + cVec[1] * zVec[0]
        b[1] = sigmaVec[1] * zVec[1]

        # ########### STEP 17: ########################################
        for j in range(1, n):
            a[j] = sigmaVec[j+1] * qVec[j] + cVec[j] * cVec[j+1] * zVec[j]
            b[j+1] = sigmaVec[j+1] * zVec[j+1]

        # ########### STEP 18: ########################################
        a[n] = cVec[n] * zVec[n]

        # ########### STEP 19: ########################################
        k = k + 1

    # ########### STEP 20: ########################################
    return ["Maximum number of iterations exceeded"]
