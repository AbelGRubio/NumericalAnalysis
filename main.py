from module.functions import *
import matplotlib.pyplot as plt
import pandas as pd
import os


# def main():
#     print("hola, empieza el programa")
#     l = 1
#     N = 20
#     p0 = 5
#     prefix = "N" + str(N) + "P" + str(p0) + "l" + str(l)
#     resultFolder = "resultados"
#     if not os.path.isdir(resultFolder):
#         os.mkdir("resultados")
#     if not os.path.isdir(os.path.join(resultFolder, prefix)):
#         os.mkdir(os.path.join(resultFolder, prefix))
#     result = ShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
#     fig1 = plt.figure(1)
#     plt.plot(result[0], result[1])
#     plt.legend(["Método del disparo"])
#     plt.title("Diagrama de momento flector de la barra de longitud " + str(2*l) + " m\n"
#               "para una presión vertical de " + str(p0) + " N/m")
#     plt.xlabel("Longitud de la barra, ξ, m")
#     plt.ylabel("Momento flector, M(ξ), Nm")
#     # plt.show()
#     name = os.path.normpath(''.join([resultFolder, "/", prefix, "/MetodoDisparo", prefix, ".png"]))
#     fig1.savefig(name)
#     DataFrame = pd.DataFrame([])
#     DataFrame['xi'] = result[0]
#     DataFrame['M'] = result[1]
#     DataFrame['dMdxi'] = result[2]
#     # reverseResult = ReverseShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
#     # fig2 = plt.figure(2)
#     # plt.plot(result[0], result[1])
#     # plt.legend(["Método del disparo inverso"])
#     # plt.title("Diagrama de momento flector de la barra de longitud " + str(2*l) + " m\n"
#     #           "para una presión vertical de " + str(p0) + " N/m")
#     # plt.xlabel("Longitud de la barra, ξ, m")
#     # plt.ylabel("Momento flector, M(ξ), Nm")
#     # plt.show()
#     # name = os.path.normpath(''.join([resultFolder, "/", prefix, "/MetodoDisparoInverso", prefix, ".png"]))
#     # fig2.savefig(name)
#     # ReverseDataFrame = pd.DataFrame([])
#     # ReverseDataFrame['xi'] = reverseResult[0]
#     # ReverseDataFrame['M'] = reverseResult[1]
#     # ReverseDataFrame['dMdxi'] = reverseResult[2]
#     linearResult = LinearFiniteDifference(N-1, -l, l, 0, 0, defineEquation1(l, p0))
#     fig3 = plt.figure(3)
#     plt.plot(linearResult[0], linearResult[1])
#     plt.legend(["Método de diferencias finitas"])
#     plt.title("Diagrama de momento flector de la barra de longitud " + str(2*l) + " m\n"
#               "para una presión vertical de " + str(p0) + " N/m")
#     plt.xlabel("Longitud de la barra, ξ, m")
#     plt.ylabel("Momento flector, M(ξ), Nm")
#     # plt.show()
#     name = os.path.normpath(''.join([resultFolder, "/", prefix, "/MetodoDiferenciasFinitas", prefix, ".png"]))
#     fig3.savefig(name)
#     LinearDataFrame = pd.DataFrame([])
#     LinearDataFrame['xi'] = linearResult[0]
#     LinearDataFrame['M'] = linearResult[1]
#     fig4 = plt.figure(4)
#     plt.plot(result[0], result[1])
#     # plt.plot(reverseResult[0], reverseResult[1])
#     plt.plot(linearResult[0], linearResult[1])
#     plt.legend(["Método del disparo", "Método de diferencias finitas"])
#     plt.title("Diagrama de momento flector de la barra de longitud " + str(2*l) + " m\n"
#               "para una presión vertical de " + str(p0) + " N/m")
#     plt.xlabel("Longitud de la barra, ξ, m")
#     plt.ylabel("Momento flector, M(ξ), Nm")
#     # plt.show()
#     name = os.path.normpath(''.join([resultFolder, "/", prefix, "/Total", prefix, ".png"]))
#     fig4.savefig(name)
#     DataFrame.to_csv(os.path.normpath(''.join([resultFolder, "/", prefix,
#                                                "/MetodoDisparo", prefix, ".csv"])))
#     # ReverseDataFrame.to_csv(os.path.normpath(''.join([resultFolder, "/", prefix,
#     #                                                   "/MetodoDisparoInverso", prefix, ".csv"])))
#     LinearDataFrame.to_csv(os.path.normpath(''.join([resultFolder, "/", prefix,
#                                                      "/MetodoDiferenciasFinitas", prefix, ".csv"])))
#
#     ComparationDataFrame = LinearDataFrame.copy()
#     ComparationDataFrame['MLinear'] = ComparationDataFrame['M']
#     del ComparationDataFrame['M']
#     ComparationDataFrame['MShoot'] = DataFrame['M']
#     ComparationDataFrame['Diff'] = abs(ComparationDataFrame['MLinear'] - ComparationDataFrame['MShoot'])
#     ComparationDataFrame.to_csv(os.path.normpath(''.join([resultFolder, "/", prefix,
#                                                           "/Comparacion", prefix, ".csv"])))
#     fig5 = plt.figure(5)
#     plt.plot(result[0], ComparationDataFrame['Diff'])
#     plt.title("Modulo entre modelos para una longitud de " + str(l) + " m\n"
#               + "y una presión vertical de " + str(p0) + " N/m")
#     plt.xlabel("Número de subintervalos, N.")
#     plt.ylabel("Módulo, M(ξ), Nm")
#     name = os.path.normpath(''.join([resultFolder, "/", prefix, "/DiffAbsoluta", prefix, ".png"]))
#     fig5.savefig(name)
#     print(sum(ComparationDataFrame['Diff'])/len(ComparationDataFrame['Diff']))
#     print(DataFrame)
#     # print(ReverseDataFrame)
#     print(LinearDataFrame)
#
#
# def main2():
#     l = 1
#     p0 = 5
#     N = 2
#     alpa = 0
#     beta = 0
#     NVector = [i*N for i in range(2, 20)]
#     ShootingVector = []
#     LinearVector = []
#     for NValue in NVector:
#         result = ShootingMethod(NValue, -l, l, alpa, beta, defineEquation1(l, p0), defineEquation2(l))
#         ShootingValue = result[1][len(result[1])-1]
#         ShootingVector.append(abs(ShootingValue))
#         linearResult = LinearFiniteDifference(NValue, -l, l, alpa, beta, defineEquation1(l, p0))
#         LinearValue = linearResult[1][len(linearResult[1])-1]
#         LinearVector.append(abs(LinearValue))
#
#     plt.figure(1)
#     plt.plot(result[0], result[1])
#     plt.legend(["Método del disparo"])
#     plt.title("Diagrama de momento flector de la barra de longitud " + str(2*l) + " m\n"
#               "para una presión vertical de " + str(p0) + " N/m")
#     plt.xlabel("Longitud de la barra, ξ, m")
#     plt.ylabel("Momento flector, M(ξ), Nm")
#     plt.figure(2)
#     plt.plot(linearResult[0], linearResult[1])
#     plt.legend(["Método del disparo"])
#     plt.title("Diagrama de momento flector de la barra de longitud " + str(2*l) + " m\n"
#               "para una presión vertical de " + str(p0) + " N/m")
#     plt.xlabel("Longitud de la barra, ξ, m")
#     plt.ylabel("Momento flector, M(ξ), Nm")
#
#     plt.figure(3)
#     plt.plot(NVector, ShootingVector)
#     plt.plot(NVector, LinearVector)
#     plt.legend(["Método del disparo", "Método de diferencias finitas"])
#     plt.title("Estabilidad y convergencia")
#     plt.xlabel("Número de subintervalos, N")
#     plt.ylabel("Error de convergencia")
#     plt.show()
#
#
# def calculaComparativa():
#     p = [1, 2, 4, 5, 8, 16]
#     for i in p:
#         print("Comparativa con carga vertical uniforme de p0 = " + str(i) + " N/m")
#         convergencia(i)
#
#
# def ComparativaLongitud(p0):
#     outFolder = "resultados"
#     if not os.path.isdir(outFolder):
#         os.mkdir(outFolder)
#     resultFolder = "ComparativaLongitud"
#     if not os.path.isdir(os.path.join(outFolder, resultFolder)):
#         os.mkdir(os.path.join(outFolder, resultFolder))
#     l1 = 1
#     N = 70
#     l=l1
#     result = ShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
#     linearResult = LinearFiniteDifference(N - 1, -l, l, 0, 0, defineEquation1(l, p0))
#     DataFrame = pd.DataFrame([])
#     DataFrame['xi'] = linearResult[0]
#     DataFrame['LFDM2'] = linearResult[1]
#     DataFrame['SM2'] = result[1]
#     DataFrame['Diff2'] = abs(DataFrame['LFDM2'] - DataFrame['SM2'])
#     l2 = 1
#     l = l2
#     print(l)
#     result16 = ShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
#     linearResult16 = LinearFiniteDifference(N - 1, -l, l, 0, 0, defineEquation1(l, p0))
#     DataFrame['LFDM16'] = linearResult16[1]
#     DataFrame['SM16'] = result16[1]
#     DataFrame['Diff16'] = abs(DataFrame['LFDM16'] - DataFrame['SM16'])
#     fig5, ax = plt.subplots()
#     ax.plot(DataFrame['xi'], DataFrame['LFDM2'])
#     ax.plot(DataFrame['xi'], DataFrame['SM2'])
#     ax.set_xlabel("Longitud de la barra, ξ, m")
#     ax.set_ylabel("Momento flector, M(ξ), Nm")
#     ax2 = ax.twinx()
#     ax2.plot(DataFrame['xi'], DataFrame['Diff2'], color='m')
#     ax2.set_ylabel("Módulo, M(ξ), Nm", color='m')
#     ax.legend(["Método de diferencias finitas", "Método del disparo"])
#     ax.set_title("Diagrama de momento flector para\n"
#                  "l=" + str(2*l1) + " m, N=" + str(N) + " y p0=" + str(p0) + " N/m")
#     # ax2.legend(["Diferencia entre los modelos"])
#     prefix = "N" + str(N) + "P" + str(p0) + "l" + str(l1)
#     name = os.path.normpath(''.join([outFolder, '/', resultFolder, "/ComparativaLong", prefix, ".png"]))
#     fig5.savefig(name)
#     plt.show()
#
#     fig6, ax6 = plt.subplots()
#     ax6.plot(DataFrame['xi'], DataFrame['LFDM16'])
#     ax6.plot(DataFrame['xi'], DataFrame['SM16'])
#     ax6.set_xlabel("Longitud de la barra, ξ, m")
#     ax6.set_ylabel("Momento flector, M(ξ), Nm")
#     ax7 = ax6.twinx()
#     ax7.plot(DataFrame['xi'], DataFrame['Diff16'], color='m')
#     ax7.set_ylabel("Módulo, M(ξ), Nm", color='m')
#     ax6.legend(["Método de diferencias finitas", "Método del disparo"])
#     ax6.set_title("Diagrama de momento flector para\n"
#                   "l=" + str(2*l2) + " m, N=" + str(N) + " y p0=" + str(p0) + " N/m")
#     # ax2.legend(["Diferencia entre los modelos"])
#     plt.show()
#     prefix = "N" + str(N) + "P" + str(p0) + "l" + str(l2)
#     name = os.path.normpath(''.join([outFolder, '/', resultFolder, "/ComparativaLong", prefix, ".png"]))
#     fig6.savefig(name)
#     print("1")
#

