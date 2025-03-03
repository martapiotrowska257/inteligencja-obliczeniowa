import random
import math
import matplotlib

matplotlib.use('TkAgg')  # Wymuszenie backendu
import matplotlib.pyplot as plt
import numpy as np

v = 50
h = 100
g = 9.81


def calc_distance(alfa, v, g, h):
    alfa = math.radians(alfa)
    sin_alfa = math.sin(alfa)
    cos_alfa = math.cos(alfa)
    v_y_final = math.sqrt(v ** 2 * sin_alfa ** 2 + 2 * g * h)  # prędkość vy w momencie uderzenia pocisku w ziemię
    d = (v * sin_alfa + v_y_final) * (v * cos_alfa / g)  # zasięg
    return d


# podpunkt 3

def plot_trajectory(alfa, v, g, h, target):
    alfa = math.radians(alfa)
    sin_alfa = math.sin(alfa)
    cos_alfa = math.cos(alfa)

    d = calc_distance(alfa, v, g, h)

    # wartości x od 0 do targetu
    x_values = np.linspace(0, target, num=1000)

    # wartości y według wzoru trajektorii
    y_values = (-g / (2 * v ** 2 * cos_alfa ** 2)) * x_values ** 2 + (sin_alfa / cos_alfa) * x_values + h
    print("Min y:", min(y_values))  # Jeśli min > 0, to coś jest źle

    # znalezienie dokładnego miejsca, gdzie y przecina oś OX (ostatni punkt lotu)
    if y_values[-1] > 0:    # wykres kończy się nad osią OX
        for i in range(len(y_values) - 1):
            if y_values[i] > 0 and y_values[i+1] < 0:
                x0, y0 = x_values[i], y_values[i]   # punkt poniżej osi OX
                x1, y1 = x_values[i + 1], y_values[i + 1]   # punkt powyżej osi OX

                # interpolacja liniowa, aby znaleźć dokładny x, dla którego y = 0
                x_land = x0 - (y0 * (x1 - x0) / (y1 - y0))

                print(f"Interpolacja: x0={x0}, y0={y0}, x1={x1}, y1={y1}, x_land={x_land}")  # Debug

                # dodajemy nowy punkt do listy, aby wykres kończył się na ziemi
                x_values = np.append(x_values[:i + 1], x_land)
                y_values = np.append(y_values[:i + 1], 0)
                break

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, label="Trajektoria lotu pocisku")
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.axvline(target, color='red', linestyle='--', label="Cel")
    plt.xlabel("Odległość d (m)")
    plt.ylabel("Wysokość h (m)")
    plt.title("Ruch ukośny pocisku")
    plt.legend()
    plt.grid()
    plt.show(block=True)


def hit_the_target(v, g, h):
    target = 260
    print("\nCel do trafienia: ", target)

    counter = 0

    while True:
        alfa = int(input("\nPodaj kąt strzału: "))
        distance = calc_distance(alfa, v, g, h)
        print("Dystans wynosi: ", distance)
        counter += 1

        # if target - 5 <= calc_distance <= target + 5:
        if abs(distance - target) <= 5:
            print("Cel trafiony!")
            plot_trajectory(alfa, v, g, h, target)
            # counter += 1
            break
        else:
            print("Spróbuj ponownie")
            print("----------------")
            # counter += 1

    return counter


attempts = hit_the_target(v, g, h)
print("\nLiczba prób trafienia celu: ", attempts)
