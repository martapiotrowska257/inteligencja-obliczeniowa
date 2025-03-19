import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def draw_plot(data, name):
    colors = {"Setosa": "red", "Versicolor": "green", "Virginica": "blue"}
    for variety, color in colors.items():
        subset = data[data.variety == variety]
        plt.scatter(subset["sepal.length"], subset["sepal.width"], c=color, label=variety)

    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.legend()
    plt.savefig(f"c:\\Marta\\Studia\\semestr_4\\inteligencja_obliczeniowa\\inteligencja-obliczeniowa\\lab02"
                f"\\zadanie_03\\{name}.png")
    plt.show()


df = pd.read_csv("c:\\Marta\\Studia\\semestr_4\\inteligencja_obliczeniowa\\inteligencja-obliczeniowa\\lab02"
                 "\\zadanie_01\\iris1.csv")

draw_plot(df, "original")

# Normalizacja min-max
df_minmax = df.copy()
df_minmax[["sepal.length", "sepal.width"]] = MinMaxScaler().fit_transform(df_minmax[["sepal.length", "sepal.width"]])
draw_plot(df_minmax, "min-max")

# Standaryzacja z-score
df_zscore = df.copy()
df_zscore[["sepal.length", "sepal.width"]] = StandardScaler().fit_transform(df_zscore[["sepal.length", "sepal.width"]])
draw_plot(df_zscore, "z-score")

# Wnioski:
# dane oryginalne mają szeroki zakres wartości
# normalizacja min-max skaluje dane do zakresu [0,1], zmniejsza odchylenie standardowe
# standaryzacja Z-score centruje dane wokół 0, gdzie średnia wynosi 0, a odchylenie standardowe 1