def resolucionApartadoA():
    l = 1
    N = 20
    p0 = 5
    prefix = "N" + str(N) + "P" + str(p0) + "l" + str(l)
    resultFolder = "ApartadoA"
    if not os.path.isdir(resultFolder):
        os.mkdir(resultFolder)
    if not os.path.isdir(os.path.join(resultFolder, prefix)):
        os.mkdir(os.path.join(resultFolder, prefix))
    result = ShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
    fig1 = plt.figure(1)
    plt.plot(result[0], result[1])
    plt.legend(["Método del disparo"])
    plt.title("Diagrama de momento flector de la barra de longitud " + str(2 * l) + " m\n"
                                                                                    "para una presión vertical de " + str(
        p0) + " N/m")
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


def resolucionApartadoB():

    l = 1
    N = 20
    p0 = 5
    prefix = "N" + str(N) + "P" + str(p0) + "l" + str(l)
    resultFolder = "ApartadoB"
    if not os.path.isdir(resultFolder):
        os.mkdir(resultFolder)
    if not os.path.isdir(os.path.join(resultFolder, prefix)):
        os.mkdir(os.path.join(resultFolder, prefix))
    result = LinearFiniteDifference(N-1, -l, l, 0, 0, defineEquation1(l, p0))
    fig1 = plt.figure(1)
    plt.plot(result[0], result[1])
    plt.legend(["Método de diferencias finitas"])
    plt.title("Diagrama de momento flector de la barra de longitud " + str(2 * l) + " m\n"
                                                                                    "para una presión vertical de " + str(
        p0) + " N/m")
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


