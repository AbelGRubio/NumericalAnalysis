"""
    Este módulo permite mostrar los resultados de los apartados.


"""

from module.functions import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


def resolucionApartadoA():
    """
    Esta función muestra los resultados obtenidos por el método de diferencias finitas
    para l=1, N=20 y presión verital de 5 N/m

    :return: Devuelve los datos del modelo y los muestra en una gráfica
    """
    l = 1
    N = 20
    p0 = 5
    prefix = "N" + str(N) + "P" + str(p0) + "l" + str(l)
    resultFolder = "ApartadoA"
    if not os.path.isdir(resultFolder):
        os.mkdir(resultFolder)
    if not os.path.isdir(os.path.join(resultFolder, prefix)):
        os.mkdir(os.path.join(resultFolder, prefix))
    result = LinearFiniteDifference(N-1, -l, l, 0, 0, defineEquation1(l, p0))
    fig1 = plt.figure(1)
    plt.plot(result[0], result[1])
    plt.legend(["Método de diferencias finitas"])
    plt.title("Diagrama de momento flector de la barra de longitud " + str(2 * l) +
              " m\npara una presión vertical de " + str(p0) + " N/m")
    plt.xlabel("Longitud de la barra, ξ, m")
    plt.ylabel("Momento flector, M(ξ), Nm")
    name = os.path.normpath(''.join([resultFolder, "/", prefix, "/MetodoDisparo", prefix, ".png"]))
    fig1.savefig(name)
    DataFrame = pd.DataFrame([])
    DataFrame['xi'] = result[0]
    DataFrame['M'] = result[1]
    print(DataFrame)
    DataFrame.to_csv(''.join([resultFolder, "/", prefix, "/Diff", prefix, ".csv"]))
    plt.show()


def resolucionApartadoB():
    """
    Esta función muestra los resultados obtenidos por el método del disparo
    para l=1, N=20 y presión verital de 5 N/m

    :return: Devuelve los datos del modelo y los muestra en una gráfica
    """
    l = 1
    N = 20
    p0 = 5
    prefix = "N" + str(N) + "P" + str(p0) + "l" + str(l)
    resultFolder = "ApartadoB"
    if not os.path.isdir(resultFolder):
        os.mkdir(resultFolder)
    if not os.path.isdir(os.path.join(resultFolder, prefix)):
        os.mkdir(os.path.join(resultFolder, prefix))
    result = ShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
    fig1 = plt.figure(1)
    plt.plot(result[0], result[1])
    plt.legend(["Método del disparo"])
    plt.title("Diagrama de momento flector de la barra de longitud " + str(2 * l) +
              " m\npara una presión vertical de " + str(p0) + " N/m")
    plt.xlabel("Longitud de la barra, ξ, m")
    plt.ylabel("Momento flector, M(ξ), Nm")
    name = os.path.normpath(''.join([resultFolder, "/", prefix, "/MetodoDisparo", prefix, ".png"]))
    fig1.savefig(name)
    DataFrame = pd.DataFrame([])
    DataFrame['xi'] = result[0]
    DataFrame['M'] = result[1]
    DataFrame['dMdxi'] = result[2]
    print(DataFrame)
    DataFrame.to_csv(''.join([resultFolder, "/", prefix, "/Diff", prefix, ".csv"]))
    plt.show()


