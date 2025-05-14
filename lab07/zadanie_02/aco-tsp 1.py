import matplotlib.pyplot as plt
import random
import time
from aco import AntColony
plt.style.use("dark_background")

filenames = [
    "aco-tsp_ant_count_50", "aco-tsp_ant_count_300", "aco-tsp_ant_count_500",
    "aco-tsp_alpha_0.5", "aco-tsp_alpha_1.0", "aco-tsp_alpha_2.0",
    "aco-tsp_beta_1.2", "aco-tsp_beta_2.7", "aco-tsp_beta_5.0",
    "aco-tsp_evaporation_0.40", "aco-tsp_evaporation_0.60", "aco-tsp_evaporation_0.80",
    "aco-tsp_constant_250", "aco-tsp_constant_1000", "aco-tsp_constant_1500",]
filename = "aco-tsp.png"

params = {
    #ant_count
    # "ant_count": 50, "alpha": 0.5, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300
    # "ant_count": 300, "alpha": 0.5, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300
    # "ant_count": 500, "alpha": 0.5, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300

    # alpha
    # "ant_count": 300, "alpha": 0.5, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300
    # "ant_count": 300, "alpha": 1.0, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300
    # "ant_count": 300, "alpha": 2.0, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300

    #beta
    # "ant_count": 50, "alpha": 1.0, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300
    # "ant_count": 50, "alpha": 1.0, "beta": 2.7, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300
    # "ant_count": 50, "alpha": 1.0, "beta": 5.0, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300

    # pheromone_evaporation_rate
    # "ant_count": 50, "alpha": 1.0, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300
    # "ant_count": 50, "alpha": 1.0, "beta": 1.2, "pheromone_evaporation_rate": 0.60, "pheromone_constant": 1000.0, "iterations": 300
    # "ant_count": 50, "alpha": 1.0, "beta": 1.2, "pheromone_evaporation_rate": 0.80, "pheromone_constant": 1000.0, "iterations": 300

    # pheromone_constant
    # "ant_count": 50, "alpha": 1.0, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 250.0, "iterations": 300
    # "ant_count": 50, "alpha": 1.0, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1000.0, "iterations": 300
    # "ant_count": 50, "alpha": 1.0, "beta": 1.2, "pheromone_evaporation_rate": 0.40, "pheromone_constant": 1500.0, "iterations": 300

    "ant_count": 50, "alpha": 1.0, "beta": 1.2, "pheromone_evaporation_rate": 0.60, "pheromone_constant": 1000.0, "iterations": 300
}

COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    (95, 50),
    (60, 20),
    (10, 10)
)

def random_coord():
    r = random.randint(0, len(COORDS))
    return r

def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    fig = plt.gcf()
    fig.set_size_inches([w, h])

def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)
    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))

plot_nodes()

start_time = time.time()
colony = AntColony(COORDS, **params)

optimal_nodes = colony.get_path()

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )

execution_time = time.time() - start_time
print(f"Execution time: {execution_time:.2f} seconds")
plt.savefig(filename, dpi=300, bbox_inches="tight")

# ----------------------------------------------------------------------------------------------------------------------
# WYNIKI W ZALEŻNOŚCI OD ZMIANY PARAMETRÓW:
# ----------------------------------------------------------------------------------------------------------------------

# Ilość 'mrówek' (ant_count):
# - 50 mrówek - 336.8903364868396, 5.82s -- wydajne rozwiązanie, dobrze rozwiązane (mała liczba mrówek w koloni)
# - 300 mrówek - 385.7593136405796, 23.13s -- pierwotne rozwiązanie, najgorsze rozwiązanie
# - 500 mrówek - 330.8197687931371, 49.34s -- długie wykonanie, rozwiązanie gorsze 50 mrówek

# Wyniki pokazują, że im więcej mrówek w kolonii, tym dłuższy jest czas wykonania programu.
# Wydaje się, że wieksza liczba mrówek zaczyna się gubić w poszukiwaniach, co prowadzi do gorszych wyników.
# Nie jest to do końca prawda. Po kilku próbach wywołania programu można zauważyć,
# że trzecie wykonanie z 500 mrówkami ma prawie idetyczny wynik jak pierwsze wykonanie z 50 mrówkami.
# Być może jest to kwestia losowości?

# ----------------------------------------------------------------------------------------------------------------------

# Alpha (zaufanie stadne):
# - 0.5 - 336.8903364868396, 25.34s
# - 1.0 - 323.6545432852203, 24.46s -- najlepsze rozwiązanie
# - 2.0 - 395.6770463783769, 24.18s -- nadmierne zaufanie, gorsze rozwiązanie

# Można zauważyć, że czas wykonania jest podobny w każdym przypadku, co oznacza, że alpha nie ma na to znaczącego wpływu.

# ----------------------------------------------------------------------------------------------------------------------
# UWAGA! Dla kolejnych elementów ant_count będzie 50, alpha 1.0
# ----------------------------------------------------------------------------------------------------------------------

# Beta (zaufanie indywidualne):
# - 1.2 - 390.79775884621955, 3.84s
# - 2.7 - 336.3889034340639, 4.08s
# - 5.0 - 378.73126854861437, 3.67s

# Beta nie wpływa znacząco na czas wykonania, choć jest on bardzo krótki względem poprzednich testów.
# Zmienia znacznie jednak rozwiązanie za każdym wykonaniem.

# ----------------------------------------------------------------------------------------------------------------------

# Pheromone evaporation rate (czas zapomnienia/parowania feromonów):
# - 0.40 - 378.73126854861437, 6.15s
# - 0.60 - 360.7799450921492, 5.42s
# - 0.80 - 336.3889034340639, 5.98s

# ----------------------------------------------------------------------------------------------------------------------

# Pheromone constant (siła feromonów):
# - 250.0 - 336.8903364868396, 5.74s
# - 1000.0 - 356.2023518454058, 6.18s
# - 1500.0 - 390.79775884621955, 6.29s

# ----------------------------------------------------------------------------------------------------------------------

# Czas wykonania nie zmienia się znacząco zmieniając parametry, poza ilością mrówek oraz alfą. Pozostałe parametry
# minimalnie zwiększa czas wykonania w zależności od wielkości ale nie są to czynniki decydujące.
# Ilość mrówek jest kluczowym czynnikiem decydującym o czasie wykonania algorytmu.

# Najbardziej optymalne rozwiązanie to:
# - 50 mrówek, alpha 1.0, beta 1.2, pheromone_evaporation_rate 0.60, pheromone_constant 1000.0
# 336.8903364868396, 356.2023518454058, 356.2023518454058  <6s