def resolucionComparativaCustom(N, l, p0):
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
    ax2.set_ylabel("Módulo, M(ξ), Nm", color='m')
    ax.legend(["Método de diferencias finitas", "Método del disparo"])
    ax.set_title("Diagrama de momento flector para\n"
                 "l=" + str(2 * l) + " m, N=" + str(N) + " y p0=" + str(p0) + " N/m")
    name = os.path.normpath(''.join([resultFolder, "/", prefix, "/ComparativaLong", prefix, ".png"]))
    fig5.savefig(name)
    plt.show()
    return sum(ComparationDataFrame['Modulo'])/len(ComparationDataFrame['Modulo'])


def resolucionComparativa():
    resolucionComparativaCustom(20, 1, 5)
    resolucionComparativaCustom(70, 1, 5)
    resolucionComparativaCustom(150, 1, 5)


def convergencia(p0):
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
    ax1.set_title("Módulo entre modelos\n para una barra de longitud " + str(2 * L[index]) + " m\n"
                  + "y una presión vertical de " + str(p0) + " N/m")
    ax1.set_xlabel("Número de subintervalos, N.")
    ax1.set_ylabel("Módulo, M(ξ), Nm")
    index = len(L) - 1
    ax2.plot(Nvector, DiffVector[index])
    ax2.set_title("Módulo entre modelos\n para una barra de longitud " + str(2 * L[index]) + " m\n"
                  + "y una presión vertical de " + str(p0) + " N/m")
    ax2.set_xlabel("Número de subintervalos, N.")
    ax2.set_ylabel("Módulo, M(ξ), Nm")
    name = os.path.normpath(''.join([resultFolder, "/", prefix,"/Diff2plot", prefix, ".png"]))
    fig.savefig(name)

    fig2 = plt.figure(2, figsize=(6.5, 6))
    leyenda = []
    for i in range(len(L)):
        plt.plot(Nvector, DiffVector[i])
        leyenda.append(str(2 * L[i]) + " m")
    plt.title("Módulo entre modelos\n para distintas longitudes\n"
              + "y una presión vertical de " + str(p0) + " N/m")
    plt.xlabel("Número de subintervalos, N.")
    plt.ylabel("Módulo, M(ξ), Nm")
    plt.legend(leyenda)
    name = os.path.normpath(''.join([resultFolder, "/", prefix, "/DiffSamePlot", prefix, ".png"]))
    resultados = pd.DataFrame(DiffVector)
    resultados = resultados.transpose()
    resultados.columns = leyenda
    resultados.to_csv(''.join([resultFolder, "/", prefix, "/Diff", prefix, ".csv"]))
    fig2.savefig(name)
    fig2.clf()


def resolucionConvergencia():
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
                print("Has elegido el apartado A\n")
                resolucionApartadoA()
            elif modo == 2:
                print("Has elegido el apartado B\n")
                resolucionApartadoB()
            elif modo == 3:
                print("Has elegido el apartado de comparativa\n")
                resolucionComparativa()
            elif modo == 4:
                print("Has elegido el apartado de estudio de convergencia\n")
                resolucionConvergencia()
            else:
                print("Elige otra funcion diferente\n")
        except ValueError:
            print("Por favor, selecciona un apartado para obtener un resultado.\n")
    else:
        print("Por favor, selecciona un apartado para obtener un resultado.\n")