def resolucionComparativaCustom(N, l, p0):
    """
    Esta función muestra los resultados obtenidos por el método de diferencias finitas
    para l=1, N=20 y presión verital de 5 N/m

    :parameter N: Número de subintervalos
    :parameter l: longitud de la viga
    :parameter p0: presión vertical

    :return: Devuelve los datos de los modelos, su diferencia y los muestra en una gráfica
    """
    prefix = "N" + str(N) + "P" + str(p0) + "l" + str(l)
    resultFolder = "resolucionComparativa"
    if not os.path.isdir(resultFolder):
        os.mkdir(resultFolder)
    if not os.path.isdir(os.path.join(resultFolder, prefix)):
        os.mkdir(os.path.join(resultFolder, prefix))
    result = ShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
    DataFrame = pd.DataFrame([])
    DataFrame['xi'] = result[0]
    DataFrame['M'] = result[1]
    DataFrame['dMdxi'] = result[2]
    linearResult = LinearFiniteDifference(N-1, -l, l, 0, 0, defineEquation1(l, p0))
    LinearDataFrame = pd.DataFrame([])
    LinearDataFrame['xi'] = linearResult[0]
    LinearDataFrame['M'] = linearResult[1]
    ComparationDataFrame = LinearDataFrame.copy()
    ComparationDataFrame['MLinear'] = ComparationDataFrame['M']
    del ComparationDataFrame['M']
    ComparationDataFrame['MShoot'] = DataFrame['M']
    ComparationDataFrame['Modulo'] = abs(ComparationDataFrame['MLinear'] - ComparationDataFrame['MShoot'])
    ComparationDataFrame.to_csv(os.path.normpath(''.join([resultFolder, "/", prefix,
                                                          "/Comparacion", prefix, ".csv"])))
    fig5, ax = plt.subplots()
    ax.plot(ComparationDataFrame['xi'], ComparationDataFrame['MLinear'])
    ax.plot(ComparationDataFrame['xi'], ComparationDataFrame['MShoot'])
    ax.set_xlabel("Longitud de la barra, ξ, m")
    ax.set_ylabel("Momento flector, M(ξ), Nm")
    ax2 = ax.twinx()
    ax2.plot(ComparationDataFrame['xi'], ComparationDataFrame['Modulo'], color='m')
    ax2.set_ylabel("Norma, M(ξ), Nm", color='m')
    ax.legend(["Método de diferencias finitas", "Método del disparo"])
    ax.set_title("Diagrama de momento flector para\n"
                 "l=" + str(2 * l) + " m, N=" + str(N) + " y p0=" + str(p0) + " N/m")
    name = os.path.normpath(''.join([resultFolder, "/", prefix, "/ComparativaLong", prefix, ".png"]))
    fig5.savefig(name)
    plt.show()
    return sum(ComparationDataFrame['Modulo'])/len(ComparationDataFrame['Modulo'])


def resolucionComparativa():
    """
    :return: Muestra las comparativas entre los modelos para distintos valores de N y mismo valor de longitud de
            la viga y presión vertical
    """
    resolucionComparativaCustom(20, 1, 5)
    resolucionComparativaCustom(70, 1, 5)
    resolucionComparativaCustom(150, 1, 5)


def resolucionNormaDiferenciasFinitas():
    """
    Calculo norma con n=4, p0=5 y l=1 para el método de diferencias finitas
    :return: Muestra gráficamente y los valores de norma L_1 para distintos valores de N (siendo N=n,2n,3n...).
    Realiza también un análisis cuantitativo.
    """

    n = 4
    p0 = 5
    l = 1
    prefix = "P" + str(p0) + "l" + str(l)
    resultFolder = "resolucionNormaDiferenciasFinitas"
    if not os.path.isdir(resultFolder):
        os.mkdir(resultFolder)
    if not os.path.isdir(os.path.join(resultFolder, prefix)):
        os.mkdir(os.path.join(resultFolder, prefix))

    NVector = [n if i == 0 else i*n for i in range(0, 50, 2)]
    DataFrame = pd.DataFrame([])
    DataFrameDiff = pd.DataFrame([])

    for j in range(len(NVector)):
        N = NVector[j]
        result = LinearFiniteDifference(N-1, -l, l, 0, 0, defineEquation1(l, p0))
        if N == n:
            DataFrame['xi'] = result[0]
            name = "M(xi) N=" + str(N)
            DataFrame[name] = result[1]
        else:
            Vector2 = result[1]
            VectorPar = [Vector2[i] for i in range(len(Vector2)) if i % (2*j) == 0]
            name = "M(xi) N=" + str(N)
            DataFrame[name] = VectorPar
            col2name = "M(xi) N=" + str(NVector[j-1])
            namediff = "N=" + str(NVector[j-1]) + "-" + str(N)
            DataFrameDiff[namediff] = abs(DataFrame[name] - DataFrame[col2name])

    NormaL1 = [sum(DataFrameDiff[colname]) for colname in DataFrameDiff.columns]
    fig1 = plt.figure(1)
    plt.plot(NormaL1)
    funResiduo = lambda p, y, x: y - (1 / (x ** p))
    funAjuste = lambda x, p: (1 / (x ** p))
    from scipy.optimize import leastsq
    popt = [1]
    ajuste = leastsq(funResiduo, popt, args=(NormaL1, np.arange(1,25)))
    print(ajuste[0])
    model = [funAjuste(i, ajuste[0]) for i in np.arange(1, 26, 25/9000)]
    print("Los valores del ajuste para una funcion x**beta son:", *popt)
    plt.plot(np.arange(0, 25, 25/9000), model)
    plt.ylim([0, 0.15])
    plt.title("Estimación del orden de convergencia.\nAjuste de la función para el método de diferencias finitas"
              "\npara l=" + str(l) + " m, y p0=" + str(p0) + " N/m")
    plt.ylabel("Valor de la norma L1")
    plt.legend(["Normas L1 calculadas",
                "Ajuste a la función 1/x^p, p="+str(round(ajuste[0][len(ajuste[0])-1]))])
    name = os.path.normpath(''.join([resultFolder, "/", prefix, "/NComparativaDiferenciasFinitas", prefix, ".png"]))
    fig1.savefig(name)
    DataFrame.to_csv(os.path.normpath(''.join([resultFolder, "/", prefix, "/NMetodosFinitosResultados", prefix, ".csv"])))
    DataFrameDiff.to_csv(os.path.normpath(''.join([resultFolder, "/", prefix, "/NMetodosFinitosDiff", prefix, ".csv"])))
    plt.show()


