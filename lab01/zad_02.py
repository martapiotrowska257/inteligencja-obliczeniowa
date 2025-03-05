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

    # wartości x od 0 do przewidywanego zasięgu lotu d
    x_values = np.linspace(0, max(d, target), num=1000)

    # wartości y dla każdego x według wzoru trajektorii
    y_values = (-g / (2 * v ** 2 * cos_alfa ** 2)) * x_values ** 2 + (sin_alfa / cos_alfa) * x_values + h

    # znalezienie indeksu pierwszego punktu, w którym y < 0 (pocisk uderza w ziemię)
    impact_index = np.argmax(y_values < 0)

    # przycięcie trajektorii do momentu uderzenia w ziemię
    if impact_index > 0:
        x_values = x_values[:impact_index]
        y_values = y_values[:impact_index]

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
    plt.savefig('trajectory.png')


def hit_the_target(v, g, h):
    target = random.randint(50, 340)
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