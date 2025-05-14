import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters.plotters import plot_contour
from pyswarms.utils.plotters.formatters import Mesher
import matplotlib.pyplot as plt

# c1 - czynnik przyciągania do najlepszej pozycji cząstki
# c2 - czynnik przyciągania do najlepszego rozwiązania roju
# w (inercja): określa, jak mocno cząstki zależą od swojej poprzedniej prędkości
# (czyli jak bardzo cząstka chce lecieć dalej w tym samym kierunku, co poprzednio)

options = {'c1':0.5, 'c2':0.3, 'w':0.5}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
optimizer.optimize(fx.sphere, iters=50)
# tworzenie animacji
m = Mesher(func=fx.sphere)
animation = plot_contour(pos_history=optimizer.pos_history, mesher=m, mark=(0, 0))
animation.save('plots/plot0.gif', writer='imagemagick', fps=10)

# C1 = 0.5, C2 = 0.3, W = 0.5 (plot0.gif)
# Animacja radziła sobie dobrze, rój trzymał się blisko siebie, ale nie był w stanie znaleźć minimum.

# C1 = 2.0, C2 = 0.1, W = 0.5 (plot1.gif)
# Zmiana wartości C1 i C2 do ekstremalnych wartości spowodowała,
# że animacja była bardziej chaotyczna, a cząstki poruszały się w różnych kierunkach.
# Jednak roj był w stanie znaleźć minimum i radził sobie lepiej.

# C1 = 0.1, C2 = 2.0, W = 0.5 (plot2.gif)
# Odwrócenie wartości C1 i C2 spowodowało, że cząstki
# podążały za sobą, ale dalej w chaotyczny sposób.

# C1 = 0.5, C2 = 0.3, W = 2.0 (plot3.gif)
# Zmiana wartości W do 2.0 spowodowała, że cząstki uciekły poza
# granice i nie były w stanie znaleźć minimum.

# C1 = 0.5, C2 = 0.3, W = 2.0 (plot4.gif)
# Zmiana wartości W do 0.1 spowodowała, że cząstki poruszały się w
# najbardziej skorelowany sposób, ale nie były w stanie znaleźć minimum.
# Poszło im zdecydowanie najgorzej.