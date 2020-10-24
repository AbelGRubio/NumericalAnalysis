

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
    Metodo que se utiliza en un proceso iterativo para obtener una solucion
     a una ecuacion diferencial planteada
    :param h: tamaño del paso
    :param x: punto de la funcion
    :param funs: funciones p(x), q(x) y r(x)
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


def defineEquation1(l, p0):
    """
    Funcion que define las funciones p(x), q(x) y r(x)
    para el caso del primer problema de valores iniciales
    :param l:
    :param p0:
    :return:
    """
    pfun = lambda x: 0
    qfun = lambda x: -(1 + (x/l)**2) / l**2
    rfun = lambda x: -p0
    return [pfun, qfun, rfun]


def defineEquation2(l):
    """
    Funcion que define las funciones p(x), q(x) y r(x) para
    el caso del segundo problema de valores iniciales
    :param l:
    :return:
    """
    pfun = lambda x: 0
    qfun = lambda x: -(1 + (x/l)**2) / l**2
    rfun = lambda x: 0
    return [pfun, qfun, rfun]


def ShootingMethod(N, a, b, alpha, beta, funs, vfuns):
    """
    Metodo del disparo para resolucion de ecuaciones diferenciales de segundo orden
    utilizando la aproximación Runge Kutta de orden 4
    :param N: Numero de subintervalos
    :param a: valor minimo de x del intervalo a estudiar
    :param b: valor maximo de x del intervalo a estudiar
    :param alpha: condicion de contorno del problema de valor inicial para el punto a
    :param beta: condicion de contorno del problema de valor inicial para el punto b
    :param funs: son las funciones p(x), q(x) y r(x) de la ecuacion de segundo grado
    :param vfuns: son las funciones p(x) y q(x) de la ecuacion de segundo grado
    :return: devuelve los valores y(x) y su derivada a la ecuacion planteada
    """

    """ STEP 1: """
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

    """ STEP 2: """
    for i in range(N):
        """ STEP 3: """
        x = a + i * h

        """ STEP 4: """
        [u1i, u2i] = rungeKutta4(h, x, funs, [u1[i], u2[i]])
        u1.append(u1i)
        u2.append(u2i)
        [v1i, v2i] = rungeKutta4(h, x, vfuns, [v1[i], v2[i]])
        v1.append(v1i)
        v2.append(v2i)

    """ STEP 5: """
    w10 = alpha
    w20 = (beta - u1[N]) / v1[N]
    if beta / u1[N] < 0.1:
        print("Round-off problem " + str(beta / u1[N]))
        print('Beta value: ', beta)
        print('u1N value: ', u1[N])

    """ STEP 6: """
    W1 = [w10]
    W2 = [w20]
    for i in range(1, N+1):
        aux1 = u1[i] + w20 * v1[i]
        W1.append(aux1)
        aux2 = u2[i] + w20 * v2[i]
        W2.append(aux2)
        x = a + i * h
        X.append(x)

    # # error stimation
    # error = []
    # for i in range(len(W1)):
    #     val = abs(u1[i] - W1[i]) / (h**4 * abs(1+v1[i]/v1[N]))
    #     error.append(val)

    return X, W1, W2


def ReverseShootingMethod(N, a, b, alpha, beta, funs, vfuns):
    """
    Metodo del disparo para resolucion de ecuaciones diferenciales de segundo orden
    utilizando la aproximación Runge Kutta de orden 4
    :param N: Numero de subintervalos
    :param a: valor minimo de x del intervalo a estudiar
    :param b: valor maximo de x del intervalo a estudiar
    :param alpha: condicion de contorno del problema de valor inicial para el punto a
    :param beta: condicion de contorno del problema de valor inicial para el punto b
    :param funs: son las funciones p(x), q(x) y r(x) de la ecuacion de segundo grado
    :param vfuns: son las funciones p(x) y q(x) de la ecuacion de segundo grado
    :return: devuelve los valores y(x) y su derivada a la ecuacion planteada
    """

    """ STEP 1: """
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

    """ STEP 2: """
    for i in range(N):
        """ STEP 3: """
        x = b - i * h
        """ STEP 4: """
        [u1i, u2i] = rungeKutta4(h, x, funs, [u1[i], u2[i]])
        u1.append(u1i)
        u2.append(u2i)
        [v1i, v2i] = rungeKutta4(h, x, vfuns, [v1[i], v2[i]])
        v1.append(v1i)
        v2.append(v2i)

    """ STEP 5: """
    w10 = alpha
    w20 = (beta - u1[N]) / v1[N]
    if beta / u1[N] < 0.1:
        print("Round-off problem " + str(beta / u1[N]))
        print('Beta value: ', beta)
        print('u1N value: ', u1[N])

    """ STEP 5: """
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
    # error = []
    # for i in range(len(W1)):
    #     val = abs(u1[i] - W1[i]) / (h**4 * abs(1+v1[i]/v1[N]))
    #     error.append(val)

    return X, W1, W2


def LinearFiniteDifference(N, a, b, alpha, beta, funs):
    """
    Método de diferencias finitas
    :param N: Numero de subintervalos
    :param a: valor minimo de x del intervalo a estudiar
    :param b: valor maximo de x del intervalo a estudiar
    :param alpha: condicion de contorno del problema de valor inicial para el punto a
    :param beta: condicion de contorno del problema de valor inicial para el punto b
    :param funs: son las funciones p(x), q(x) y r(x) de la ecuacion de segundo grado
    :return: devuele la solucion de la ecuacion de sgundo orden evaluada en todos los puntos
    """

    """ STEP 1: """
    h = (b - a) / (N + 1)
    x = a + h
    a1 = 2 + h**2 * funs[1](x)
    A = [a1]
    b1 = -1 + h/2 * funs[0](x)
    B = [b1]
    C = [0]  # este valor no se utiliza en ningun momento, solo es para que el vector C este a la par de los demás
    d1 = -h**2 * funs[2](x)
    D = [d1]

    """ STEP 2: """
    for i in range(1, N-1):
        x = a + i*h
        ai = 2 + h**2 * funs[1](x)
        A.append(ai)
        bi = -1 + h / 2 * funs[0](x)
        B.append(bi)
        ci = -1 - h / 2 * funs[0](x)
        C.append(ci)
        di = -h**2*funs[2](x)
        D.append(di)

    """ STEP 3: """
    x = b - h
    an = 2 + h**2 * funs[1](x)
    A.append(an)
    cn = -1 - h/2 * funs[0](x)
    C.append(cn)
    dn = -h**2 * funs[2](x) + (1 - (h / 2) * funs[0](x)) * beta
    D.append(dn)

    """ STEP 4: """
    l1 = a1
    u1 = b1 / a1
    U = [u1]
    z1 = d1 / l1
    Z = [z1]

    """ STEP 5: """
    for i in range(1, N-1):
        li = A[i] - C[i]*U[i-1]
        ui = B[i] / li
        U.append(ui)
        zi = (D[i] - C[i]*Z[i-1])/li
        Z.append(zi)

    """ STEP 6: """
    ln = an - cn*U[len(U)-1]
    zn = (dn - cn*Z[len(Z)-1])/ln
    Z.append(zn)

    """ STEP 7: """
    w0 = alpha
    wnplus1 = beta
    wn = zn
    W = [wnplus1, wn]

    """ STEP 8: """
    for i in range(N-2, -1, -1):
        wi = Z[i] - U[i]*W[N-i-1]
        W.append(wi)
    W.append(w0)
    W = W[::-1]

    """ STEP 9: """
    X = []
    for i in range(N+2):
        x = a + i * h
        X.append(x)
    return X, W