

def funSub2(h, values, Us, Ks):
    """
    Esta funcion calcula los valores de K con subindice i,2 con i = 1,2,3,4
    :param h: valor del step
    :param values: son los valores de las funciones p, q y r evaluadas en x [p(x), q(x), r(x)]
    :param Us: son los valores de la funcion y la derivada en el paso anterior
    :param Ks: valores de las constantes k con subindices Ki1, y Ki2 respectivamente con i = 1,2,3,4
    :return:
    """
    return h * (values[0] * (Us[1] + Ks[1]) + values[1] * (Us[0] + Ks[0]) + values[2])


def funSub1(h, u, k):
    """
    Esta funcion calcula los valores de K con subindice i,1 con i = 1,2,3,4
    :param h: valor del step
    :param u: valor de la funcion o la derivada en el paso anterior
    :param k: valor de la constante k
    :return:
    """
    return h * (u + k)


def updateUs(Us, K1, K2):
    """
    Actualiza los valores de la funcion para la siguiente iteracion
    :param Us: son los valores de la funcion y de la derivada en el paso anterior
    :param K1: valores de la constantes para actualizar el valor de la funcion
    :param K2: valores de las constantes para actualizar el valor de la derivada
    :return:
    """
    u1 = Us[0] + 1/6 * (K1[0] + 2 * K1[1] + 2 * K1[2] + K1[3])
    u2 = Us[1] + 1/6 * (K2[0] + 2 * K2[1] + 2 * K2[2] + K2[3])
    return [u1, u2]


def rungeKutta4(h, x, funs, Us):
    """
    Funcion que estima los valores de
    :param h:
    :param x:
    :param funs:
    :param Us: son los valores de la funcion y la derivada en el paso anterior
    :return:
    """
    # Evaluamos las funciones en los puntos de interes
    px = funs[0](x)
    qx = funs[1](x)
    rx = funs[2](x)
    pxh2 = funs[0](x+h/2)
    qxh2 = funs[1](x+h/2)
    rxh2 = funs[2](x+h/2)
    pxh = funs[0](x+h)
    qxh = funs[1](x+h)
    rxh = funs[2](x+h)

    k11 = funSub1(h, Us[1], 0)
    k12 = funSub2(h, [px, qx, rx], Us, [0, 0])
    k21 = funSub1(h, Us[1], 0.5 * k12)
    k22 = funSub2(h, [pxh2, qxh2, rxh2], Us, [0.5 * k11, 0.5 * k12])
    k31 = funSub1(h, Us[1], 0.5 * k22)
    k32 = funSub2(h, [pxh2, qxh2, rxh2], Us, [0.5 * k21, 0.5 * k22])
    k41 = funSub1(h, Us[1], k32)
    k42 = funSub2(h, [pxh, qxh, rxh], Us, [k31, k32])
    Us = updateUs(Us, [k11, k21, k31, k41], [k12, k22, k32, k42])
    return Us


def ShootingMethod(N, a, b, alpha, beta, funs, vfuns):
    """

    :param N: Numero de subintervalos
    :param a: valor minimo de x del intervalo a estudiar
    :param b: valor maximo de x del intervalo a estudiar
    :param alpha: condicion de contorno del problema de valor inicial para el punto a
    :param beta: condicion de contorno del problema de valor inicial para el punto b
    :param funs: son las funciones p(x), q(x) y r(x) de la ecuacion de segundo grado
    :param vfuns: son las funciones p(x) y q(x) de la ecuacion de segundo grado
    :return: devuelve los valores y(x) y su derivada a la ecuacion planteada
    """
    h = (b - a) / N
    u10 = alpha
    u20 = 0
    v10 = 0
    v20 = 1
    u1 = [u10]
    u2 = [u20]
    v1 = [v10]
    v2 = [v20]
    X = [a]
    # u1i = u10
    # u2i = u20
    # v1i = v10
    # v2i = v20

    for i in range(N):
        x = a + i * h
        [u1i, u2i] = rungeKutta4(h, x, funs, [u1[i], u2[i]])
        u1.append(u1i)
        u2.append(u2i)
        [v1i, v2i] = rungeKutta4(h, x, vfuns, [v1[i], v2[i]])
        v1.append(v1i)
        v2.append(v2i)

    w10 = alpha
    w20 = (beta - u1[N]) / v1[N]
    print('Beta value: ', beta)
    print('u1N value: ', u1[N])
    if beta / u1[N] < 0.1:
        print("Round-off problem " + str(beta / u1[N]))
    W1 = [w10]
    W2 = [w20]
    for i in range(1, N+1):
        aux1 = u1[i] + w20 * v1[i]
        W1.append(aux1)
        aux2 = u2[i] + w20 * v2[i]
        W2.append(aux2)
        x = a + i * h
        X.append(x)

    # error stimation
    error = []
    for i in range(len(W1)):
        val = abs(u1[i] - W1[i]) / (h**4 * abs(1+v1[i]/v1[N]))
        error.append(val)

    return X, W1, W2


def ReverseShootingMethod(N, a, b, alpha, beta, funs, vfuns):
    """

    :param N: Numero de subintervalos
    :param a: valor minimo de x del intervalo a estudiar
    :param b: valor maximo de x del intervalo a estudiar
    :param alpha: condicion de contorno del problema de valor inicial para el punto a
    :param beta: condicion de contorno del problema de valor inicial para el punto b
    :param funs: son las funciones p(x), q(x) y r(x) de la ecuacion de segundo grado
    :param vfuns: son las funciones p(x) y q(x) de la ecuacion de segundo grado
    :return: devuelve los valores y(x) y su derivada a la ecuacion planteada
    """
    h = (b - a) / N
    u10 = alpha
    u20 = 0
    v10 = 0
    v20 = 1
    u1 = [u10]
    u2 = [u20]
    v1 = [v10]
    v2 = [v20]
    X = [b]
    # u1i = u10
    # u2i = u20
    # v1i = v10
    # v2i = v20

    for i in range(N):
        x = b - i * h
        [u1i, u2i] = rungeKutta4(h, x, funs, [u1[i], u2[i]])
        u1.append(u1i)
        u2.append(u2i)
        [v1i, v2i] = rungeKutta4(h, x, vfuns, [v1[i], v2[i]])
        v1.append(v1i)
        v2.append(v2i)

    w10 = alpha
    w20 = (beta - u1[N]) / v1[N]
    print('Beta value: ', beta)
    print('u1N value: ', u1[N])
    if beta / u1[N] < 0.1:
        print("Round-off problem " + str(beta / u1[N]))
    W1 = [w10]
    W2 = [w20]
    for i in range(1, N+1):
        aux1 = u1[i] + w20 * v1[i]
        W1.append(aux1)
        aux2 = u2[i] + w20 * v2[i]
        W2.append(aux2)
        x = b - i * h
        X.append(x)

    # error stimation
    error = []
    for i in range(len(W1)):
        val = abs(u1[i] - W1[i]) / (h**4 * abs(1+v1[i]/v1[N]))
        error.append(val)

    return X, W1, W2


def defineEquation1(l, p0):
    pfun = lambda x: 0
    qfun = lambda x: -(1 + (x/l)**2) / l**2
    rfun = lambda x: -p0
    return [pfun, qfun, rfun]


def defineEquation2(l):
    pfun = lambda x: 0
    qfun = lambda x: -(1 + (x/l)**2) / l**2
    rfun = lambda x: 0
    return [pfun, qfun, rfun]