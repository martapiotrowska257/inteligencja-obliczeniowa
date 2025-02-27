import random
import math

v = 50
h = 100
g = 9.81


def calc_distance(alfa, v, g, h):
    alfa = math.radians(alfa)
    sin_alfa = math.sin(alfa)
    cos_alfa = math.cos(alfa)
    t = math.sqrt(v ** 2 * sin_alfa ** 2 + 2 * g * h)
    d = (v * sin_alfa + t) * (v * cos_alfa / g)
    return d


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
            # counter += 1
            break
        else:
            print("Spróbuj ponownie")
            print("----------------")
            # counter += 1

    return counter


attempts = hit_the_target(v, g, h)
print("\nLiczba prób trafienia celu: ", attempts)
