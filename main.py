from module.functions import ShootingMethod, defineEquation1, defineEquation2, ReverseShootingMethod
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    print("hola, empieza el programa")
    l = 20
    N = 500
    p0 = 5
    result = ShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
    DataFrame = pd.DataFrame([])
    DataFrame['x'] = result[0]
    DataFrame['y'] = result[1]
    DataFrame['dydx'] = result[2]
    reverseResult = ReverseShootingMethod(N, -l, l, 0, 0, defineEquation1(l, p0), defineEquation2(l))
    ReverseDataFrame = pd.DataFrame([])
    ReverseDataFrame['x'] = reverseResult[0]
    ReverseDataFrame['y'] = reverseResult[1]
    ReverseDataFrame['dydx'] = reverseResult[2]
    plt.plot(result[0], result[1])
    plt.plot(reverseResult[0], reverseResult[1])
    plt.legend(["Shooting Method", "Reverse Shooting Method"])
    plt.show()
    print(DataFrame)