def resolucionNormaMetodoDisparo():
    """
    Calculo norma con n=4, p0=5 y l=1 para el método del disparo
    :return: Muestra gráficamente y los valores de norma L_1 para distintos valores de N (siendo N=n,2n,3n...).
    Realiza también un análisis cuantitativo.
    """

    n = 4
    p0 = 5
    l = 1
    prefix = "P" + str(p0) + "l" + str(l)
    resultFolder = "resolucionNormaDisparo"
    if not os.path.isdir(resultFolder):
        os.mkdir(resultFolder)
    if not os.path.isdir(os.path.join(resultFolder, prefix)):
        os.mkdir(os.path.join(resultFolder, prefix))

    NVector = [n if i == 0 else i*n for i in range(0, 50, 2)]
    DataFrame = pd.DataFrame([])
    DataFrameDiff = pd.DataFrame([])

    for j in range(len(NVector)):
        N = NVector[j]
        result = ShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
        if N == n:
            DataFrame['xi'] = result[0]
            name = "M(xi) N=" + str(N)
            DataFrame[name] = result[1]
        else:
            Vector2 = result[1]
            VectorPar = [Vector2[i] for i in range(len(Vector2)) if i % (2*j) == 0]
            name = "M(xi) N=" + str(N)
            DataFrame[name] = VectorPar
            col2name = "M(xi) N=" + str(NVector[j-1])
            namediff = "N=" + str(NVector[j-1]) + "-" + str(N)
            DataFrameDiff[namediff] = abs(DataFrame[name] - DataFrame[col2name])

    NormaL1 = [sum(DataFrameDiff[colname]) for colname in DataFrameDiff.columns]
    fig1 = plt.figure(1)
    plt.plot(NormaL1)

    funResiduo = lambda p, y, x: y - (1 / (x ** p))
    funAjuste = lambda x, p: (1 / (x ** p))
    from scipy.optimize import leastsq
    popt = [1]
    ajuste = leastsq(funResiduo, popt, args=(NormaL1, np.arange(1,25)))
    print(ajuste)
    model = [funAjuste(i, ajuste[0]) for i in np.arange(1, 26, 25/9000)]
    plt.plot(np.arange(0, 25, 25/9000), model)
    plt.ylim([0, 0.003])
    plt.title("Estimación del orden de convergencia.\nAjuste de la función para el método del disparo"
              "\npara l=" + str(l) + " m, y p0=" + str(p0) + " N/m")
    plt.ylabel("Valor de la norma L1")
    plt.legend(["Normas L1 calculadas", "Ajuste a la función 1/x^p, p="
                +str(round(ajuste[0][len(ajuste[0])-1]))])
    name = os.path.normpath(''.join([resultFolder, "/", prefix, "/NComparativaDisparo", prefix, ".png"]))
    fig1.savefig(name)
    DataFrame.to_csv(os.path.normpath(''.join([resultFolder, "/", prefix, "/NMetodoDisparoResultados", prefix, ".csv"])))
    DataFrameDiff.to_csv(os.path.normpath(''.join([resultFolder, "/", prefix, "/NMetodoDisparoDiff", prefix, ".csv"])))
    plt.show()


