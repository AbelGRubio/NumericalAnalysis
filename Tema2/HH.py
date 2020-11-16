import numpy as np


def HouseHolderMethod(A: np.ndarray):
    """
    Descompone la matriz simétrica en una matriz tridiagonal.

    :parameter A: Matrix simétrica cuadrada
    :return:
    """

    assert type(A) == np.ndarray, "No es un matrix del tipo " + str(np.ndarray)
    n, m = A.shape
    assert n == m, "No es una matriz cuadrada"
    assert (A == A.transpose()).all(), "No es una matriz simétrica"

    A = A.astype(float)
    # vVector = np.zeros(n)
    # uVector = np.zeros(n)
    # zVector = np.zeros(n)
    Ak1 = A.copy()

    # ########### STEP 1: ########################################
    for k in range(n-2):
        A = Ak1.copy()

        # ########### STEP 2: ########################################
        vector = A[:, k]
        q = sum(vector[(k+1):n]**2)

        # ########### STEP 3: ########################################
        if A[k+1, k] == 0:
            alpha = - q**(1/2)
        else:
            alpha = - q**(1/2) * A[k+1, k] / abs(A[k+1, k])

        # ########### STEP 4: ########################################
        RSQ = alpha**2 - alpha * A[k+1, k]

        # ########### STEP 5: ########################################
        vVector = np.zeros(n)
        vVector[k+1] = A[k+1, k] - alpha
        for j in range(k+2, n):
            vVector[j] = A[j, k]

        # ########### STEP 6: ########################################
        uVector = np.zeros(n)
        for j in range(k, n):
            uVector[j] = sum(A[j, (k+1):n]*vVector[(k+1):n]) / RSQ

        # ########### STEP 7: ########################################
        PROD = sum(vVector[(k+1):n]*uVector[(k+1):n])

        # ########### STEP 8: ########################################
        zVector = np.zeros(n)
        for j in range(k, n):
            zVector[j] = uVector[j] - (PROD / (2 * RSQ)) * vVector[j]

        # ########### STEP 9: ########################################
        for l in range(k+1, n-1):

            # ########### STEP 10: ########################################
            for j in range(l, n):
                Ak1[j, l] = A[j, l] - vVector[l] * zVector[j] - vVector[j] * zVector[l]
                Ak1[l, j] = Ak1[j, l]

            # ########### STEP 11: ########################################
            Ak1[l, l] = A[l, l] - 2 * vVector[l] * zVector[l]

        # ########### STEP 12: ########################################
        Ak1[n-1, n-1] = A[n-1, n-1] - 2 * vVector[n-1] * zVector[n-1]

        # ########### STEP 13: ########################################
        for j in range(k+2, n):
            Ak1[k, j] = 0
            Ak1[j, k] = 0

        # ########### STEP 14: ########################################
        Ak1[k+1, k] = A[k+1, k] - vVector[k+1]*zVector[k]
        Ak1[k, k+1] = Ak1[k+1, k]

        # A = Ak1.copy()
        print("Iter num" + str(k))
        print(Ak1)
        # print("matrix original")
        # print(A)

    return Ak1