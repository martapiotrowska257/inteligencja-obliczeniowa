from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier

# podpunkt a

iris = load_iris()
datasets = train_test_split(iris.data, iris.target,
                            test_size=0.7)
# podpunkt b
train_data, test_data, train_labels, test_labels = datasets

# print(iris)
# Liczby: 0,1,2
# 0: setosa
# 1: versicolor
# 2: virginica

# podpunkt d
two_neur_mlp = MLPClassifier(hidden_layer_sizes=(2,), max_iter=5000, random_state=25)

# podpunkt e
two_neur_mlp.fit(test_data, test_labels)
two_neur_pred_dd = two_neur_mlp.predict(test_data)
two_neur_accuracy = two_neur_mlp.score(test_data, test_labels)
two_neur_procent_dd = two_neur_accuracy * 100
print(f"MLP z 2 neuronami w ukrytej warstwie - dokładność: {two_neur_procent_dd:.2f}%")
print("\n", "------------------------------")

# podpunkt f
three_neur_mlp = MLPClassifier(hidden_layer_sizes=(3,), max_iter=5000, random_state=25)

three_neur_mlp.fit(test_data, test_labels)
three_neur_pred_dd = three_neur_mlp.predict(test_data)
three_neur_accuracy = three_neur_mlp.score(test_data, test_labels)
three_neur_procent_dd = three_neur_accuracy * 100
print(f"MLP z 3 neuronami w ukrytej warstwie - dokładność: {three_neur_procent_dd:.2f}%")
print("\n", "------------------------------")

# podpunkt g
three_three_neur_mlp = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=5000, random_state=25)

three_three_neur_mlp.fit(test_data, test_labels)
three_three_neur_pred_dd = three_three_neur_mlp.predict(test_data)
three_three_neur_accuracy = three_three_neur_mlp.score(test_data, test_labels)
three_three_neur_procent_dd = three_three_neur_accuracy * 100
print(f"MLP z parą ukrytych wartstw każda po 3 neurony - dokładność: {three_three_neur_procent_dd:.2f}%")