def convergencia(p0):
    """
    Muestra el estudio de convergencia para distintos valores de longitud de viga y número de subintervalos, para
    una presión vertical determinada.

    :parameter p0: valor de presión vertical aplicado sobre la viga

    :return: guarda los resultados en su carpeta correspondiente
    """
    resultFolder = "EstudioConvergencia"
    if not os.path.isdir(os.path.join(resultFolder)):
        os.mkdir(os.path.join(resultFolder))
    # p0 = 1
    prefix = "P" + str(p0)
    if not os.path.isdir(os.path.join(resultFolder, prefix)):
        os.mkdir(os.path.join(resultFolder, prefix))
    L = [2 * i for i in range(1, 10)]

    DiffVector = []
    for i in L:
        print("Calculos para l=", str(i))
        Nvector, Diff = ModuleConvergencia(l=i, p0=p0)
        DiffVector.append(Diff)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    # fig.suptitle("Convergencia hacia la solución")
    index = 0
    ax1.plot(Nvector, DiffVector[index])
    ax1.set_title("Norma de la diferencia entre modelos\n para una barra de longitud " + str(2 * L[index]) + " m\n"
                  + "y una presión vertical de " + str(p0) + " N/m")
    ax1.set_xlabel("Número de subintervalos, N.")
    ax1.set_ylabel("Norma, M(ξ), Nm")
    index = len(L) - 1
    ax2.plot(Nvector, DiffVector[index])
    ax2.set_title("Norma de la diferencia entre modelos\n para una barra de longitud " + str(2 * L[index]) + " m\n"
                  + "y una presión vertical de " + str(p0) + " N/m")
    ax2.set_xlabel("Número de subintervalos, N.")
    ax2.set_ylabel("Norma, M(ξ), Nm")
    name = os.path.normpath(''.join([resultFolder, "/", prefix,"/Diff2plot", prefix, ".png"]))
    fig.savefig(name)

    fig2 = plt.figure(2, figsize=(6.5, 6))
    leyenda = []
    for i in range(len(L)):
        plt.plot(Nvector, DiffVector[i])
        leyenda.append(str(2 * L[i]) + " m")
    plt.title("Norma de la diferencia entre modelos\n para distintas longitudes\n"
              + "y una presión vertical de " + str(p0) + " N/m")
    plt.xlabel("Número de subintervalos, N.")
    plt.ylabel("Norma, M(ξ), Nm")
    plt.legend(leyenda)
    name = os.path.normpath(''.join([resultFolder, "/", prefix, "/DiffSamePlot", prefix, ".png"]))
    resultados = pd.DataFrame(DiffVector)
    resultados = resultados.transpose()
    resultados.columns = leyenda
    resultados.to_csv(''.join([resultFolder, "/", prefix, "/Diff", prefix, ".csv"]))
    fig2.savefig(name)
    fig2.clf()


def resolucionConvergencia():
    """
    :return: Realiza un estudio de convergencia para los valores de presión vertical p=5 N/m y 16 N/m
    """
    p = [5, 16]
    for i in p:
        print("Comparativa con carga vertical uniforme de p0 = " + str(i) + " N/m")
        convergencia(i)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        try:
            modo = int(sys.argv[1])
            if modo == 1:
                print("Has elegido el apartado A: Método de diferencias finitas\n")
                resolucionApartadoA()
            elif modo == 2:
                print("Has elegido el apartado B: Método del disparo\n")
                resolucionApartadoB()
            elif modo == 3:
                print("Has elegido el apartado de comparativa\n")
                resolucionComparativa()
            elif modo == 4:
                print("Has elegido el apartado de estudio de convergencia del método de diferencias finitas\n")
                resolucionNormaDiferenciasFinitas()
            elif modo == 5:
                print("Has elegido el apartado de estudio de convergencia del método del disparo\n")
                resolucionNormaMetodoDisparo()
            elif modo == 6:
                print("Has elegido el apartado de estudio de convergencia a la misma solución\n")
                resolucionConvergencia()
            else:
                print("Elige otra funcion diferente\n")
        except ValueError:
            print("Por favor, selecciona un apartado para obtener un resultado.\n")
    else:
        print("Por favor, selecciona un apartado para obtener un resultado.\n")

