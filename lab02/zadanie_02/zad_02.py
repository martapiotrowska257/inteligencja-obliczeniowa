import matplotlib

matplotlib.use('TkAgg')

from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "c:\\Marta\\Studia\\semestr_4\\inteligencja_obliczeniowa\\inteligencja-obliczeniowa\\lab02\\zadanie_01\\iris1.csv")

X = df[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
y = df["variety"]


def count_pca(components):
    pca = PCA(n_components=components).fit(X)
    print(X.columns[:components].tolist())
    print(pca.explained_variance_ratio_)
    return sum(pca.explained_variance_ratio_)


print(count_pca(4))  # 100% wariancji
print("==============================")

print(count_pca(3))  # 99% wariancji
print("==============================")

print(count_pca(2))  # około 97/98% wariancji
print("==============================")

print(count_pca(1))  # 0.924618723201729, czyli poniżej 95% wariancji => ZA MALO
print("==============================")


# z tego wynika ze aby zachowac 95% wariancji potrzebujemy 2 pierwszych komponentow => potwierdzamy to wzorem


def count_loss():
    pca = PCA().fit(X)
    total_variance_sqrt = sum(pca.explained_variance_ ** 0.5)

    for n in range(4, 0, -1):
        pca_n = PCA(n_components=n).fit(X)
        kept_variance_sqrt = sum(pca_n.explained_variance_ ** 0.5)

        loss = (total_variance_sqrt - kept_variance_sqrt) / total_variance_sqrt
        explained_variance = sum(pca_n.explained_variance_ratio_)

        print(f"Strata informacyjna przy {n} komponentach: {loss:.4f} (Wariancja: {explained_variance:.4f})")


count_loss()

newIris = PCA(n_components=2).fit_transform(X)


def draw_plot():
    plt.scatter(newIris[y == "Setosa"][:, 0], newIris[y == "Setosa"][:, 1], c="red", label="Setosa")
    plt.scatter(newIris[y == "Versicolor"][:, 0], newIris[y == "Versicolor"][:, 1], c="green", label="Versicolor")
    plt.scatter(newIris[y == "Virginica"][:, 0], newIris[y == "Virginica"][:, 1], c="blue", label="Virginica")
    plt.legend()
    plt.savefig("c:\\Marta\\Studia\\semestr_4\\inteligencja_obliczeniowa\\inteligencja-obliczeniowa\\lab02"
                "\\zadanie_02\\zadanie_02.png")
    # plt.show()


draw_plot()
